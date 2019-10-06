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
