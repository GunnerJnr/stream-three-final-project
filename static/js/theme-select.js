// When the window has loaded
window.onload = function () {

    // create two variables that will store ID's
    var styleCSS = document.getElementById('theme-css');
    var styleChoice = document.getElementById('theme');

    // here we check to see if the local storage exists
    if (!localStorage.getItem('theme')) {
        // if it doesn't then we populate it
        populateStorage();
    } else {
        // otherwise we set the already stored chosen style
        setStyles();
    }

    // we define a function that will handle populating the storage
    function populateStorage() {
        // we set the items value of which we wish to store in local storage
        localStorage.setItem('theme', document.getElementById('theme').value);

        // now we call our setStyles function
        setStyles();
    }

    // create a function that will handle changing the style of the site to the chosen theme
    function setStyles() {
        // fetch and store the current choice
        var currentChoice = localStorage.getItem('theme');

        // set the element to the current choice
        document.getElementById('theme').value = currentChoice;

        // set the chosen attribute to the current choice
        styleCSS.setAttribute('href', currentChoice);
    }

    // call on our populate storage function
    styleChoice.onchange = populateStorage;
};