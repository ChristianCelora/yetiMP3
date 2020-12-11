$(document).ready(function(){
    console.log("yeti mp3");

    $("#yt-form-submit").click(function(){
        console.log("form submit")
        // should be AJAX call 
        $("#yt-form").submit()
    })
});