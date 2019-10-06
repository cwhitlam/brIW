// Modal handling
var modal = document.getElementById("js-create-person-modal");
var openModalBtn = document.getElementById("js-create-person-btn");
var closeModalSpan = document.getElementsByClassName("close")[0];

openModalBtn.onclick = function() {
  modal.style.display = "block";
}

closeModalSpan.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
