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

    <title>Hospital Profile</title>

    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/metisMenu.min.css" rel="stylesheet">
    <link href="css/startmin.css" rel="stylesheet">
    <link href="css/font-awesome.min.css" rel="stylesheet" type="text/css">
<style>

.inner {
  padding: 20px;
  background: #fff;
  max-width: 900px;
  margin: auto;
  display: flex; 
  border-radius: 20px;
  border: 2px solid rgb(236, 63, 63);
}
  .inner .image-holder {
    width: 50%;
   
    }
  .inner form {
    width: 50%;
    padding-top: 36px;
    padding-left: 45px;
    padding-right: 45px; }
  .inner h3 {
    text-transform: uppercase;
    font-size: 25px;
    font-family: "Poppins-SemiBold";
    text-align: center;
    margin-bottom: 28px; }

.form-group {
  display: flex; }
  .form-group input {
    width: 50%; }
    .form-group input:first-child {
      margin-right: 25px; }

.form-wrapper {
  position: relative; }
  .form-wrapper i {
    position: absolute;
    bottom: 9px;
    right: 0; }

.form-control {
  border: 1px solid rgb(236, 63, 63);
  border-top: none;
  border-right: none;
  border-left: none;
  display: block;
  width: 100%;
  height: 30px;
  padding: 0;
  margin-bottom: 25px; }
  .form-control::-webkit-input-placeholder {
    font-size: 13px;
    color: #6f7a85;
    font-family: "Poppins-Regular"; 
     font-size: medium;}
  .form-control::-moz-placeholder {
    font-size: 13px;
    color: #6f7a85;
    font-family: "Poppins-Regular"; }
  .form-control:-ms-input-placeholder {
    font-size: 13px;
    color: #6f7a85;
    font-family: "Poppins-Regular"; }
  .form-control:-moz-placeholder {
    font-size: 13px;
    color: #6f7a85;
    font-family: "Poppins-Regular"; }

select {
  -moz-appearance: none;
  -webkit-appearance: none;
  cursor: pointer;
  padding-left: 20px; }
  select option[value=""][disabled] {
    display: none; }

.button {
  border: none;
  width: 160px;
  height: 51px;
  margin: auto;
  margin-top: 40px;
  border-radius: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  background: #333;
  font-size: 15px;
  color: #fff;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s; }
  
  .button i {
    margin-right: 20px;
    
    -webkit-transform: translateZ(0);
    transform: translateZ(0); }
  .button:hover i, button:focus i, button:active i {
    -webkit-animation-name: hvr-icon-wobble-horizontal;
    animation-name: hvr-icon-wobble-horizontal;
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-timing-function: ease-in-out;
    animation-timing-function: ease-in-out;
    -webkit-animation-iteration-count: 1;
    animation-iteration-count: 1; }
    

@-webkit-keyframes hvr-icon-wobble-horizontal {
  16.65% {
    -webkit-transform: translateX(6px);
    transform: translateX(6px); }
  33.3% {
    -webkit-transform: translateX(-5px);
    transform: translateX(-5px); }
  49.95% {
    -webkit-transform: translateX(4px);
    transform: translateX(4px); }
  66.6% {
    -webkit-transform: translateX(-2px);
    transform: translateX(-2px); }
  83.25% {
    -webkit-transform: translateX(1px);
    transform: translateX(1px); }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0); } }
@keyframes hvr-icon-wobble-horizontal {
  16.65% {
    -webkit-transform: translateX(6px);
    transform: translateX(6px); }
  33.3% {
    -webkit-transform: translateX(-5px);
    transform: translateX(-5px); }
  49.95% {
    -webkit-transform: translateX(4px);
    transform: translateX(4px); }
  66.6% {
    -webkit-transform: translateX(-2px);
    transform: translateX(-2px); }
  83.25% {
    -webkit-transform: translateX(1px);
    transform: translateX(1px); }
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0); } }
@media (max-width: 1199px) {
  .wrapper {
    background-position: right center; } }
@media (max-width: 991px) {
  .inner form {
    padding-top: 10px;
    padding-left: 30px;
    padding-right: 30px; } }
@media (max-width: 767px) {
  .inner {
    display: block; }
    .inner .image-holder {
      width: 100%; }
    .inner form {
      width: 100%;
      padding: 40px 0 30px; }

  button {
    margin-top: 60px; } }
   

