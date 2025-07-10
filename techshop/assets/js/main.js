document.addEventListener("DOMContentLoaded", function () {
    alert("Welcome to Techshop!");

    const navToggle = document.getElementById("nav-toggle");
    const navMenu = document.getElementById("nav-menu");

    navToggle.addEventListener("click", function () {
        navMenu.classList.toggle("active");
    });
});
