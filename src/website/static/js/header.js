const navBar    = document.querySelector("#nav-bar");
const navBarBtn = document.querySelector('#menu-icon');
function handleMenuClick(){
    if (navBar.style.display == "block" ) {
        navBar.style.display = "none";
    } else {
        navBar.style.display = "block";
    }
}