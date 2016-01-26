// function dosubmit(){
     // var in_1 = document.getElementById('pswd');
     // var in_2 = document.getElementById('pswd1');
     // var inpswd = document.getElementById('pswdmd5');
     // alert in_1.value;
     // if (in_1.value === in_2.value) {
        // alert in_1.value;
        // alert in_2.value;
        // alert inpswd.value;
        // inpswd.value = (in_1.value);
            // return true ;
        // }
    // else{
            // alert("password is error");
            // return false;
         // }
     // return false;
// }
function dosubmit(){
    var in_ = document.getElementById('pswd');
    var in2 = document.getElementById('pswd1');
    var inm = document.getElementById('pswdmd5');
    if (in_.value === in2.value && in_.value !== ''){
        inm.value = hex_md5(in2.value);
        alert('success');
        return true;
    }
    return false;
}
