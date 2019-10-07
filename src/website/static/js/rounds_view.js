import { countdown } from "./countdown_timer.js";

//Modal handling
var modal = document.getElementById("js-create-round-modal");
var btn = document.getElementById("js-create-round-btn");
var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// Countdown Timers
const countdownTimers = document.querySelectorAll(".countdown-timer");
countdownTimers.forEach( (timer) => {
 countdown(timer, null, true);
});
