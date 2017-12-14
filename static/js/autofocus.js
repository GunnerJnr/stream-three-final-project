// Create a function that will handle delaying of auto focus to the input field
function delayFocusInput() {
    // scroll the window by 150 pixels vertically
    window.scrollBy(0, 150);
    // target the id of 'username' and auto focus into the input field.
    $("#id_username").focus();
}

// use setTimeout() to execute
setTimeout(delayFocusInput, 1000);
