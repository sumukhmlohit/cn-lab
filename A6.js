function add(){
    var n1=+document.getElementById("no1").value;
    var n2=+document.getElementById("no2").value;
    var n3=n1+n2;
    window.alert(n3);
}

function sub(){
    var n1=+document.getElementById("no1").value;
    var n2=+document.getElementById("no2").value;
    var n3=n1-n2;
    window.alert(n3);
}

function mul(){
    var n1=+document.getElementById("no1").value;
    var n2=+document.getElementById("no2").value;
    var n3=n1*n2;
    window.alert(n3);
}

function div(){
    try{
    var n1=+document.getElementById("no1").value;
    var n2=+document.getElementById("no2").value;
    var n3=n1/n2;
    if(n2==0)
    window.alert("/ by 0 error");
    window.alert(n3);
    }
    catch(e){
        window.alert("/ by 0 error")
    }
}