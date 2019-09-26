function word(){
    var longest=0;
    var str=document.getElementById("sen").value;
    var str1=str.split(" ");
    for(i=0;i<str1.length;i++){
        if(longest<str1[i].length){
            longest=str1[i].length;
        }
    }
    window.alert(longest);
   
}  