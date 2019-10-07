// Addd Person Modal handling
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

// Edit Person Modal Handling
var editPersonModal = document.getElementById("js-edit-person-modal");
var editPersonModalBtns = document.querySelectorAll(".js-edit-person-btn");
var editPersonCloseModalSpan = document.querySelectorAll(".close")[1];

editPersonModalBtns.forEach(function(el) {
  el.onclick = function() {
    editPersonModal.style.display = "block";
  };
});

editPersonCloseModalSpan.onclick = function() {
  editPersonModal.style.display = "none";
};

window.onclick = function(event) {
  if (event.target == editPersonModal) {
    editPersonModal.style.display = "none";
  }
}