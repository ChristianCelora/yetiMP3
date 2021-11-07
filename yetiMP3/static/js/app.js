var max_times = 20;
var delta_ms = 5000;

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
        if("status" in data && data["status"] &&  "task_id" in data){
            console.log("task created succesfully");
            // Check task status every delta_ms seconds
            checkTaskStatus(data["task_id"], 0).then(function(ret){
                $("#yt-form-loading").hide();
                $("#yt-form-container").show();
                if(ret && "file_name" in ret && "frontend_name" in ret){
                    downloadMp3(ret.file_name, ret.frontend_name);
                }else{
                    alert("Errore download file");
                }
            });
        }else{
            alert("Error creating task")
        }
    }).fail(function(xhr, textStatus, error){
        console.log(xhr);
    });
}

function validateUrl(url){
    console.log(url);
}

function parseRequestCheckTaskStatus(task_id){
    ret = $.ajax({
        url: "/ajax/async/check_task/",
        method: "POST",
        data: {
            "csrfmiddlewaretoken": $("input[name=csrfmiddlewaretoken]").val(),
            "task_id": task_id
        },
        dataType: "json",
        async: false
    });

    return (ret.status == 200) ? ret.responseJSON : null;
}

async function checkTaskStatus(task_id, i){
    ret = parseRequestCheckTaskStatus(task_id);
    if(ret && ret["status"] && ret["task"]["status"] == 1){
        return ret["task"];
    }else if(i >= max_times){
        return null;
    }
    await timeout(delta_ms);
    return checkTaskStatus(task_id, i+1);
}

function timeout(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function downloadMp3(id, file_name){
    window.location = "/ajax/download/" + id + "/" + encodeURIComponent(file_name);
}