/*# sourceMappingURL=style.css.map */

	</style>
<style>
        .filterDiv {
          float: left;
          width: 370px;
          line-height: 100px;
          text-align: center;
          margin: 2px;
          position: relative; 
        }
body{
    margin: 0;
    padding: 0;
}
.box{
    position: absolute;
    top: 15%;
    left: 87%;
    transform: translate(-50%,-50%);
}
input{
    width: 28px;
    height: 40px;
    border: none;
    outline: none;
    background: none;
}
.button111{
    height: 30px;
    width: 50px;    
}
.button222{
    height: 30px;
    width: 50px;
}
i{
    position: relative;
    bottom: 35px;    
}
</style>
<style>
    .btn-group button {
      border: 1px solid green;
      color: white;
      padding: 5px 15px;
      cursor: pointer;
      float: left;
      width: 33%;
    }
</style>
</head>
    <body style="font-family: loud;">
        <img src="img/img2.jpg" alt="" width="1900" height="320">
        <div id="wrapper" >
            <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
                <div class="navbar-header">
                    <a class="navbar-brand" >Life Share</a>
                </div>
                <ul class="nav navbar-nav navbar-left navbar-top-links">
                    <li><a href="index.py"><i class="fa fa-home fa-fw"></i> Website</a></li>
                </ul>
                <ul class="nav navbar-right navbar-top-links">
                    <li><a href="hospitallogin.py"><i class="fa fa-clock-o fa-fw"></i> Logout</a></li>
                </ul>
                <div class="navbar-default sidebar" role="navigation">
                    <div class="sidebar-nav navbar-collapse"><br>
                        <ul class="nav" id="side-menu">
                            <img src="img/pic.jpg" alt="" width="250" height="152">
                            <li>
                                <a href="#profile" class="active"><i class="fa fa-dashboard fa-fw"></i>Profile</a>
                            </li><br><br><br>

                            <li>
                                <a href="#record"><i class="fa fa-clock-o fa-fw"></i>Blood Records</a>
                            </li><br><br><br>

                            <li>
                                <a href="#donor"><i class="fa fa-user fa-fw"></i>Donor Details</a>
                            </li><br><br><br>
                            <li>
                                <a href="#request"><i class="fa fa-envelope fa-fw"></i>All Patients</a>
                            </li><br><br><br>                          
                        </ul>
                    </div>
                </div>
            </nav>''')
src="SELECT * FROM request WHERE hid=1"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<div id="profile">                                
                <div id="page-wrapper" > 
                <div class="row">
                            <div class="col-lg-12">
                                <h1  class="page-header" style="color: rgb(180, 0, 0); border-bottom-color: rgb(151, 0, 0);">Hospital Profile</h1>
                            </div>
                        </div>               
                    <div class="inner">
				<div class="image-holder">
					<img src="img/gg.gif" alt="" style="max-width: 100%; height: 690px;">
				</div>''')
    for rec in rs:
        print('''<form name="frm" method="post" action="abcd.py">
					<h3>Request Form</h3>					
					<div class="form-wrapper">
						<input type="text" placeholder="Hospital Name" value="{}" name="hname" class="form-control" required>
						<i class="fas fa-hospital"></i>
					</div>
					<div class="form-wrapper">
						<input type="text" placeholder="Hospital Address" value="{}" name="haddr" class="form-control" required>
						<i class="fas fa-map-marker-alt"></i>
					</div>
					<div class="form-wrapper">
						<input type="email" placeholder="Email Address" value="{}" name="hemail" class="form-control" required>
						<i class="fa fa-envelope"> </i>
					</div>
          <div class="form-wrapper">
						<input type="password" placeholder="Passward" value="{}" name="hpass" class="form-control" required>
						<i class="fa fa-key"> </i>
					</div>
					
					<div class="form-group">
						<input type="number" placeholder="Contact Number" name="cont" class="form-control" value="{}" required>	
						<input type="number" placeholder="Pin Code" name="pin" class="form-control" value="{}" required>
						
					</div>'''.format(rec[1],rec[2],rec[3],rec[4],rec[5],rec[6]))
