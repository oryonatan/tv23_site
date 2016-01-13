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
        $("#start").val(currentTime.toFixed(0));
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
        $("#snipEd_start_display")[0].innerHTML = $("#start").val();
        $("#snipEd_end_display")[0].innerHTML = $("#end").val();
        $("#snippet_editor").show();
        return false;
    });

    $("#snipEd_save").click(function(){
        $("#snippet_editor").hide();
        $("#start").val(0);
        $("#start").show();
        $("#snipEd_start").val($("#snipEd_start_display").text());
        $("#snipEd_end").val($("#snipEd_end_display").text());
        $("#save-start").show();
    });


    $('#add-snippet').ajaxForm(function (data) {
        $("#snippets").append(data);
    });

    function updateSnippetEndTimer(){
        var currentTime = TV23.kdp.evaluate("{video.player.currentTime}");
        $("#end").val(currentTime.toFixed(0));
    }

    function HHMMSStoSeconds(HH,MM,SS){
        return HH*3600+MM*60+SS;
    }

    $("body").on("click", ".jumpTo", function(){
        TV23.kdp.sendNotification("doSeek", $(this).data("start"));
    });

});