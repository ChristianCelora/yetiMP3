$(document).ready(function(){
    console.log("yeti mp3");

    function validateUrl(url){
        console.log(url);
    }

    $("#yt-form-submit").click(function(){
        // should be AJAX call 
        // $("#yt-form").submit()
        var url = $("#yt_url").val();
        validateUrl(url);
        $.ajax({
            url: "/ajax/download_yt/",
            method: "POST",
            data: {
                "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
                "url": url
            },
            dataType: "json"
        }).done(function(data){
            console.log(data);
            if("status" in data && data["status"]){
                let get_params = "id=" + data["id"] + "&name=" + encodeURIComponent(data["name"]);
                console.log(get_params);
                window.location = "/ajax/download/?" + get_params;
            }
        });
    });
});