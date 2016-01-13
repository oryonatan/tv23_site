"use strict";
var TV23 = {
    kdp: null
};


kWidget.addReadyCallback(function (playerId) {
    TV23.kdp = document.getElementById(playerId);
});


$("#save-start").click(function() {
    var x = TV23.kdp.evaluate("{video.player.currentTime}");
    $("#start").val(x);
    return false;
});


