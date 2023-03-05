import cgi, cgitb, config
cgitb.enable()
frm = cgi.FieldStorage()
print('''Content-type:text/html\r\n\r\n
<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Hospital Login Page | </title>
    <link rel="shortcut icon" href="assets/images/fav.png" type="image/x-icon">
    <link href="https://fonts.googleapis.com/css?family=Josefin+Sans:300,400,600,700" rel="stylesheet">
    <link rel="shortcut icon" href="assets/images/fav.jpg">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="assets/css/style.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css">
    <script src="https://kit.fontawesome.com/98a6403fa6.js" crossorigin="anonymous"></script>
    <script>
        function myFunction() {
            var x = document.getElementById("myInput");
            if (x.type === "password") {
            x.type = "text";
            } else {
            x.type = "password";
            }
        }
    </script>
</head>

<body>
<ul style=" list-style-type: none;margin-top: 1px; padding: 0;overflow: hidden; background-color: skyblue;">
      <li style="float: right;"><a class="active" href="index.py" style="display: block;color: Black;text-align: center;padding: 14px 16px;text-decoration: none;"><i class="fas fa-home"></i>  Back To Home</a></li>
  </ul>
    <div class="container-fluid">
        <div class="container">
            <div class="col-xl-10 col-lg-11 login-container">
                <div class="row">
                    <div class="col-lg-7 img-box">
                        <img src="assets/images/depositphotos_82310178-smiling-nurse-in-hospital.jpg" alt="">
                    </div>
                    <div class="col-lg-5 no-padding">
                        <div class="login-box">
                            <h5>Welcome </h5>

                            <form name="frm" method="post" action="hoslogin_code.py" role="form">
                                <p style="color: blue;">Hospital Email Id</p> 
                                <input type="text" name="email" autofocus="" autocapitalize="none" autocomplete="username" required="" id="id_username"><br><br>
                                <p style="color: blue;">Password</p> 
                                <input type="password" name="password" value="" id="myInput" required>
                                <input type="checkbox" onclick="myFunction()">Show
                                <br>''')
if frm.getvalue('msg'):
    print(frm.getvalue('msg'))
print('''
                                <div >
                                    <br><p><a href="frgtps.py" style="color: rgb(7, 7, 7);">Forget Password?</a></p>
                                 </div>
     
                                  <div class="login-row btnroo row no-margin">
                                    <input type="submit" style="background: rgb(82, 159, 230);" name="ok" class="btn btn-primary btn-sm" value="Sign In">
                                    
                                 </div>
                                 
                            </form>
                             <div class="login-row donroo row no-margin">
                                     <p style="color: rgb(255, 7, 7); font-size: larger;">Dont have an Account ? <a href="hospitalrequest.py" </a> <button class="btn btn-primary btn-sm" id="signUp">Sign Up</button></p>
                                 </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>


</body>

</html>

''')