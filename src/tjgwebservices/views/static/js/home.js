function registerValidation(){

					var pwInput = document.getElementById("psw");
					var confirmInput = document.getElementById("pswconfirm");
					var letter = document.getElementById("letter");
					var capital = document.getElementById("capital");
					var number = document.getElementById("number");
					var length = document.getElementById("length");
					var matchpw = document.getElementById("match");
					var registerButton = document.getElementById("register");

					confirmInput.onfocus = function() {
					  document.getElementById("message").style.display = "block";
					}

					confirmInput.onblur = function() {
					  document.getElementById("message").style.display = "none";
					}

					confirmInput.onkeyup = function() {
					  // Validate lowercase letters
					  var lowerCaseLetters = /[a-z]/g;
					  if(confirmInput.value.match(lowerCaseLetters)) { 
						letter.classList.remove("invalid");
						letter.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						letter.classList.remove("valid");
						letter.classList.add("invalid");
						registerButton.disabled = true;
					}

					  // Validate capital letters
					  var upperCaseLetters = /[A-Z]/g;
					  if(confirmInput.value.match(upperCaseLetters)) { 
						capital.classList.remove("invalid");
						capital.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						capital.classList.remove("valid");
						capital.classList.add("invalid");
						registerButton.disabled = true;
					  }

					  // Validate numbers
					  var numbers = /[0-9]/g;
					  if(confirmInput.value.match(numbers)) { 
						number.classList.remove("invalid");
						number.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						number.classList.remove("valid");
						number.classList.add("invalid");
						registerButton.disabled = true;
					  }

					  // Validate length
					  if(confirmInput.value.length >= 8) {
						length.classList.remove("invalid");
						length.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						length.classList.remove("valid");
						length.classList.add("invalid");
						registerButton.disabled = true;
					  }
					  
					  // Validate match
					  if(confirmInput.value === pwInput.value) {
						matchpw.classList.remove("invalid");
						matchpw.classList.add("valid");
						registerButton.disabled = false;
					  } else {
						matchpw.classList.remove("valid");
						matchpw.classList.add("invalid");
						registerButton.disabled = true;
					  }

					}


}


