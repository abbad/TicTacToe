/*
    FEATURE tracking users.
(function () {
  //Establish a listener for the  submit form
  $("#login-form").on('submit', function(event) {
    event.preventDefault();
    /*
    var formData = $(this).serializeObject();
    var url = $(this).attr('action');
    // Send POST request
    $.ajax({
      type: "POST",
      url: url,
      data: formData,
      dataType: 'json',
      success: function(data) {
        if (data.success) {
            //window.location.href = data.redirect_url;
        }
        else {
        }
      },
      error: function(data) {
        $("#error").text(data.error_message);
      },
      complete: function(data) {
      }
    })
  })
})();*/