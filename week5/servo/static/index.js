$(document).ready(function(){
    $(".button_control").click(function(){
        send_command($(this).val(), $(this))
    });
});


function send_command(command, clicked_button) {
    if (clicked_button.is(":enabled")) {
        $.ajax({
        type: "POST",
        url: "command",
        data: JSON.stringify({ command: command }),
        contentType: "application/json; charset=utf-8",
        beforeSend: function () {$(':button').prop('disabled', true);},
        success: function(data) {console.log(data);},
        error: function(errMsg) {alert(errMsg);},
        complete: function() {$(':button').prop('disabled', false);}
        });
    }
}