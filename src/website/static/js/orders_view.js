import { countdown } from "./countdown_timer.js";
// Modal handling
var modal = document.getElementById("js-create-order-modal");
var openModalBtn = document.getElementById("js-create-order-btn");
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

// Countdown Timer
const timerSpan = document.getElementById("js-countdown-timer");
const onExpiry = function () {
  openModalBtn.style.display = "none";

}

countdown(timerSpan, onExpiry);


// Get person's drink preference
const personSelect = document.querySelector("#js-modal-person-select");

personSelect.onchange = function () {
  const personId = this.value;
  if (personId != "") {
    preSelectPersonsDrinkPreference(personId)
  }
}

const preSelectPersonsDrinkPreference = function(personId) {
  const drinkSelect = document.querySelector("#js-modal-drink-select");
  const url   = "/people/" + personId + "/drink";
  const xhttp = new XMLHttpRequest();
  
  xhttp.open("GET", url, true);

  xhttp.onprogress = function(e) {
    drinkSelect.value = "";
  }

  xhttp.onload = function(e) {
    const jsonResponse = JSON.parse(xhttp.responseText);
    if (jsonResponse == null || jsonResponse["drink_id"] == null) {
      return;
    }
    
    drinkSelect.value = jsonResponse["drink_id"];
  }

  xhttp.send(null);
}
