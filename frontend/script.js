var searchInput = document.getElementById("navBarSearch");
var searchBtn = document.getElementById("search_button");

// if (document.activeElement === searchInput) {
//     searchBtn.style.backgroundColor = "var(--primary-color)";
//     searchBtn.style.fill = "var(--dark-color)";
// };
searchInput.addEventListener('focusin', function() {
    searchBtn.style.backgroundColor = "var(--primary-color)";
    searchBtn.style.fill = "var(--dark-color)";
    searchInput.style.borderColor = "var(--primary-color)"
});
searchInput.addEventListener('focusout', function() {
    searchBtn.style.backgroundColor = "lightgrey";
    searchBtn.style.fill = "rgba(0,0,0,0.4)";
    searchInput.style.borderColor = "lightgrey"
});

var splide = new Splide('.splide', {
    type: 'loop',
    perPage: 3,
    perMove: 1,
    heightRatio: 0.2,
    autoWidth: true,
    gap: 8,
    pagination: false,
});
splide.mount();