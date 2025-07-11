document.addEventListener("DOMContentLoaded", function () {
    alert("Welcome to GillDev!");

    const navToggle = document.getElementById("nav-toggle");
    const navMenu = document.getElementById("nav-menu");

    navToggle.addEventListener("click", function () {
        navMenu.classList.toggle("active");
        $('#nav-toggle').css('background', 'red');
    });

    const scorea = 'Hello';
    const scoreb = ' World!';
    const scorec = scorea + scoreb;
    alert(scorec);


});
