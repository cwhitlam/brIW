function isValidString(string) {
    regex = /[a-z]/i
    return string.match(regex);
}

function validateFormInput(string) {
    const errorMessage = document.getElementById("js-error-message");
    const drinkInput = document.getElementById("js-drink-input");
    errorMessage.style.display = "none";
    if (!isValidString(drinkInput.value)) {
       errorMessage.style.display = "block";
       console.log("invalid string");
       return false;
    }
    return true;
}
