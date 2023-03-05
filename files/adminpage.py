import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html lang="en">
    <!-- Added by HTTrack --><meta http-equiv="content-type" content="text/html;charset=utf-8" /><!-- /Added by HTTrack -->
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>admin</title>

        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/metisMenu.min.css" rel="stylesheet">
        <link href="css/startmin.css" rel="stylesheet">
        <link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div id="wrapper">
            <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="navbar-header">
                    <a class="navbar-brand" >Life Share</a>
                </div>
                <ul class="nav navbar-nav navbar-left navbar-top-links">
                    <li><a href="index.py"><i class="fa fa-home fa-fw"></i> Website</a></li>
                </ul>
                <ul class="nav navbar-right navbar-top-links">                    
                    <li class="dropdown">
                        <a href="adminlogin.py"><i class="fa fa-sign-out fa-fw"></i> Logout</a>
                    </li>
                </ul>
            </nav>
                <div class="container-fluid">
                    <br><br><br><br>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="hero-widget well well-sm">
                                <img src="img/admin1.jpg" width="1400px" height="450px"> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminrequest.py"><i class="fa fa-hospital-o" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> Requested Hospitals </button></b>
                                </a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminPatients.py"><i class="fa fa-bed" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> Patients Verify </button></b>
                                </a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminPost.py"><i class="fa fa-pencil-square" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> Post Verify </button></b>
                                </a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminalluser.py"><i class="fa fa-user-o" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> All Users </button></b>
                                </a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminmessages.py"><i class="fa fa-envelope" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> All Messages </button></b>
                                </a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="adminfeedback.py"><i class="fa fa-comments-o" aria-hidden="true" style="color: rgb(255, 0, 0); font-size: 210px; width: 50%;"></i>
                                    <p></p><b><button style="background:none; width: 370px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(0, 0, 0); font-size:30px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"> All Feedback </button></b>
                                </a> 
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
        </div>   
    </body>
</html>''')
