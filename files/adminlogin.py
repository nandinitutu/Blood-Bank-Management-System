import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Admin Sign IN</title>
  <link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css'>
  <link rel="stylesheet" href="./style.css">
  <script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>
</head>
<script >
  function login() {
                var email = document.getElementById("mail").value
                var psw = document.getElementById("pssw").value
                if(email == "nandini@gmail.com" && psw == "Nandini8"){
                    window.open("adminpage.py")
                }
                else{
                    window.alert("Incorrect Username or Password")
                }    
                
            }
            
</script>
<script>
    function myFunction() {
      var x = document.getElementById("pssw");
      if (x.type === "password") {
        x.type = "text";
        document.getElementById('show').style.display = "inline-block";
        document.getElementById('hide').style.display = "none";
      } else {
        x.type = "password";
        document.getElementById('show').style.display = "none";
        document.getElementById('hide').style.display = "inline-block";
      }
    }
    </script>
	<style>
		body {
  margin: 0;
  padding: 0;
  background-color: #eee;
  font-family: "Lato", sans-serif;
}

.container {
  width: 100vw;
  height: 100vh;
  position: relative;
}

.container .inner {

  width: 100%;
  height: 100%;
  top: 30px;
  position: center;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
  justify-content: center;
  align-items: center;
  background-color: rgba(0, 0, 0, 0.5);
  opacity: .5px;
  
}

.container .inner .background-wrapper {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 500;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: url("img/img3.gif");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.container .inner .logo {
  align-self: auto;
  min-height: 50px;
  width: 100px;
  margin: 25px 0;
  border-radius: 50%;
  text-align: center;
  z-index: 2;
}


.container .inner .login-wrapper {
  width: 100%;
  position: relative;
  z-index: 2;
}

.container .inner .login-wrapper .inner {
  width: 560px;
  min-height: 150px;
  margin: 0 auto;
  background-color: rgba(black,0.5);
  border-radius: 10px;
 
  padding: 20px;
}

.container .inner .login-wrapper .inner h1 {
  font-weight: 300;
  color: red;
  text-transform: uppercase;
  font-size: 24px;
}

.container .inner .login-wrapper .inner p {
  text-align: center;
  color: rgba(245, 232, 48, 0.897);
}


.container .inner .login-wrapper .inner #emailBox input[type=email] {
  background-color: transparent;
  width: 350px;
  border: none;
  border-bottom: 3px solid #28e77e;
  padding: 10px 5px 5px 5px;
  color: #fff;
  font-size: 16px;
  border-radius: 3px;
}

.container .inner .login-wrapper .inner #emailBox input[type=email]:focus {
  outline: none;
  background-color: none;
  color: none;
}

.container .inner .login-wrapper .inner #emailBox label {
  color: #28e77e;
  text-transform: uppercase;
  font-size: 17px;
}


.container .inner .login-wrapper .inner #passBox .form  {
  background-color: transparent;
  outline: none;
  border: none;
  width: 350px;
  border-bottom: 3px solid #28e77e;
  padding: 10px 5px 5px 5px;
  color: #fff;
  margin: 10px 0 0 0;
  font-size: 16px;
  border-radius: 3px;
  
}

.container .inner .login-wrapper .inner #passBox label {
  color: #28e77e;
  text-transform: uppercase;
  font-size: 17px;
}

.container .inner .login-wrapper .inner .btn {
  font-size: 17px;
  background-color: rgb(6, 87, 180);
  border-radius: 3px;
  cursor: pointer;
  margin: 20px 0;
  padding: 10px 25px;
  color: #fff;
  transition: all 0.4s ease-in-out;
  text-transform: uppercase;
  border: 1px solid rgb(8, 7, 7);
  border-radius: 6px;
}

.container .inner .login-wrapper .inner .btn i {
  font-size: 16px;
}

.container .inner .login-wrapper .inner .btn:hover {
  background-color: rgb(64, 180, 226);
  border: 1px solid rgb(8, 7, 7);
  color: rgb(8, 7, 7);
}
i{
  cursor: pointer;
  margin:4px 2px ;
  font-size: 15px;
}
.show{
  margin: 2px 4px;
}
#show{
  display: none;
}

	</style>

<body>

<!-- partial:index.partial.html -->
<div class="container">
			<div class="inner">

				<div class="background-wrapper"></dreiv>
				<!--<div style="background-image: url(' D:\ my folder\ Major Project\ red.gif');">-->

				
<br><br><br><br><br><br>
				<div class="login-wrapper">
					<div class="inner">
						<i class="fas fa-user-shield" style="color:rgb(105, 105, 105); font-size: 70px; "></i>
						<h1>Admin <span style="color: aliceblue;  text-transform: none;">Sign In</span></h1>
						<p>Welcome, please type your Email and Password to login.</p><br>

						<div id="emailBox">
							<input id="mail" type="email" name="Email"><br>
							<label for="Email">email*</label>
						</div>
						<div id="passBox">
							<input class="form" id="pssw" type="password" name="Password"><br>
						<label for="Password">password*</label>
							<i class="far fa-eye" id="show"  onclick="myFunction()" style="float: right;cursor: pointer;margin: 4px 10px; font: 18px;position: relative; margin-top:-30px;color: #28e77e;"></i>
							<i class="far fa-eye-slash" id="hide" onclick="myFunction()"style="float: right;cursor: pointer;margin: 4px 10px; font: 18px;position: relative; margin-top:-30px;color: #28e77e;"></i>
						</div>
						

						
						<div class="btn-wrapper">
							<button id="login" onclick="login();" class="btn" type="button" name="button">Login</button>
						</div>
						
					</div>
				</div>

			</div>
		</div>
<!-- partial -->
  
 

</body>
</html>''')