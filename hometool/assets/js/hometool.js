$(document).ready(function () {
    
    initOnboardingDropdown();  

    //Navigation Tag Js
    $('.js-nav-tab').click(function (e) {
        $('.onboarding-container').hide();
        $('.js-nav-tab.active').removeClass('active');
        $('.js-nav-list').removeClass('appoint-active');
        $(this).addClass('active');
        $(this).tab('show');
        $('.appoint-tab.active').parents('.js-nav-list').addClass('appoint-active');
        e.preventDefault();
    });

    var currentTab = $('.onboarding-tab.active').attr('data-index');
    $('.onboarding-tab').click(function (e) {
        var activ_index = $(this).attr('data-index');
        if( activ_index < currentTab ) {
            $('.js-form-status').text('Save Changes');
        } else {
            $('.js-form-status').text('Next');
        }
        $('.onboarding-tab.active').removeClass('active');
        $(this).addClass('active');
        $(this).tab('show');
        e.preventDefault();
    });

    $('.js-form-status').click(function (e) {
        var next_tab = $('.onboarding-tab.active').parent('li').next();
        next_tab.find('a').triggerHandler('click');
        e.preventDefault();
    });

    //Custum Radio buttons toggles
    var $input = $('.js-radio-toggle > input:radio');
    $input.each(function () {
        if($(this).is(":checked") || $(this).checked || $(this).prop("checked")) {
            $(this).parent().addClass('active');
        }
    });

    $input.on('click', function (e) {
        var r_status = returnRadioState($(this));
    });
    
    //Checkbox js 
    var $checkbox = $('.js-checkbox-toggle > input:checkbox');
    $checkbox.each(function () {
        if($(this).is(':checked') || $(this).prop('checked') || $(this).checked ){
            $(this).parent().addClass('checked');
        }
    });

    $checkbox.click(function (e) {
        var state = returnCheckBoxState($(this));
    });

});

//Onboarding dropdown trigger and select...use only with select option form
function initOnboardingDropdown () {
    var $select = $('.js-select-menu');

    $select.each(function () {
        var $option = $(this).find('option');
        var $list_dropdown = $(this).siblings('.js-dropdown-list-target');
        // $list_dropdown.find('li').remove();
        // code to initialize the bootstrap style drop down for form select boxes.
        $option.each(function () {
            var list_item = '<li role="presentation"><a class="js-option" data-value="'+ $(this).val() +'" role="menuitem" tabindex="-1" href="#">'+ $(this).text() +'</a></li>';
            $list_dropdown.append(list_item);
        });
    });

    // Code to update the selected option of dropdown
    $('.js-option').on('click', function (e) {
        // set display text
        $(this).parents('ul').siblings('.dropdown-toggle').children('.dropdown-placeholder').hide();
        $(this).parents('ul').siblings('.dropdown-toggle').children('.dropdown-target').text($(this).text());
        // set the selector value
        $(this).parents('ul').siblings(".js-select-menu").val($(this).data("value")).change();
        e.preventDefault();
    });
}

function returnRadioState (radioInput) {
    var $radio = radioInput;
    if($radio.is(":checked") || $radio.checked || $radio.prop("checked")) {
        $radio.parent().addClass('active');
        var sibling = $radio.parents('.radio').siblings('.radio').find('input');
        sibling.parent().removeClass('active');
        return true;
    }
    e.stopPropagation();
}

function returnCheckBoxState (checkbox) {
    var $this = checkbox;
    if($this.is(':checked') || $this.prop('checked') || $this.checked ){
        $this.parent().addClass('checked');
        return true;
    } else {
        $this.parent().removeClass('checked');
        return false;
    }
    event.stopPropagation();
}
