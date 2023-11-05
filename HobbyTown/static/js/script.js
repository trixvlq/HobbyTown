var modals = document.querySelectorAll(".modal");
var buttons = document.querySelectorAll(".openModalBtn");
var closeButtons = document.querySelectorAll(".close");

buttons.forEach(function (btn) {
    btn.onclick = function () {
        var modalId = btn.getAttribute("data-modal-id");
        var modal = document.querySelector("#modal_" + modalId);
        if (modal) {
            modal.style.display = "block";
        }
    };
});

closeButtons.forEach(function (closeBtn) {
    closeBtn.onclick = function () {
        var modal = closeBtn.parentElement; // Находим соответствующее модальное окно
        modal.style.display = "none";
    };
});

window.onclick = function (event) {
    modals.forEach(function (modal) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
};