print('''
					<div class="form-wrapper">
						<select name="hcity" id="" class="form-control" required>
							<option value="{}" selected>{}</option>'''.format(rec[7],rec[7]))
city=["Kolkata","Siliguri","Medinipur","Bakura","Nodia","Darjeeling","Bardwan","Kharagpur","Haldia","Asansol","Durgapur"]
for i in city:
    print('<option value="{}">{}</option>'.format(i, i))
print(''' 	</select>
						<i class="fa fa-caret-down" style="font-size: 17px"></i>
					</div>
					<div class="form-wrapper">
						<input type="text" placeholder="Website Link" value="{}" name="web" class="form-control" required>
						<i class="fa fa-link"></i>
					</div>'''.format(rec[8]))
print('''
          <div class="form-wrapper">    
						<select name="sques" id="" class="form-control" required>
							<option value="{}"Selected>{}</option>'''.format(rec[9],rec[9]))
secu=["What is your oldest cousins first name?","What is your favourite actor?","What is your favourite food?","What is the title and artist of your favorite song?","What is your work address?","In what city or town did your mother and father meet?","What is your cars license plate number?","What was your first car?","What is the middle name of your oldest child?","what was your first pets name?","In what city or town was your first job?","What was your childhood nickname?","What is your favourite cricket team?"]
for i in secu:
    print('<option value="{}">{}</option>'.format(i, i))
print(''' 	</select>
						<i class="fa fa-caret-down" style="font-size: 17px"></i>
					</div>
          <div class="form-wrapper">
						<input type="text" name="sans" value="{}" placeholder="Security Answer" class="form-control" required>'''.format(rec[10]))
print('''
						<i class="fa fa-reply"></i>
					</div>
          <div class="button"><input type="submit" name="ok" value="Update" style="border: none; width: 80px; height: 51px; margin: right; margin-top: 0; border-radius: 20px;  cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 0; background: #333; font-size: 20px; color: #fff; vertical-align: middle; -webkit-transform: perspective(1px) translateZ(0); transform: perspective(1px) translateZ(0); -webkit-transition-duration: 0.3s; transition-duration: 0.3s;"></div>
				</form></div></div>
                    
                </div>
            </div>''')
src="SELECT * FROM bldstck WHERE hid=1"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<div id="record">                                
                <div id="page-wrapper" >                
                    <div>
                        <h1 class="page-header" style="color: rgb(180, 0, 0); border-bottom-color: rgb(151, 0, 0);">Blood Records</h1>
                    <div class="filterDiv">
                        <img src="img/ap.png" alt="">''')
    for rec in rs:
        print('''       <div class="box">
                            <input type="int" value="{}" readonly>
                        </div> <br> <div class="abc">
                        <a href="updmns.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a></div>
                    </div>'''.format(rec[2],rec[2],rec[2]))
        print('''
                    <div class="filterDiv">
                        <img src="img/bp.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns1.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls1.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>'''.format(rec[4],rec[4],rec[4]))
        print('''
                    <div class="filterDiv">
                        <img src="img/abp.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns2.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls2.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>'''.format(rec[6],rec[6],rec[6]))
        print('''
                    <div class="filterDiv">
                        <img src="img/op.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        </div><br>
                        <a href="updmns3.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls3.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div><br>'''.format(rec[8],rec[8],rec[8]))
        print('''
                    <div class="filterDiv">
                        <img src="img/am.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns4.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls4.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>'''.format(rec[3],rec[3],rec[3]))
        print('''
                    <div class="filterDiv">
                        <img src="img/bm.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns5.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls5.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>'''.format(rec[5],rec[5],rec[5]))
        print('''
                    <div class="filterDiv">
                        <img src="img/abm.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns6.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls6.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>'''.format(rec[7],rec[7],rec[7]))
        print('''
                    <div class="filterDiv">
                        <img src="img/om.png" alt="">
                        <div class="box">
                            <input type="text" value="{}" readonly>
                        
                        </div><br>
                        <a href="updmns7.py?pid={}"><button type="button" class="button111" data-quantity="minus" data-field="quantity">
                            <i class="fa fa-minus" aria-hidden="true"></i>
                        </button></a>
                        <a href="updpls7.py?pid={}"><button type="button" class="button222" data-quantity="plus" data-field="quantity">
                            <i class="fa fa-plus" aria-hidden="true"></i>
                        </button></a>
                    </div>
                    </div>'''.format(rec[9],rec[9],rec[9]))
