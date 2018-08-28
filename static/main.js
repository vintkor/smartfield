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

    // ---------------------------- Запись данных поля в data атрибут при выборе ---------------------------- //
    $('#choice-field-id').on('change', function () {
        var self = this;
        $.ajax({
            url: window.location.href,
            data: {
                action: 'get_field_data',
                field_id: $(self).val()
            },
            success: function (response) {
                if (response.status) {
                    $(self).attr('data-field_data', JSON.stringify(response.field_data));
                }
            },
            error: function (e) {
                console.log(e);
            }
        });
    });

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
        var field_square = $('#choice-field-id').data('field_data').square;

        $.ajax({
            url: window.location.href,
            method: 'get',
            data: {
                'action': 'add_plan_item',
                'field_square': field_square
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
                $(el).val('');
            });
        }

    });

    //

    function set_data_after_technique_for_work_change(rowParent, data, el_class) {
        $(rowParent).find('.' + el_class).val(data);
    }

    function recountRowData(row) {
        var composition_driver = $(row).find('.composition_driver'),
            composition_others = $(row).find('.composition_others'),
            output_rate = $(row).find('.output_rate'),
            coast_for_output_rate_driver = $(row).find('.coast_for_output_rate_driver'),
            coast_for_output_rate_others = $(row).find('.coast_for_output_rate_others'),
            coefficient_for_quality_driver = $(row).find('.coefficient_for_quality_driver'),
            coefficient_for_quality_others = $(row).find('.coefficient_for_quality_others'),
            fuel_rate = $(row).find('.fuel_rate'),
            coefficient_recount = parseFloat($('.coefficient_recount').val()),
            volume_start = parseFloat($('.volume_start').val());

        var volume_finish = volume_start * coefficient_recount;
        $(row).find('.volume_finish').val(volume_finish);

        // К-во нормосмен механизаторов
        var output_rate_driver = 0;
        if (parseFloat(composition_driver.val()) >= 1) {
            output_rate_driver = volume_finish / parseFloat(output_rate.val());
        }
        $(row).find('.output_rate_driver').val(output_rate_driver);

        // К-во нормосмен других
        var output_rate_other = 0;
        if (parseFloat(composition_others.val()) >= 1) {
            output_rate_other = volume_finish / parseFloat(output_rate.val());
        }
        $(row).find('.output_rate_other').val(output_rate_other);

        // Затраты труда (человекочасы) механизаторов
        var labor_coast_driver = 0;
        if (output_rate_driver > 0) {
            labor_coast_driver = output_rate_driver * 7;
        }
        $(row).find('.labor_coast_driver').val(labor_coast_driver);

        // Затраты труда (человекочасы) других
        var labor_coast_other = 0;
        if (output_rate_driver > 0) {
            labor_coast_other = output_rate_driver * 7;
        }
        $(row).find('.labor_coast_other').val(labor_coast_other);

        // Оплата по тарифу за весь объём механизаторов
        var coast_for_all_output_rate_driver = 0;
        if (output_rate_driver > 0) {
            coast_for_all_output_rate_driver = output_rate_driver * parseFloat(coast_for_output_rate_driver.val());
        }
        $(row).find('.coast_for_all_output_rate_driver').val(coast_for_all_output_rate_driver);

        // Оплата по тарифу за весь объём других
        var coast_for_all_output_rate_others = 0;
        if (output_rate_other > 0) {
            coast_for_all_output_rate_others = output_rate_other * parseFloat(coast_for_output_rate_driver.val());
        }
        $(row).find('.coast_for_all_output_rate_others').val(coast_for_all_output_rate_others);

        // Всего по оплате труда механизаторов
        var all_salary_drivers = 0;
        if (coast_for_all_output_rate_driver > 0){
            all_salary_drivers = coast_for_all_output_rate_driver + coast_for_all_output_rate_driver * parseFloat(coefficient_for_quality_driver.val());
        }
        $(row).find('.all_salary_drivers').val(all_salary_drivers);

        // Всего по оплате труда других
        var all_salary_others = 0;
        if (coast_for_all_output_rate_driver > 0){
            all_salary_others = coast_for_all_output_rate_others + coast_for_all_output_rate_others * parseFloat(coefficient_for_quality_others.val());
        }
        $(row).find('.all_salary_others').val(all_salary_others);

        // Топливо На весь объём работ
        var all_fuel = 0;
        if (parseFloat(fuel_rate.val()) > 0) {
            all_fuel = parseFloat(fuel_rate.val()) * volume_finish;
        }
        $(row).find('.all_fuel').val(all_fuel);

    }

    $(document).on('change', '.planning-add-row-technique-for-work', function () {
        var workAndTecniqueID = $(this).val();
        var rowParent = $(this).parents('tr');

        $.ajax({
            url: window.location.href,
            data: {
                action: 'get_data_by_work_and_technique',
                work_and_technique_id: workAndTecniqueID
            },
            success: function (response) {
                set_data_after_technique_for_work_change(rowParent, response.composition_driver, 'composition_driver');
                set_data_after_technique_for_work_change(rowParent, response.composition_others, 'composition_others');
                set_data_after_technique_for_work_change(rowParent, response.output_rate, 'output_rate');
                set_data_after_technique_for_work_change(rowParent, response.coast_for_output_rate_driver, 'coast_for_output_rate_driver');
                set_data_after_technique_for_work_change(rowParent, response.coast_for_output_rate_others, 'coast_for_output_rate_others');
                set_data_after_technique_for_work_change(rowParent, response.coefficient_for_quality_driver, 'coefficient_for_quality_driver');
                set_data_after_technique_for_work_change(rowParent, response.coefficient_for_quality_others, 'coefficient_for_quality_others');
                set_data_after_technique_for_work_change(rowParent, response.fuel_rate, 'fuel_rate');

                recountRowData(rowParent);
            },
            error: function (e) {
                console.log(e);
            }
        });

    });

});

