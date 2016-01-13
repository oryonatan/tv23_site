var TV23 = {
    kdp: null
};

$(function () {

    "use strict";


kWidget.addReadyCallback(function (playerId) {
    TV23.kdp = document.getElementById(playerId);
});

var updateEndTimer;

$("#save-start").click(function() {
    var currentTime = TV23.kdp.evaluate("{video.player.currentTime}");
    $("#start").val(currentTime.toFixed(1));
    $("#save-start").hide();
    updateEndTimer = setInterval(updateSnippetEndTimer,100);
    $("#timer_end_span").show();
    return false;
});

$("#save-end").click(function() {
    clearInterval(updateEndTimer);
    var currentTime = TV23.kdp.evaluate("{video.player.currentTime}");
    $("#start").hide();
    $("#timer_end_span").hide();
    $("#snipEd_start")[0].innerHTML = $("#start").val();
    $("#snipEd_end")[0].innerHTML = $("#end").val();
    $("#snippet_editor").show();
    return false;
});

$("#snipEd_save").click(function(){
    $("#snippet_editor").hide();
    $("#start").val(0);
    $("#start").show();
    $("#save-start").show();
});

function updateSnippetEndTimer(){
    var currentTime = TV23.kdp.evaluate("{video.player.currentTime}");
    $("#end").val(currentTime.toFixed(1));
}

    $('#add-snippet').ajaxForm(function (data) {
        $("#snippets").append(
            $("<li/>").html(data)
        );
    });

});