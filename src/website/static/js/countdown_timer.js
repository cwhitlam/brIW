export function countdown(el, onExpiry = null, useShortOutput = false) { 
    const expiry = el.getAttribute("data-expiry-datetime");
    const expiryDateTime = new Date(expiry);
    var interval = setInterval(() => {
        var now = new Date().getTime();
        var distance = expiryDateTime - now;

        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        if (seconds < 10) {
            seconds = "0" + seconds;
        }

        el.innerHTML = minutes + ":" + seconds + " Remaining";
        if (!useShortOutput) {
        el.innerHTML += " To Order";
        }

        if (distance < 0) {
            clearInterval(interval)
            el.innerHTML = "Expired "
            if (!useShortOutput) {
                el.innerHTML += expiry;
            }
            el.style.color = "red";
            if (onExpiry != null) {
                onExpiry();
            }
        }
    }, 1000);
};
