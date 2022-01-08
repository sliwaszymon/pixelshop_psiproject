$('document').ready(function(){

    let btn = document.querySelector("#btn");
    let sidebar = document.querySelector(".sidebar");
    let container = document.querySelector(".container")

    btn.onclick = function() {
        sidebar.classList.toggle("active");
        container.classList.toggle("activenav");
    }})