var modals = document.querySelectorAll(".modal");
var buttons = document.querySelectorAll(".openModalBtn");
var closeButtons = document.querySelectorAll(".close");

buttons.forEach(function (btn, index) {
    btn.onclick = function () {
        modals[index].style.display = "block";
    };
});

closeButtons.forEach(function (closeBtn, index) {
    closeBtn.onclick = function () {
        modals[index].style.display = "none";
    };
});

window.onclick = function (event) {
    modals.forEach(function (modal, index) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    });
};