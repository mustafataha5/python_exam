


erorr_fname = document.querySelector("#error_fname ")
erorr_lname = document.querySelector("#error_lname ")
erorr_email = document.querySelector("#error_email  ")
erorr_password = document.querySelector("#error_password ")
erorr_mpassword = document.querySelector("#erorr_mpassword")
erorr_birth = document.querySelector("#error_birth")
error_login_email = document.querySelector("#error_login_email")
error_login_password = document.querySelector("#error_login_password")
const emailRegex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;;






function registeration_validate(){
    fname = document.forms['regForm']['first_name'].value
    lname = document.forms['regForm']['last_name'].value
    email = document.forms['regForm']['email'].value
    password = document.forms['regForm']['password'].value
    mpassword = document.forms['regForm']['confirm_password'].value 
    birth =  document.forms['regForm']['birthday'].value 
    erorr_fname.innerHTML =""
    erorr_lname.innerHTML =""
    erorr_email.innerHTML =""
    erorr_password.innerHTML =""
    erorr_mpassword.innerHTML =""
    flag = true
    
    if(fname == ''){
        erorr_fname.innerHTML = "please fill the First Name "
       // console.log(e_fname)
        flag = false;
    }
    if(lname == ''){
        erorr_lname.innerHTML = "please fill the Last Name "
       // console.log(e_fname)
       flag = false;
    }

    //print(String(email).toLowerCase().match( /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|.(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/))
    //console.log(emailRegex.test(email))
    if( !emailRegex.test(email)){
        erorr_email.innerHTML = "Invalid email address "
       // console.log(e_fname)
       flag = false;
    }

    if (password == ''){
        erorr_password.innerHTML ="please fill the password"
        flag=false
    }
    
    if (password !== mpassword){
        
        erorr_mpassword.innerHTML = "The confirm-PW does not match"
        flag=false
    }

    if(birth !==''){
        
        current_date =new Date()
        birth_date = new Date(birth)
        diff = (current_date - birth_date)/(1000*60*60*24)
        if(diff<0){
            erorr_birth.innerHTML="Birthday must be in past"
            flag=false
        }
        else if (diff < 13*365){
            erorr_birth.innerHTML="Just above 13 year are allowed"
            flag=false
        }
    }
    else{
        erorr_birth.innerHTML="Fill the birthday"
        flag= false
    }

    return flag

}

function login_validate(){
    email = document.forms['loginForm']['email'].value
    password = document.forms['loginForm']['password'].value
    error_login_email.innerHTML = ''
    error_login_password.innerHTML = ''
    flag = true
    if(email == ''){
        error_login_email.innerHTML="Fill email address"
        flag = false
    }
    if (email !== '' && !(emailRegex.test(email))){
        error_login_email.innerHTML="Invalid email address"
        flag = false
    }

    if (password == ''){
        error_login_password.innerHTML = 'Fill Password field'
        flag = false
    }
    return flag

}



