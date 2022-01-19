$('document').ready(function(){

    let btn = document.querySelector("#btn");
    let sidebar = document.querySelector(".sidebar");
    let content_shop = document.querySelector(".content-shop");
    let content_main = document.querySelector(".content-main");
    let content_about_us = document.querySelector(".content-about-us");

    btn.onclick = function() {
        sidebar.classList.toggle("active");
        try{
            content_shop.classList.toggle("activenav");
        }catch{
            null;
        }
        try{
            content_main.classList.toggle("activenav");
        }catch{
            null;
        }
        try{
            content_about_us.classList.toggle("activenav");
        }catch{
            null;
        }
    }})