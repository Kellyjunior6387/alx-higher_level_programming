const $ = require('jquery');

// Import jQuery library

// Fetch character name from the URL
$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Display character name in the HTML tag DIV#character
    $('#character').text(data.name);
});