import cgi, cgitb, config
cgitb.enable()
frm = cgi.FieldStorage()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Paitent Login</title>
    <script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>
</head>
<style>
    
    .register-photo {
    background: #fafafa;
    padding: 110px 0px;
    height: 790px;
    background-image: url(https://image.freepik.com/free-vector/blood-donation-pattern_17735-76.jpg);
    background-size: 60% 60%

}
.register-photo .image-holder {
    display: table-cell;
    width: auto;
    background-size: cover;
    background-image: url("img/bb.jpg");
    background-repeat: no-repeat;
}
.register-photo .form-container {
    display: table;
    max-width: 945px;
    width:900%;
    margin: 0 auto;
    box-shadow: 1px 1px 5px rgba(235, 103, 103, 0.658);
   
}
.register-photo form {
    display: table-cell;
    width: 400px;
    background-color: #ffffff;
    padding: 40px 60px;
    color: hsl(0, 80%, 54%);
    margin-top: 100px;
    
    
}
.register-photo form h1 {
    font-size: 24px;
    line-height: 1.5;
    margin-bottom: 30px
}

.register-photo form .btn {
    background: rgb(2, 131, 2);
    border: none;
    font-size: medium;
    border-radius: 8px;
    height:  41px;
    width: 200px;
    box-shadow: none;
    margin-top: 35px;
    margin-left: 90px;
    text-shadow: none;
    outline: none !important
    
}
.register-photo form .btn:hover,
.register-photo form .btn:hover
 {
    background: rgb(106, 218, 156)
 }
.register-photo form .btn :active {
    transform: translateY(1px)
}
.register-photo form .already {
    display: block;
    text-align: center;
    font-size: 15px;
    color: #6f7a85;
    opacity: 0.9;
    text-decoration: none;
    font-size: medium;
    margin-right: 40px;
    


}
.register-photo form .form-control {
    background: transparent;
    border: none;
    border-bottom: 1px solid hsl(0, 80%, 54%);
    border-radius: 0;
    box-shadow: none;
    outline: none;
    color: initial;
    text-indent: 0px;
    width: 300px;
    height: 50px;
    font-size: large;
   
  }
  ul {
   
  list-style-type: none;
  margin-top: -8px;
  padding: 0;
  overflow: hidden;
  background-color: hsl(0, 54%, 47%);
}

li {
  float: right;
}

li a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

li a:hover {
  background-color: rgb(230, 82, 82);
}
.register-photo form .ready {
  list-style-type: none;
  margin: 0;
  padding: 0;
  color: #6f7a85;
 
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
<script>
    function myFunction() {
      var x = document.getElementById("myInput");
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
<body style="font-family: loud;">
    <ul>
        <li><a class="active" href="index.py"><i class="fas fa-home"></i>  Back To Home</a></li>
        
    </ul>
    <div class="register-photo"><br><br><br><br><br><br><br><br>
        <div class="form-container">
            <div class="image-holder"></div>
            <form name="frm" method="post" action="login_code.py" role="form">
                <h1 class="text-center" style="text-transform: uppercase;"> Paitent/ Donor Login</h1>
              
                <div class="form-group"><i class="far fa-envelope" style="color:#6f7a85 ;"></i> <input class="form-control" type="email" name="email" placeholder="Email...." required></div>
                <div class="form-group"><i class="fas fa-key" style="color:#6f7a85 ;"></i> <input class="form-control" type="password" name="password" placeholder="Password...." id="myInput" required></div>''')
if frm.getvalue('msg'):
    print(frm.getvalue('msg'))
print('''
                   <i class="far fa-eye" id="show"  onclick="myFunction()" style="float: right;cursor: pointer;margin: 4px 78px; font: 18px;position: relative; margin-top:-30px"></i>
                   <i class="far fa-eye-slash" id="hide" onclick="myFunction()"style="float: right;cursor: pointer;margin: 4px 78px; font: 18px;position: relative; margin-top:-30px ; "></i>
                <div class="form-group"><button class="btn btn-success btn-block" type="submit">LOGIN</button></div><br>
                <a class="already" href="forgotpsw.py">forgot your password?</a><br><a style="color:#6f7a85;  margin-left: 80px;">Don't have any accout?</a><a class="ready" href="paitentregistretion.py"> Sing Up</a>
            </form>
        </div>
    </div>
</body>
</html>''')