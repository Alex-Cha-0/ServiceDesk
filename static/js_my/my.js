window.onload = function () {
    document.body.classList.add('loaded_hiding');
    window.setTimeout(function () {
      document.body.classList.add('loaded');
      document.body.classList.remove('loaded_hiding');
    }, 500);
  }

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

function tableSearch() {
    var phrase = document.getElementById('search-text');
    var table = document.getElementById('myTable2');
    var regPhrase = new RegExp(phrase.value, 'i');
    var flag = false;
    for (var i = 1; i < table.rows.length; i++) {
        flag = false;
        for (var j = table.rows[i].cells.length - 1; j >= 0; j--) {
            flag = regPhrase.test(table.rows[i].cells[j].innerHTML);
            if (flag) break;
        }
        if (flag) {
            table.rows[i].style.display = "";
        } else {
            table.rows[i].style.display = "none";
        }

    }
}

// $('.change-card').hover(
//     function (){
//         $('.change-card').css('background-color','#ebebeb')
//     },
//     function(){
//         $('.change-card').css('background-color','#FFF');
//     }
// )