var navmenu = function (command){
	var container,form,divModalContent,anchorClose, h1;
	var labelUName, inputUName, labelPassword, inputPassword, submitButton;
	var p, labelName, inputName, labelEmail, inputEmail, labelRegion, selectRegion;
	var regions, labelProfession, selectProfession, professions;
	var labelReferred, selectReferred, referred, labelPasswordRepeat;
	var inputPasswordRepeat, inputPasswordRepeat, submitButton;
	
	switch(command){
		container = document.querySelector('#page-wrapper > div:nth-child(2)');
		form = document.createElement("form");
		form.setAttribute("method","post");
		form.setAttribute("action","/register");
		divModalContent = document.createElement("div");
		divModalContent.setAttribute("class","modal-content");
		anchorClose = document.createElement("a");
		anchorClose.setAttribute("href","#");
		anchorClose.innerHTML = "close";
		divModalContent.appendChild(anchorClose);
		h1 = document.createElement("h1");
		case "login":
			console.log("login");
			h1.innerHTML="Login";
			labelUName = document.createElement("label");
			labelUName.setAttribute("for","uname");
			divModalContent.appendChild(labelUName);
			inputUName = document.createElement("input");
			inputUName.setAttribute("name","uname");
			inputUName.setAttribute("type","text");
			inputUName.setAttribute("placeholder","Enter User Name");
			divModalContent.appendChild(inputUName);
			labelPassword = document.createElement("label");
			labelPassword.setAttribute("for","psw");
			labelPassword.innerHTML = "psw";
			divModalContent.appendChild(labelPassword);
			inputPassword = document.createElement("input");
			inputPassword.setAttribute("name","psw");
			inputPassword.setAttribute("id","psw");
			inputPassword.setAttribute("type","password");
			submitButton = document.createElement("button");
			submitButton.setAttribute("type","submit");
			submitButton.setAttribute("class","registerbtn");
			submitButton.setAttribute("id","register");
			submitButton.innerHTML="Register";
			
		case "signup":
			console.log("signup");
			h1.innerHTML="Register";
			divModalContent.appendChild(h1);
			p = document.createElement("p");
			p.innerHTML="Please fill in this form to create an account";
			divModalContent.appendChild(p);
			labelName = document.createElement("label");
			labelName.setAttribute("for","name");
			divModalContent.appendChild(labelName);
			inputName = document.createElement("input");
			inputName.setAttribute("name","name");
			inputName.setAttribute("type","text");
			inputName.setAttribute("placeholder","Enter Name");
			divModalContent.appendChild(inputName);
			labelUName = document.createElement("label");
			labelUName.setAttribute("for","uname");
			divModalContent.appendChild(labelUName);
			inputUName = document.createElement("input");
			inputUName.setAttribute("name","uname");
			inputUName.setAttribute("type","text");
			inputUName.setAttribute("placeholder","Enter User Name");
			divModalContent.appendChild(inputUName);
			labelEmail = document.createElement("label");
			labelEmail.setAttribute("for","email");
			divModalContent.appendChild(labelEmail);
			inputEmail = document.createElement("input");
			inputEmail.setAttribute("name","email");
			inputEmail.setAttribute("type","text");
			inputEmail.setAttribute("placeholder","Enter Email");
			divModalContent.appendChild(inputEmail);
			labelRegion = document.createElement("label");
			labelRegion.setAttribute("for","region");
			divModalContent.appendChild(labelRegion);
			selectRegion = document.createElement("select");
			regions = [{"americas":"Americas"},{"africa":"Africa"},
						{"asia":"Asia"},{"europe":"Europe"}];
			for (var i=0;i<regions.length;i++){
				var option = document.createElement("option");
				option.innerHTML = Object.values(regions[i])[0];
				option.value = Object.keys(regions[i])[0];
				selectRegion.append(option);
			}
			divModalContent.appendChild(selectRegion);
			labelProfession = document.createElement("label");
			labelProfession.innerHTML = "Profession";
			divModalContent.appendChild(labelProfession);
			selectProfession = document.createElement("select");
			professions = [{"it":"IT Professional"},{"student":"Student"},
						{"education":"Education"},{"commerce":"Commerce"},
						{"other":"Other"}];
			for (var i=0;i<professions.length;i++){
				var option = document.createElement("option");
				option.innerHTML =  Object.values(professions[i])[0];
				option.value = Object.keys(professions[i])[0];
				selectProfession.append(option);
			}
			divModalContent.appendChild(selectProfession);
			labelReferred = document.createElement("label");
			labelReferred.innerHTML = "Referred";
			divModalContent.appendChild(labelReferred);
			selectReferred = document.createElement("select");
			referred = [{"website":"Website"},{"search":"Search"},
						{"ad":"Online Ad"},{"email":"Email"},
						{"other":"Other"}];
			for (var i=0;i<referred.length;i++){
				var option = document.createElement("option");
				option.innerHTML = Object.values(referred[i])[0];
				option.value = Object.keys(referred[i])[0];
				selectReferred.append(option);
			}
			divModalContent.appendChild(selectReferred);
			labelPassword = document.createElement("label");
			labelPassword.setAttribute("for","psw");
			labelPassword.innerHTML = "psw";
			divModalContent.appendChild(labelPassword);
			inputPassword = document.createElement("input");
			inputPassword.setAttribute("name","psw");
			inputPassword.setAttribute("id","psw");
			inputPassword.setAttribute("type","password");
			inputPassword.setAttribute("placeholder","Enter Password");
			inputPassword.setAttribute("pattern","(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}");
			divModalContent.appendChild(inputPassword);
			labelPasswordRepeat = document.createElement("label");
			labelPasswordRepeat.setAttribute("for","psw-repeat");
			labelPasswordRepeat.innerHTML = "psw-repeat";
			divModalContent.appendChild(labelPasswordRepeat);
			inputPasswordRepeat = document.createElement("input");
			inputPasswordRepeat.setAttribute("name","psw-repeat");
			inputPasswordRepeat.setAttribute("id","pswconfirm");
			inputPasswordRepeat.setAttribute("type","password");
			inputPasswordRepeat.setAttribute("placeholder","Repeat Password");
			divModalContent.appendChild(inputPasswordRepeat);
			registerLogin = document.createElement("input");
			registerLogin.setAttribute("type","hidden");
			registerLogin.setAttribute("value","register");
			registerLogin.setAttribute("name","login");
			divModalContent.appendChild(registerLogin);
			var messageDiv = document.createElement("div");
			var messageDivHeading = document.createElement("h3");
			messageDivHeading.innerHTML = "Password must contain the following:";
			messageDiv.appendChild(messageDivHeading);
			var invalidMessages = [{"letter":"A lowercase letter"},{"capital":"A capital letter"},
								{"number":"A number"},{"length":"Minimum 8 characters"},
								{"match":"Confirm password matches"}];
			for (var i=0;i<invalidMessages.length;i++){
				var messageP = document.createElement("p");
				messageP.setAttribute("id",Object.keys(invalidMessages[i])[0]);
				messageP.setAttribute("class","invalid");
				messageP.innerHTML = Object.values(invalidMessages[i])[0];
				messageDiv.append(option);
			}
			divModalContent.appendChild(messageDiv);
			var inputCheckbox = document.createElement("input");
			inputCheckbox.setAttribute("type","checkbox");
			inputCheckbox.setAttribute("name","terms");
			inputCheckbox.setAttribute("value","agree");
			inputCheckbox.setAttribute("required","required");
			divModalContent.appendChild(inputCheckbox);
			submitButton = document.createElement("button");
			submitButton.setAttribute("type","submit");
			submitButton.setAttribute("class","registerbtn");
			submitButton.setAttribute("id","register");
			submitButton.innerHTML="Register";
			divModalContent.appendChild(submitButton);
			
			break;
		case "post":
			console.log("post");		
			break;
		case "profile":
			console.log("profile");	
			break;
		case "menu":
			console.log("menu");						
			break;
	}	
	divModal = document.createElement("div");
	divModal.setAttribute("class","modal");
	divModal.appendChild(divModalContent);
	divModal.style.display = "block";
	form.appendChild(divModal);
	container.appendChild(form);
	divModalContent.addEventListener("click",function(e){
		e.preventDefault();
		divModal.style.display ="none";
	});
	anchorClose.addEventListener("click",function(e){
		e.preventDefault();
		divModal.style.display ="none";
	});
	registerValidation();
	
}

