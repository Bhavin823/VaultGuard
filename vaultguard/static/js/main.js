document.addEventListener("DOMContentLoaded",function(){
    let copyicon = document.getElementById("copy-username-icon");
    var usernametooltip = document.getElementById("username-tooltip");
    // function for show star of password length
    function star(count){
        let star = "";
        for(let i=0; i<=count;i++){
            star+= "*";
        }
        return star;
    }
    
    if(copyicon && usernametooltip){
        
        // username-copy
        copyicon.addEventListener("click",function(){
            if (copyicon.classList.contains('fa-regular')){
                copyicon.classList.remove('fa-regular');
                copyicon.classList.add('fa-solid'); 
            }
        
            let usernameDisplay =  document.getElementById('username-display');
            let tempInput = document.createElement('input');
            tempInput.value = usernameDisplay.innerText;
            document.body.appendChild(tempInput);
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
            
            usernametooltip.classList.add("show");
            setTimeout(function(){
                usernametooltip.classList.remove("show");        
            },1500)
        });
    }

    // password-copy
    let copyPasswordIcon = document.getElementById("copy-password-icon");
    let passwordtooltip = document.getElementById('password-tooltip');
    let ogPassword = document.getElementById("ogpwd");
    

    if(copyPasswordIcon && passwordtooltip && ogPassword){
        copyPasswordIcon.addEventListener("click",function(){
            if(copyPasswordIcon.classList.contains('fa-regular')){
                copyPasswordIcon.classList.remove('fa-regular');
                copyPasswordIcon.classList.add('fa-solid')
            }
        
            let passwordDisplay = document.getElementById('password-display');
            let tempInput = document.createElement('input');
            tempInput.value = ogPassword.value;
            document.body.appendChild(tempInput);
            document.execCommand("copy");
            tempInput.select();
            document.execCommand("copy");
            document.body.removeChild(tempInput);
        
            passwordtooltip.classList.add("show");
            setTimeout(function(){
                passwordtooltip.classList.remove("show");        
            },1500)
        });
        
    // togle-password visiability
    let togglePasswordIcon = document.getElementById('toggle-password-icon');
    let passwordDisplay = document.getElementById('password-display');
    
    if(togglePasswordIcon && passwordDisplay && ogPassword){
        passwordDisplay.innerText = star(ogPassword.value.length)
        
        let passwordVisible = false;
        
        togglePasswordIcon.addEventListener("click",function(){
            if (passwordVisible){
                passwordDisplay.textContent = star(ogPassword.value.length)
                passwordVisible = false;
                togglePasswordIcon.classList.remove("fa-eye");
                togglePasswordIcon.classList.add("fa-eye-slash");
            }else{
                passwordDisplay.textContent = ogPassword.value;
                passwordVisible = true;
                togglePasswordIcon.classList.remove("fa-eye-slash")
                togglePasswordIcon.classList.add("fa-eye");
            }
        
        });
    }
    }


    // serach site feature
    let serchInput = document.getElementById('search-site');
    
    if(serchInput){
        let serchText = '';
        let passList = JSON.parse(document.getElementById('listdata').innerText.replace(/'/g,'"'));
        let passwordList = document.querySelector('.password-list');
        
        const showPassword = () => {
            passwordList.innerHTML = '';
            
            let fragment = document.createDocumentFragment();

            passList.filter(password=>password.websitename.toLowerCase().includes(serchText.toLowerCase())
            ).forEach(password => {
            
                const div = document.createElement('div');
                div.classList.add('password-box');
        
                const h2 = document.createElement('h2');
                h2.classList.add('website-name');
                h2.innerText = password.websitename;
        
                const viewbutton = document.createElement('a');
                viewbutton.classList.add('view-button');
                viewbutton.href = `/vault/passwordDetailView/${password.id}/`;
                viewbutton.innerText = "View";
        
                div.appendChild(h2);
                div.appendChild(viewbutton);
                
                fragment.appendChild(div);
            });
            passwordList.innerHTML = '';
            passwordList.appendChild(fragment);
        };

        serchInput.addEventListener('input', _.debounce(function(event) {
            serchText = event.target.value;
            showPassword();
        }, 300)); // 300ms debounce interval

        // serchInput.addEventListener('input',function(event){
        //     serchText = event.target.value;
        //     showPassword();
        // },300);
        
    }  


    // password validation feature
    let pwdInput = document.getElementById('password');
    let pwdMsgItem = document.getElementsByClassName('password-message-item');
    let pwdMsg = document.getElementById('password-message');
    
    if(pwdInput && pwdMsgItem && pwdMsg){
        // click inside password field show validation box
        pwdInput.onfocus = function(){
            pwdMsg.style.display = "block";
        }

        // click outside password field hide validation box
        pwdInput.onblur = function(){
            pwdMsg.style.display = "none";
        }

        pwdInput.onkeyup = function(){
            // check lower letter 
            let lowercaseRegex = /[a-z]/g;
            if (pwdInput.value.match(lowercaseRegex)){
                pwdMsgItem[0].classList.remove("invalid");
                pwdMsgItem[0].classList.add("valid");
            }else{
                pwdMsgItem[0].classList.remove("valid");
                pwdMsgItem[0].classList.add("invalid");
            }

            // check uppper letter 
            let upppercaseRegex = /[A-Z]/g;
            if (pwdInput.value.match(upppercaseRegex)){
                pwdMsgItem[1].classList.remove("invalid");
                pwdMsgItem[1].classList.add("valid");
            }else{
                pwdMsgItem[1].classList.remove("valid");
                pwdMsgItem[1].classList.add("invalid");
            }


            // check number  
            let numberRegex = /[0-9]/g;
            if (pwdInput.value.match(numberRegex)){
                pwdMsgItem[2].classList.remove("invalid");
                pwdMsgItem[2].classList.add("valid");
            }else{
                pwdMsgItem[2].classList.remove("valid");
                pwdMsgItem[2].classList.add("invalid");
            }

            // check 8 character 
            if(pwdInput.value.length>=8){
                pwdMsgItem[3].classList.remove("invalid");
                pwdMsgItem[3].classList.add("valid");
            }else{
                pwdMsgItem[3].classList.remove("valid");
                pwdMsgItem[3].classList.add("invalid");
            }
        }


    } 
    
    // updatepassword page show-password-toggle
    let inputval = document.getElementById('updaepassword')
    let toggleupdatePasswordIcon = document.getElementById('toggle-updatepassword-icon');
    
    if(toggleupdatePasswordIcon && inputval){
        toggleupdatePasswordIcon.addEventListener("click",function(){
            if (inputval.type === 'password'){
                inputval.type = "text";
                toggleupdatePasswordIcon.classList.remove("fa-eye");
                toggleupdatePasswordIcon.classList.add("fa-eye-slash");
            }else{
                inputval.type = 'password'
                toggleupdatePasswordIcon.classList.remove("fa-eye-slash")
                toggleupdatePasswordIcon.classList.add("fa-eye");
            }
        
        });    
    }
});







