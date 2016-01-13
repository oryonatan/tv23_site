var TV23 = {
    kdp: null
};

$(function () {

    "use strict";


    kWidget.addReadyCallback(function (playerId) {
        TV23.kdp = document.getElementById(playerId);
    });


    $("#save-start").click(function () {
        var x = TV23.kdp.evaluate("{video.player.currentTime}");
        $("#start").val(x);
        return false;
    });


    $('#add-snippet').ajaxForm(function (data) {
        $("#snippets").append(
            $("<li/>").html(data)
        );
    });

});