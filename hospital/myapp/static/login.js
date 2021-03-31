
function validate1(){
	var username = document.getElementById("username");
    var password = document.getElementById("password");
   
if(username.value==''){
	alert("please fill the username");
	username.focus();
	return false;
}
if(password.value==''){
	alert("please fill the password");
	password.focus();
	return false;
}
	var reg1=/^baban$/;
	
	if(!reg1.test(username.value)){
		alert("incorrect user name");
		username.focus();
		return false;
	}
	
	var reg1=/^b123$/;
	
	if(!reg1.test(password.value)){
		alert("incorrect password name");
		password.focus();
		return false;
	}
	
}
function validate2(){
	var username1 = document.getElementById("username1");
    var password1 = document.getElementById("password1");

if(username1.value==''){
	alert("please fill the username");
	username1.focus();
	return false;
}
if(password1.value==''){
	alert("please fill the password");
	password1.focus();
	return false;
}
	var reg1=/^doctor$/;

	if(!reg1.test(username1.value)){
		alert("incorrect user name");
		username1.focus();
		return false;
	}

	var reg1=/^d123$/;

	if(!reg1.test(password1.value)){
		alert("incorrect password name");
		password1.focus();
		return false;
	}

}