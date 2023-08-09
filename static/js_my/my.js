function confirmMsgApplyOrder() {
    return confirm("Принять заявку?");
}

function configMsgCloseOrder() {
    return confirm("Закрыть заявку?")
}

function configMsgDeleteOrder() {
    return confirm("Удалить заявку?")
}

function ifOpenOrder() {
    return confirm("Заявка уже принята")
}


$(document).ready(function () {
    $("#show-checkboxes").click(function () {
        $("#checkboxes-dropdown").toggle(); // Показать/скрыть выпадающее окно
    });
});