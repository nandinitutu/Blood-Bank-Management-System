import cgi, cgitb, config, check_cookie
cgitb.enable()
frm = cgi.FieldStorage()
print('''Content-type:text/html\r\n\r\n

<!DOCTYPE html>
<html lang="en">
    <meta http-equiv="content-type" content="text/html;charset=utf-8" /><!-- /Added by HTTrack -->
<head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>Search Blood</title>

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
                        <a href="loginpage.py"><i class="fa fa-sign-out fa-fw"></i> Logout</a>
                    </li>
                </ul>
            </nav>
                <div class="container-fluid">
                    <br><br><br><br>
                    <div class="row">
                        <div class="col-sm-12">
                            <div class="hero-widget well well-sm">
                                <img src="img/avlchck.png" width="1500px" height="450px"> 
                            </div>
                        </div>
                        <form action="upload.py" name="frm" method="post" enctype="multipart/form-data">
                            <div class="col-lg-12">
                                <div class="panel panel-info">
                                    <div class="panel-heading">
                                        <span style="color: black; font-size: 25px;"> Submit Your Prescription.....And <span style="color: rgb(0, 141, 19);"> Verify</span> Now.....</span><input type="file" name="file" required><br><input type="text" name="bld" placeholder="Enter Blood Group" required>
                                    </div>
                                    <div class="panel-footer">
                                        <input type="Submit" name="Submit" class="btn btn-primary">
                                    </div>
                                </div>
                            </div>
                        </form>''')
if frm.getvalue('msg'):
    print(frm.getvalue('msg'))
print('''
                        <div class="panel panel-default">
                            <div class="panel-body">         
                                <p>
                                    <a href="patientpost.py"><button type="button" class="btn btn-outline btn-primary btn-lg btn-block">Let's Post It !!</button><a/>
                                </p>
                            </div>
                        </div>
                        <div>''')
src="SELECT * FROM srcbld WHERE status=1"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<iframe src="https://www.google.com/maps/d/embed?mid=179E6svgkmMm-562H789UHczgoc7yl1om" width="1900" height="480" frameborder="0"></iframe>''')
else:
    print('You are not verified')
print('''                       </div>
                    </div>
                </div>  
        </div>   
    </body>
</html>''')