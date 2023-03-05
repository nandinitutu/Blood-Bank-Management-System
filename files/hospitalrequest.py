import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Hospital Request</title>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
		<script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>
		<link rel="stylesheet" href="css/style.css">
	</head>
	<style>
		@font-face {
  font-family: "Poppins-Regular";
  src: url("../fonts/poppins/Poppins-Regular.ttf"); }
@font-face {
  font-family: "Poppins-SemiBold";
  src: url("../fonts/poppins/Poppins-SemiBold.ttf"); }
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box; }

body {
  font-family: "Poppins-Regular";
  color: rgb(236, 63, 63);
  font-size: 13px;
  margin: 0; }

input, textarea, select, button {
  font-family: "Poppins-Regular";
  color: #6f7a85;
  font-size: 13px;
font-size: medium; }

p, h1, h2, h3, h4, h5, h6, ul {
  margin: 0; }

img {
  max-width: 100%;
  height: 650px;
  }

ul {
  padding-left: 0;
  margin-bottom: 0; }

a:hover {
  text-decoration: none; }

:focus {
  outline: none; }

.wrapper {
  min-height: 100vh;
  background-size: 1000% 1000%;
  display: flex;
  align-items: center; 
  
 }

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
    ul {
   
      list-style-type: none;
      margin-top: 0px;
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

	<body style="background-image: url(img/fff.jpg) ; background-repeat: no-repeat; background-size: 100% 100%;">
		<ul>
			<li><a class="active" href="hospitallogin.py"><i class="fas fa-home"></i>  Back To Login</a></li>
			
		</ul>
		
		<div class="wrapper" >
			
			<div class="inner">
				<div class="image-holder">
					<img src="img/gg.gif" alt="">
				</div>
				<form name="frm" method="post">
					<h3>Request Form</h3>
					
					<div class="form-wrapper">
						<input type="text" placeholder="Hospital Name" name="hname" class="form-control" required>
						<i class="fas fa-hospital"></i>
					</div>
					<div class="form-wrapper">
						<input type="text" placeholder="Hospital Address" name="haddr" class="form-control" required>
						<i class="fas fa-map-marker-alt"></i>
					</div>
					<div class="form-wrapper">
						<input type="email" placeholder="Email Address" name="hemail" class="form-control" required>
						<i class="fa fa-envelope"> </i>
					</div>
          <div class="form-wrapper">
						<input type="password" placeholder="Passward" name="hpass" class="form-control" required>
						<i class="fa fa-key"> </i>
					</div>
					
					<div class="form-group">
						<input type="number" placeholder="Contact Number" name="cont" class="form-control" required>	
						<input type="number" placeholder="Pin Code" name="pin" class="form-control" required>
						
					</div>
					<div class="form-wrapper">
						<select name="hcity" id="" class="form-control" required>
							<option value="Select">City</option>''')
city=["Kolkata","Siliguri","Medinipur","Bakura","Nodia","Darjeeling","Bardwan","Kharagpur","Haldia","Asansol","Durgapur"]
for i in city:
    print('<option value="{}">{}</option>'.format(i, i))
print(''' 	</select>
						<i class="fas fa-caret-down" style="font-size: 17px"></i>
					</div>
					<div class="form-wrapper">
						<input type="text" placeholder="Website Link" name="web" class="form-control" required>
						<i class="fas fa-link"></i>
					</div>
          <div class="form-wrapper">
						<select name="sques" id="" class="form-control" required>
							<option value="Select">Security Question</option>''')
secu=["What is your oldest cousins first name?","What is your favourite actor?","What is your favourite food?","What is the title and artist of your favorite song?","What is your work address?","In what city or town did your mother and father meet?","What is your cars license plate number?","What was your first car?","What is the middle name of your oldest child?","what was your first pets name?","In what city or town was your first job?","What was your childhood nickname?","What is your favourite cricket team?"]
for i in secu:
    print('<option value="{}">{}</option>'.format(i, i))
print(''' 	</select>
						<i class="fas fa-caret-down" style="font-size: 17px"></i>
					</div>
          <div class="form-wrapper">
						<input type="text" name="sans" placeholder="Security Answer" class="form-control" required>
						<i class="fas fa-reply"></i>
					</div>
          <div class="button"><input type="submit" name="ok" value="Request" style="border: none; width: 100px; height: 51px; margin: right; margin-top: 0; border-radius: 20px;  cursor: pointer; display: flex; align-items: center; justify-content: center; padding: 0; background: #333; font-size: 20px; color: #fff; vertical-align: middle; -webkit-transform: perspective(1px) translateZ(0); transform: perspective(1px) translateZ(0); -webkit-transition-duration: 0.3s; transition-duration: 0.3s;"><i class="fas fa-arrow-right"></i></div>
				</form></div></div>''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    hname=frm.getvalue('hname')
    haddr=frm.getvalue('haddr')
    hemail=frm.getvalue('hemail')
    hpass=frm.getvalue('hpass')
    cont=frm.getvalue('cont')    
    pin=frm.getvalue('pin')
    hcity=frm.getvalue('hcity')
    web=frm.getvalue('web')
    sques = frm.getvalue('sques')
    sans = frm.getvalue('sans')
    sub=0
    try:
        cursor = config.db8.cursor()
        src = "SELECT hemail FROM request WHERE hemail='{}'".format(hemail)
        cursor.execute(src)
        rec = cursor.fetchall()
        if rec:
            print('''<h1 style="font-family: loud; font-size: 50px; text-align: center; color: red; margin-bottom: 2px;">You are already registered</h1>''')
        else:
            sql = "INSERT INTO request(hname, haddr, hemail, hpass, cont, pin, hcity, web,sques, sans, status) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}',0)".format(hname, haddr, hemail, hpass, cont, pin, hcity, web, sques, sans, sub)
            cursor.execute(sql)
            config.db8.commit()
            config.db8.close()
            print('''<h1 style="font-family: loud; font-size: 50px; text-align: center; color: rgb(0, 128, 11);">Registration Successfull</h1>''')
    except Exception as e:
        print(e)    
print('''        		
	</body>
</html>''')