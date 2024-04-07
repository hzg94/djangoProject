$(document).ready(function () {
    $("#login_btn").click(function () {
        $.post("/api/login", {
            "username": $("#username_input").val(),
            "password": $("#password_input").val(),
        }, function (res) {
            console.log("111");
        });
    });
});