print('''
                    
                </div>
            </div>
            <br>
            <div id="donor">
                <div id="page-wrapper">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-lg-12">
                                <h1 id="donor" class="page-header" style="color: rgb(180, 0, 0); border-bottom-color: rgb(151, 0, 0);">Donor Details</h1>
                            </div>
                        </div>''')
src="SELECT p.status,u.name,u.email,u.age,u.gen,u.blood,u.city,u.mob FROM donorbld p INNER JOIN registration u ON p.pid=u.pid"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<div class="row">
                                        <div class="col-lg-12">
                                            <div class="panel panel-default">
                                                <div class="panel-heading">
                                                    <div style="color: rgb(0, 0, 0);">Here are all Requests...
                                                        <input style="padding: 6px; margin-top: 8px; font-size: 17px; border: none; float: none; display: block; text-align: left; width: 60%; margin: 0; padding: 14px; border: 1px solid rgb(136, 0, 0);" type="text" placeholder="Search Blood Group..." name="search">
                                                    </div>
                                                </div>
                                                <div class="panel-body">
                                                    <div class="table-responsive">
                                                        <table class="table table-striped table-bordered table-hover" id="dataTables-example">
                                                            <thead>
                                                                <tr>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Requester</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Email</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Age </th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Gender</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Blood Group</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">City</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Contact</th>
                                                                </tr>
                                                            </thead>
                                                            <tbody>''')
    for rec in rs:
        print('''<tr class="odd gradeX">
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">{}</td>
                                                                    <td style="text-align: center;">
                                                                        <div class="btn-group">
                                                                            <a href="tel:+91{}"><button style="width:100%; background-color: rgb(0, 216, 36); color:#000;"><b>Contact</b></button></a>
                                                                      </div>
                                                                    </td>
                                                                </tr>'''.format(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]))
else:
    print('You are not verified')
print('''     
                                                </tbody>
                                            </table>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <br>
            <div id="request">
                <div id="page-wrapper">
                    <div class="container-fluid">
                        <div class="row">
                            <div class="col-lg-12">
                                <h1 id="request" class="page-header" style="color: rgb(180, 0, 0); border-bottom-color: rgb(151, 0, 0);">All Patients</h1>
                            </div>
                        </div>''')
src="SELECT p.status,u.name,u.email,u.age,u.gen,u.blood,u.city,u.mob FROM srcbld p INNER JOIN registration u ON p.pid=u.pid"
cursor=config.db8.cursor()
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    print('''<div class="row">
                                        <div class="col-lg-12">
                                            <div class="panel panel-default">
                                                <div class="panel-heading">
                                                    <div style="color: rgb(0, 0, 0);">Here are all Requests...
                                                        <input style="padding: 6px; margin-top: 8px; font-size: 17px; border: none; float: none; display: block; text-align: left; width: 60%; margin: 0; padding: 14px; border: 1px solid rgb(136, 0, 0);" type="text" placeholder="Search Blood Group..." name="search">
                                                    </div>
                                                </div>
                                                <div class="panel-body">
                                                    <div class="table-responsive">
                                                        <table class="table table-striped table-bordered table-hover" id="dataTables-example">
                                                            <thead>
                                                                <tr>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Requester</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Email</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Age </th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Gender</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Blood Group</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">City</th>
                                                                    <th style="text-align: center; color: rgb(209, 0, 52);">Accept/ Cancel</th>
                                                                </tr>
                                                            </thead>
                                                            <tbody>''')
    for rec in rs:
        print('''<tr class="odd gradeX">
                                                                    <td>{}</td>
                                                                    <td>{}</td>
                                                                    <td>{}</td>
                                                                    <td>{}</td>
                                                                    <td>{}</td>
                                                                    <td>{}</td>
                                                                    <td style="text-align: center;">
                                                                        <div class="btn-group">
                                                                            <a href="tel:+{}"><button style="width: 100%; background-color: rgb(0, 216, 36); color:#000;"><b>Contact</b></button></a>
                                                                      </div>
                                                                    </td>
                                                                </tr>'''.format(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7]))
else:
    print('You are not verified')
print('''                                       
                                                  </tbody>
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