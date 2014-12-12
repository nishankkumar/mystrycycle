$(document).ready(function(){
	initOnboardingDropdown();
});
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