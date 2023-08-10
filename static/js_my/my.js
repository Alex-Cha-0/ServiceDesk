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


(function activeLink() {
  [...this.querySelectorAll("a")]
    .filter(a => this.URL.startsWith(a.href))
    .forEach(a => a.classList.add("active"));
}.bind(window.document)());


$(".sidebar i").each(function () {
    if ((window.location.pathname.indexOf($(this).attr("href"))) > -1) {
        $(this).addClass("fa-beat");
    }
});
