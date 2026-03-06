function set_mode(){
    if(body.getAttribute("data-bs-theme") === "dark"){
        body.setAttribute("data-bs-theme","light");
        dark_mode.textContent="🌙";
        dark_mode.setAttribute("class","btn btn-dark btn-sm");
    } else {
        body.setAttribute("data-bs-theme","dark");
        dark_mode.textContent="☀️";
        dark_mode.setAttribute("class","btn btn-light btn-sm");
    }
}
window.onload = function () {
    
    const body = document.getElementById("body");

    const darkThemeMq = window.matchMedia("(prefers-color-scheme: dark)");

    if (darkThemeMq.matches) {
        body.setAttribute("data-bs-theme", "dark");
    } else {
        body.setAttribute("data-bs-theme", "light");
    }
}
/* 
function set_names(params) {
    let dark_mode=document.getElementById("mode");
    if (darkThemeMq.matches){
        dark_mode.textContent="☀️";
        dark_mode.setAttribute("class","btn btn-light btn-sm");
    }else{
        dark_mode.textContent="🌙";
        dark_mode.setAttribute("class","btn btn-dark btn-sm")
    }
}
function set_mode(){
    if(body.getAttribute("data-bs-theme") === "dark"){
        body.setAttribute("data-bs-theme","light");
        dark_mode.textContent="🌙";
        dark_mode.setAttribute("class","btn btn-dark btn-sm");
    } else {
        body.setAttribute("data-bs-theme","dark");
        dark_mode.textContent="☀️";
        dark_mode.setAttribute("class","btn btn-light btn-sm");
    }
} */