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
    const firstName = el.getAttribute("data-first-name");
    const surname = el.getAttribute("data-surname")
    const personId = el.getAttribute("data-person-id");
    const drinkId = el.getAttribute("data-drink-id");

    const personIdInput = document.querySelector("#js-person-id-input");
    const firstNameInput = document.querySelector("#js-first-name-input");
    const surnameInput = document.querySelector("#js-surname-input");
    const drinkSelect = document.querySelector("#js-drink-select"); 

    personIdInput.value = personId;
    firstNameInput.value = firstName;
    surnameInput.value = surname;
    setSelectedValue(drinkSelect, drinkId);


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

function setSelectedValue(selectInput, value) {
  for (var i = 0; i < selectInput.options.length; i++) {
    if (selectInput.options[i].value == value) {
        selectInput.options[i].selected = true;
        return;
    }
  }
}