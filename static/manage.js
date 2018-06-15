$(document).ready(function(){
     $("#encrypt").click(function(){
       $.post({
          url: "encrypt",
          data: JSON.stringify({ data: $("#encrypt_input").val(), password: $("#encrypt_pass").val()}),
          contentType: "application/json; charset=utf-8",
          success: function (data) {
            $("#encrypted_label").html(data);
        }
      });
     });
      $("#decrypt").click(function(){
       $.post({
          url: "decrypt",
          data: JSON.stringify({ data: $("#decrypt_input").val(), password: $("#decrypt_pass").val()}),
          contentType: "application/json; charset=utf-8",
          success: function (data) {
            $("#decrypted_label").html(data);
        }
      });
    });
});
