var styleCSS = document.getElementById('theme-css');
var styleChoice = document.getElementById('theme');

if(!localStorage.getItem('theme')) {
    populateStorage();
} else {
    setStyles();
}

function populateStorage() {
    localStorage.setItem('theme', document.getElementById('theme').value);

    setStyles();
}

function setStyles() {
    var currentChoice = localStorage.getItem('theme');

    document.getElementById('theme').value = currentChoice;

    styleCSS.setAttribute('href', currentChoice);
}

styleChoice.onchange = populateStorage;