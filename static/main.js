$(document).ready(function () {

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

    // =================================== ДОБАВЛЕНИЕ ПЛАНА ПОЛЯ =================================== //

    $('.select2').select2();

    $('#choice-agriculture-id').change(function () {
        var self = this;

        $.ajax({
            url: window.location.href,
            method: 'get',
            data: {
                action: 'get_seeds',
                agriculture_id: $(self).val()
            },
            success: function (response) {
                var seedsSelect = $('#choice-seeds-id');

                if (response.seeds.length > 0) {
                    seedsSelect.empty();

                    // var newOption2 = new Option('rwer', 're', false, false);
                    // seedsSelect.append(newOption2).trigger('change');

                    response.seeds.forEach(function (el) {
                        var newOption = new Option(el.title, el.id);
                        seedsSelect.append(newOption).trigger('change');
                        seedsSelect.prop("disabled", false);
                    });
                } else {
                    seedsSelect.empty();
                    seedsSelect.prop("disabled", true);
                }

            },
            error: function (e) {
                console.log(e.statusText)
            }
        });
    });


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
                console.log(response);
                table.append(response);
                table.find('.select2').select2({width: '100%'});
            },
            error: function (e) {
                console.log(e)
            }
        });

    });

});

