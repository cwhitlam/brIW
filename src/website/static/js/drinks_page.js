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
