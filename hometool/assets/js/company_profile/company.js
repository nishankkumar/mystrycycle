// js related to company profile pages
function updateTime(input) {
    var timeValue = input.val();
    var timeRegex = /^([01]\d|2[0-3]):?([0-5]\d)$/;
    if ((timeValue != '') && (timeRegex.test(timeValue))) {
        input.parent('.form-group').addClass('time-selected');
        var t = input.val();
        if(t.charAt(2) != ':') {
            var res = t.slice(0, 2) + ':' + t.slice(2 + Math.abs(0));
            input.val(res);
        }
        input.parent().removeClass('has-error');
    }
    else {
        input.parent().addClass('has-error');
    }
}

$(document).ready(function() {

    $('.js-time').each(function() {
        var time_value = $(this).val();
        if (time_value != "") {
            $(this).parent('.form-group').addClass('time-selected');
        } else {
            $(this).parent('.form-group').removeClass('time-selected');
        }
    });


    $('.js-time').on('change', function() {
        updateTime($(this));
    });

    $('.js-add-feild').on('click', function(e) {
        var tr = $(this).siblings('.js-licenses-wrap').children('.js-policy-group:last-child').find('.js-modify-feild');
        tr.trigger('click');
        e.preventDefault();
    });

    //Add/remove licence js
    $(document).on('click', '.js-modify-feild', function(event) {
        var $this = $(this);
        if ($this.hasClass('add')) {
            var new_feild = $this.parent('.js-policy-group').clone();
            $this.removeClass('add').text('-');
            $('.js-licenses-wrap').append(new_feild);
        } else {
            $this.parent('.js-policy-group').fadeOut('slow', function() {
                $this.parent('.js-policy-group').remove();
            });
        }
        event.preventDefault();
    });

    //Service Dropdown JS

    var $service_checkbox = $('.js-services-dropdown');
    var $label = $('.dropdown-menu').find('label');

    $label.click(function(e) {
        e.stopPropagation();
    });

    function updateInfo (dropdown, valueArray) {
        dropdown.siblings('.dropdown-trigger').children('.dropdown-placeholder').hide();
        if (valueArray[0] == 1) {
            dropdown.siblings('.dropdown-trigger').children('.dropdown-target').show().text(valueArray[1]);
        } else if( valueArray[0] > 1 ) {
            dropdown.siblings('.dropdown-trigger').children('.dropdown-target').show().text('Multiple Selected');
        } else {
            dropdown.siblings('.dropdown-trigger').children('.dropdown-target').hide();
            dropdown.siblings('.dropdown-trigger').children('.dropdown-placeholder').show().text(valueArray[2]);
        }
    }
    
    function updateInputDropdown ( dropdownList ) {
        var dropDownValue = new Array(0, "", "");
        var $dropDown = dropdownList;
        var options_checkbox = $dropDown.find('input[type="checkbox"]');
        dropDownValue[2] = $dropDown.children('.dropdown-placeholder').text();
        options_checkbox.each(function () {
            if ($(this).is(':checked') || $(this).prop('checked') || $(this).checked) {
                dropDownValue[0] += 1;
                dropDownValue[1] = $(this).siblings('span').text();
            }
        });
        updateInfo($dropDown, dropDownValue);
    }

    $service_checkbox.each(function() {
        var valueArray = new Array(0, "", "");
        var options_checkbox = $(this).find('input[type="checkbox"]');
        valueArray[2] = $(this).children('.dropdown-placeholder').text();
        options_checkbox.each(function () {
            if ($(this).is(':checked') || $(this).prop('checked') || $(this).checked) {
                valueArray[0] += 1;
                valueArray[1] = $(this).siblings('span').text();
            }
            $(this).click(function (e) {
                var parentList = $(this).parents('.js-services-dropdown');
                updateInputDropdown(parentList);
            });
        });
        updateInfo($(this), valueArray);
    });

    //dynamic content Remove JS
    $(document).on('click', '.js-remove-content', function(e) {
        $(this).parents('.js-content').find('.delete-body').fadeIn();
        e.preventDefault();
    });

    $(document).on('click', '.js-choice', function(e) {
        if ($(this).hasClass('remove')) {
            var container = $(this).parents('.js-content');
            container.fadeOut('slow', function() {
                container.remove();
            });
        } else {
            $(this).parents('.delete-body').fadeOut();
        }
        e.preventDefault();
    });

    //Edit Info JS
    $(document).on('click', '.js-modify-info', function(e) {
        var $editor = $(this).parents('.js-static-info').siblings('.js-content-edit');
        $(this).parents('.js-static-info').fadeOut();
        setTimeout(function() {
            $editor.fadeIn();
        }, 300);
        e.preventDefault();
    });

    $(document).on('click', '.js-cancel-edit', function(e) {
        var $holder = $(this).parents('.js-content-edit').siblings('.js-static-info');
        $(this).parents('.js-content-edit').fadeOut('slow', function() {
            $holder.fadeIn();
        });
        e.preventDefault();
    });

    //select Languages js for others part this only adds a input at bottom as text input
    $('.js-other-options > input').on('click', function(e) {
        var state = returnCheckBoxState($(this), e);
        if (state == true) {
            $(this).parent().siblings('.onboarding-input').removeClass('hide');
        } else {
            $(this).parent().siblings('.onboarding-input').addClass('hide');
        }
    });

    $(document).on('click', '.in-dropdown', function(e) {
        e.stopPropagation();
    });

    $('.js-area-dropdown').find('input:radio').click(function(e) {
        if ($(this).hasClass('js-radius-toggle')) {
            $(this).parents('.radio').siblings('.js-radius-select').removeClass('hide');
            $(this).parents('.radio').siblings('.map-container').removeClass('hide');
        } else {
            $(this).parents('li').siblings('.js-radius-select').addClass('hide');
            $(this).parents('.radio').siblings('.map-container').addClass('hide')
        }
    });
    var selectedRadius = 8046;
    var radiusArray = new Array(8046, 16093, 40234, 80467, 160934);
    //                          <10,   10,    25,    50,     100 miles

    $('.js-radius-select > button').on('click', function(e) {
        $('.js-radius-select').toggleClass('open');
        e.stopPropagation();
    });

    $('.js-radius-list').find('.js-option').click(function(e) {
        $(this).parents('.js-radius-select').toggleClass('open');
        var radiusValue = $(this).parents('.js-radius-list').siblings('#radiusInputValue').val();
        selectedRadius = radiusArray[radiusValue];
        $(this).parents('.js-radius-list').siblings('#map-radius').val(selectedRadius).change();
        var radiusInput = $(this).parents('.js-radius-list').siblings('#map-radius');
    });

    $(document).on('click', '.map-main', function(e) {
        e.stopPropagation();
    });

    $('.map-main').locationpicker({
        //dummy location, remove on integration or provide a default location, now it is austin,tx
        location: {
            latitude: 30.3077609,
            longitude: -97.7534014
        },
        radius: 300,
        scrollwheel: true,
        inputBinding: {
            radiusInput: $('#map-radius'), //radius parameter
            // $('#us5-street1').val(addressComponents.addressLine1); //address line1
            // $('#us5-city').val(addressComponents.city);            // city name
            // $('#us5-state').val(addressComponents.stateOrProvince);// state name
            // $('#us5-zip').val(addressComponents.postalCode);       // postalCode
            // $('#us5-country').val(addressComponents.country);      // Country
            // locationNameInput: $('#us2-address');
        }

    });

    $('.js-isadmin-toggle').each(function () {
        if($(this).is(':checked') || $(this).prop('checked') || $(this).checked){
            $(this).parents('.checkbox').siblings('.image-container').children('.profile-image').addClass('admin-ring');
        } else {
            $(this).parents('.checkbox').siblings('.image-container').children('.profile-image').removeClass('admin-ring');
        }
    });


    $(document).on('click', '.js-isadmin-toggle', function () {
        if($(this).is(':checked') || $(this).prop('checked') || $(this).checked){
            $(this).parents('.checkbox').siblings('.image-container').children('.profile-image').addClass('admin-ring');
        } else {
            $(this).parents('.checkbox').siblings('.image-container').children('.profile-image').removeClass('admin-ring');
        }
    });

});