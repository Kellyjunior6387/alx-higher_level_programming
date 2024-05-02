// Import jQuery library
var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.6.0.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

// Wait for jQuery to load
script.onload = function() {
    // Fetch the translation from the API
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Display the translation in the DIV#hello tag
        $('DIV#hello').text(data.hello);
    });
};