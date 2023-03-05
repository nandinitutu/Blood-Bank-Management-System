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
                                <img src="img/fdbck.jpg" width="1400px" height="650px"> 
                            </div>
                        </div>
                        <div class="container-fluid">
                            <div class="row">
                                <div class="col-lg-12">
                                    <h1 id="request" class="page-header" style="color: rgb(180, 0, 0); border-bottom-color: rgb(151, 0, 0);">All Feedbacks...........</h1>
                                </div>
                            </div>
                            <div class="row">
                                <div class="col-lg-12">
                                    <div class="panel panel-default">
                                        <div class="panel-heading">
                                            <div style="color: rgb(0, 0, 0);">Here are all User Details...
                                                <input style="padding: 6px; margin-top: 8px; font-size: 17px; border: none; float: none; display: block; text-align: left; width: 60%; margin: 0; padding: 14px; border: 1px solid rgb(136, 0, 0);" type="text" placeholder="Search Blood Group..." name="search">
                                            </div>
                                        </div>
                                        <div class="panel-body">
                                            <div class="table-responsive">''')
try:
    src = "SELECT * FROM fdbk"
    cursor = config.db8.cursor()
    cursor.execute(src)
    rs = cursor.fetchall()
except Exception as e:
    print(e)
if rs:
    print('''                                  <table class="table table-striped table-bordered table-hover" id="dataTables-example">
                                                    <thead>
                                                        <tr>
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">Name</th>                                                            
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">Email</th>                                                            
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">Any suggestion</th>
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">How can we improve</th> 
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">If you were describing this web page to a friend, would you say this web page is</th> 
                                                            <th style="text-align: center; color: rgb(209, 0, 52);">Are there any feature which you would like to see add or expanded on the future?</th>                                                            
                                                        </tr>
                                                    </thead>
                                                    <tbody>''')
    for rec in rs:
        print('''<tr>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>
            <td>{}</td>            
            </tr>'''.format(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6]))
    print('''                                       </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
        </div>   
    </body>
</html>''')