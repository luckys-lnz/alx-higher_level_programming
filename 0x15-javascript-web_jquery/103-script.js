$(document).ready(function() {
  // Function to fetch and display the translation
  function fetchTranslation() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }

  // Event handler for the button click
  $('#btn_translate').click(function() {
    fetchTranslation();
  });

  // Event handler for pressing Enter key in the input field
  $('#language_code').keypress(function(event) {
    if (event.which === 13) { // Enter key code
      fetchTranslation();
    }
  });
});

