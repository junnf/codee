function dosubmit(){
     var in_1 = document.getElementById('pswd');
     var in_2 = document.getElementById('pswd1');
     var inpswd = document.getElementById('pswdmd5');
    if (in_1.value == in_2.value) {
        alert in_1.value;
        alert in_2.value;
        alert inpswd.value;
        inpswd.value = (in_1.value);
            return true ;
        }
    else{
            alert("password is error");
            return false;
         }
     return false;
}
