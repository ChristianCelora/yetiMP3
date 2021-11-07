$(document).ready(function(){
    console.log("yeti mp3");
    $("#yt-form-loading").hide();

    $("#yt-form-submit").click(function(){
        // should be AJAX call 
        // $("#yt-form").submit()
        $("#yt-form-loading").show();
        $("#yt-form-container").hide();
        var url = $("#yt_url").val();
        var name = $("#yt_new_name").val();
        parseRequestDownloadMp3Async(url, name)
    });
});

// function parseRequestDownloadMp3Sync(url, name){
//     validateUrl(url);
//     $.ajax({
//         url: "/ajax/download_yt/",
//         method: "POST",
//         data: {
//             "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
//             "url": url,
//             "name": name
//         },
//         dataType: "json"
//     }).done(function(data){
//         console.log(data);
//         if("status" in data && data["status"]){
//             window.location = "/ajax/download/" + data["id"] + "/" + encodeURIComponent(data["name"]);
//         }
//         $("#yt-form-loading").hide();
//         $("#yt-form-container").show();
//     }).fail(function(xhr, textStatus, error){
//         console.log(xhr);
//     });
// }

function parseRequestDownloadMp3Async(url, name){
    validateUrl(url);
    $.ajax({
        url: "/ajax/async/download_yt/",
        method: "POST",
        data: {
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
            "url": url,
            "name": name
        },
        dataType: "json"
    }).done(function(data){
        console.log(data);
        if("status" in data && data["status"]){
            console.log("task created succesfully")
            //Begin check cycle every x seconds
        }else{
            alert("Error creating task")
        }
        $("#yt-form-loading").hide();
        $("#yt-form-container").show();
    }).fail(function(xhr, textStatus, error){
        console.log(xhr);
    });
}

function validateUrl(url){
    console.log(url);
}