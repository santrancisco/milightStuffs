var selectedLight=[];
var baseurl = "http://10.1.1.12/api/";

function toggleMultiLight(light,button){
    var index = selectedLight.indexOf(light)
    if( index > -1){
       selectedLight.splice(index,1);
       $("#"+button).removeClass("active");
    } else {
       selectedLight.push(light);
       $("#"+button).addClass("active");

    }
}
function toggleLight(light,button){
       $("#select1").removeClass("active");
       $("#select2").removeClass("active");
       $("#select3").removeClass("active");
       selectedLight=[light];
       $("#"+button).addClass("active");
}


function sendtoLight(action){
    selectedLight.forEach(function(light){
        $.get(baseurl+light+"/"+action);
        setTimeout(function(){},1000);
    })

}

$("#select1").click(function(){
    toggleLight(1,"select1");
});
$("#select2").click(function(){
    toggleLight(2,"select2");
});
$("#select3").click(function(){
    toggleLight(3,"select3");
});


$("#btton").click(function(){
    sendtoLight("on");
});
$("#bttoff").click(function(){
    sendtoLight("off");
});
$("#bttdim").click(function(){
    sendtoLight("dimmer");
});
$("#bttbright").click(function(){
    sendtoLight("brighter");
});
$("#bttdis").click(function(){
    sendtoLight("disco");
});
$("#bttwarm").click(function(){
    sendtoLight("white");
});

function changecolor(button){
    console.log(button.innerHTML);
    var color=button.innerHTML;
    sendtoLight(color);
}

