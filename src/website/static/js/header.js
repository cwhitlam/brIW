const navBar    = document.querySelector("#nav-bar");
const navBarBtn = document.querySelector('#menu-icon');
navBarBtn.addEventListener("click", function(){
    
    if (navBar.style.display == "none") {
        navBar.style.display = "block";
    } else {
        navBar.style.display = "none";
    }
})