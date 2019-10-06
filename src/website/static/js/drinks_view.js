//Modal handling
var modal = document.getElementById("js-create-drink-modal");
var btn = document.getElementById("js-create-drink-btn");
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

function isValidString(string) {
    regex = /[a-z]+/i
    return string.match(regex);
}

function validateFormInput() {
    event.preventDefault(); 
    const errorMessage = document.querySelector("#js-error-message");
    const drinkInput   = document.querySelector("#js-drink-input");
     
    errorMessage.style.display = "none";
    if (!isValidString(drinkInput.value)) {
       errorMessage.style.display = "block";
       return false;
    }
    event.currentTarget.submit();    
}
