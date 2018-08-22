// Удаление элемента из ДОМ-дерева с анимацией
function deleteElFromDomWithAnimation(el) {
    $(el).css({
        backgroundColor: 'rgba(243, 227, 13, .4)'
    }).hide('slow');
    setTimeout(function () {
        $(el).remove();
    }, 800);
}

// Подстановка в select2 поле данных из ответа сервера
function resetSelect2(select2Element, response, propertyName, title) {
    if (response[propertyName].length > 0) {
        select2Element.empty();
        response[propertyName].forEach(function (el) {
            var newOption = new Option(el[title], el.id);
            select2Element.append(newOption).trigger('change');
            select2Element.prop("disabled", false);
        });
    } else {
        select2Element.empty();
        select2Element.prop("disabled", true);
    }
}

$(document).ready(function () {

    // ====================================================================== //
    // =========================  Установка csrf  =========================== //
    // ====================================================================== //

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function sameOrigin(url) {
        var host = document.location.host;
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    // ====================================================================== //
    // =================   Удаление элементов в справочнике  ================ //
    // ====================================================================== //

    $('.delete-reference-book-row').click(function (e) {
        e.preventDefault();

        var model = $(this).data('model'),
            pk = $(this).data('pk'),
            self = this,
            parentRow = $(this).parents('tr');

        swal({
            title: 'Вы уверены?',
            text: "Это действие может привести к непредвиденным результатам!",
            type: 'warning',
            showCancelButton: true,
            confirmButtonText: 'Да, удалить!'
        }).then(function (result) {
            if (result.value) {
                $.ajax({
                    url: window.location.origin
                        + '/dashboard/reference-books/delete-any-row/'
                        + model + '/'
                        + pk + '/',
                    method: 'post',
                    success: function (response) {
                        console.log(response);
                        if (response.status) {
                            deleteElFromDomWithAnimation(parentRow);
                            swal('Удалено!');
                        }
                    },
                    error: function (e) {
                        console.log(e);
                    }
                });
            }
        })

    });

    // ====================================================================== //
    // =======================   ДОБАВЛЕНИЕ ПЛАНА ПОЛЯ  ===================== //
    // ====================================================================== //

    // TODO Проверить, подключен ли select2 на странице
    $('.select2').select2();

    // ----------------------------- Подстановка доступных семян при выборе культуры ----------------------------- //
    $('#choice-agriculture-id').change(function () {
        var self = this;
        var seedsSelect = $('#choice-seeds-id');

        $.ajax({
            url: window.location.href,
            method: 'get',
            data: {
                action: 'get_seeds',
                agriculture_id: $(self).val()
            },
            success: function (response) {
                resetSelect2(seedsSelect, response, 'seeds', 'title');
            },
            error: function (e) {
                console.log(e);
            }
        });
    });

    // ----------------------------- Добавление строки ----------------------------- //
    $('#add-planning-add-row').click(function (e) {
        e.preventDefault();
        var table = $('#add-planning-table');

        $.ajax({
            url: window.location.href,
            method: 'get',
            data: {
                'action': 'add_plan_item'
            },
            success: function (response) {
                table.find('tbody').append(response);
                table.find('.select2').select2({width: '100%'});
            },
            error: function (e) {
                console.log(e)
            }
        });

    });

    // ----------------------------- Удаление строки ----------------------------- //
    $(document).on('click', '.add-plan-row__delete-row', function (e) {
        e.preventDefault();
        var parentRow = $(this).parents('tr');
        deleteElFromDomWithAnimation(parentRow);
        // TODO Перед удалением делать аякс запрос и удалять запись из БД
    });

    // ----------------------------- Подстановка ед измерения в добавленой строке ----------------------------- //
    $(document).on('change', '.planning-add-row-choice-work', function () {
        var workID = $(this).val();
        var unitSelect = $(this).parents('tr').find('.planning-add-row-choice-work-unit');
        var techniqueForWorkSelect = $(this).parents('tr').find('.planning-add-row-technique-for-work');

        $.ajax({
            url: window.location.href,
            method: 'get',
            data: {
                action: 'get_work_units',
                work_id: workID
            },
            success: function (response) {
                console.log(response);
                resetSelect2(unitSelect, response, 'units', 'title');
                resetSelect2(techniqueForWorkSelect, response, 'technique', 'farming_techniques');
            },
            error: function (e) {
                console.log(e);
            }
        });

    });

    // ----------------------------- Изменение данных для полей ДРУГИЕ ----------------------------- //
    $(document).on('change, input', '.other-parent', function () {
        var otherParentValue = parseInt($(this).val());
        var children = $(this).parents('tr').find('.other-child');

        if (otherParentValue > 0) {
            children.each(function (ind, el) {
                $(el).removeAttr('disabled');
            });
        } else {
            children.each(function (ind, el) {
                $(el).attr('disabled', true);
            });
        }

    });

});

