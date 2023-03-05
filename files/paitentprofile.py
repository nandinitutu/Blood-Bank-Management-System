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

        <title>Patient Profile</title>

        <link href="css/bootstrap.min.css" rel="stylesheet">
        <link href="css/metisMenu.min.css" rel="stylesheet">
        <link href="css/startmin.css" rel="stylesheet">
        <link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">
    </head>
    <body background="">
        <div id="wrapper">
            <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="navbar-header">
                    <a class="navbar-brand" href="index.html">Life Share</a>
                </div>
                <ul class="nav navbar-nav navbar-left navbar-top-links">
                    <li><a href="index.py"><i class="fa fa-home fa-fw"></i> Website</a></li>
                </ul>
                <ul class="nav navbar-right navbar-top-links">                    
                    <li class="dropdown">
                        <a href="paitentlogin.py"><i class="fa fa-sign-out fa-fw"></i> Logout</a>
                    </li>
                </ul>
            </nav>
                <div class="container-fluid">
                    <br><br><br><br>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="hero-widget well well-sm">
                                <img src="img/pin.jpeg" width="1500px" height="400px">
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="paitentdonor.py"><img src="img/donor.jpeg" width="400px" height="400px"></a> 
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="paitentsearchblood.py"><img src="img/srchbld.jpeg" width="400px" height="400px"></a>
                            </div>
                        </div>
                        <div class="col-sm-4">
                            <div class="hero-widget well well-sm">
                                <a href="modofyprofile.py"><img src="img/modify.jpeg" width="400px" height="400px"></a>
                            </div>
                        </div>
                        
                    </div>
                    
                </div>
        </div>   
    </body>
</html>''')