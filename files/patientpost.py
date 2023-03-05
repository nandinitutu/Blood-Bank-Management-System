import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>
	<head>
		<title>Patient Post</title>
		<link rel="stylesheet" type="text/css" href="login.css">
    <style>
      @import "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css";
header
{
	height: 130px;
	width: 1900px;
	background-color: black;
	padding: 10px;
}
h1{
	text-align:center;
	font-size:60px;
}
body {
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: 100% 100%;
  font-family: loud;
}
.form{
	width: 700px;
	height: 880px;
	position: absolute;
	top: 50%;
	left: 50%;
	padding:30px;
	border: 2px solid white;
	transform: translate(-50%, -50%);
	border-radius: 20px;
	text-align: center;
}
.textbox{
	width: 660px;
	overflow: hidden;
	font-size:10px;
	padding: 8px;
	margin: 8px;
	text-align: left;
	
}

.textbox textarea:focus{
	width:660px;
  text-align: center;
	font-size:20px;
}

.login input[type="submit"]{
	background: none;
	width: 190px;
	padding: 10px;
	border-radius: 20px;
	border: 2px solid #2ecc71;
	color:rgb(255, 255, 255);
	font-size:20px;
	transition: 0.25s;
	text-align: center;
	outline: none;
	margin:20px auto;
	cursor: pointer;
}
.login input[type= "submit"]:hover{
	background:  #2ecc71;
}

.black {
        width: 120px;
        height: 30px;
        border: 1px solid black;
        font-size: 18px;
        color: black;
        background-color: #eee;
        border-radius: 5px;
        box-shadow: 4px 4px #ccc;
      }

.p1{
	color: aqua;
	position:static;
	padding-left: 25px;
	font-size: 22px;
}
.p2{
	color: rgb(39, 238, 129);
	position:static;
	padding-left: 45px;
	font-size: 22px;
}
.p3{
	color: rgb(246, 245, 255);
	position:static;
	padding-left: 35px;
	font-size: 22px;
}
    </style>
	</head>
	<script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.6.9/angular.min.js"></script>

	<body background="img/post.gif">
		<div style="text-align: right;">
			<button style="background:rgb(255, 1, 1); width: 170px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(255, 255, 255); font-size:20px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"><a style="color:rgb(255, 255, 255);" href="patientlogin.py"> <i class="fa fa-sign-out" aria-hidden="true"> Log Out</i></a></button>
			<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
			<button style="background:none; width: 170px; padding: 3px; border-radius: 12px; border: 2px solid #e20f00; color:rgb(255, 255, 255); font-size:20px; transition: 0.25s; text-align: center; outline: none; margin:20px auto; cursor: pointer;"><a style="color:rgb(255, 255, 255);" href="paitentsearchblood.py"> <i class="fa fa-backward" aria-hidden="true"> Back To Privious Page</i></a></button>
		</div>
		<div class="form">
			<form name="frm" method="post">
				<div class="textbox">
					<div style="text-align: center;">
						<i class="fa fa-universal-access" aria-hidden="true" style="color: rgb(214, 255, 248); font-size: 210px; width: 50%;"></i>
						<p style="font-size: 30px; color: rgb(0, 81, 255); ">----LET'S POST IT----</p>
					</div>
					<div ng-app="myApp" ng-controller="myCtrl">
						<textarea name="post" rows="7" cols="59" placeholder="Create your POST" style=" font-size:50px; font-family: {{myfont}}; background: {{myback}}; border: none; color:{{mytext}}; transition: 0.25s; outline: none;"></textarea>
						<p1 class="p1">Font style</p1>
						<p2 class="p2">Background color</p2>
						<p3 class="p3">Text color</p3><br>
							<select class="black" ng-model="myfont" style="margin:15px" id="id1" name="font">
							<option ng-repeat="x in cars" style="font-family: {{x.font}}" value="{{x.font}}">{{x.font}}</option>
							</select>
							<select class="black" ng-model="myback" style="margin:0 25px" id="id2" name="back">
							<option ng-repeat="x in cars" style="background: {{x.back}}" value="{{x.back}}">CHOOSE BACKGROUND</option>
							</select>
							<select class="black" ng-model="mytext" style="margin:15px" id="id3" name="text">
							<option ng-repeat="x in cars" style="background:{{x.text}}" value="{{x.text}}">CHOOSE TEXT COLOR</option>
							</select>
						</div>
						
						<script>
						var app = angular.module('myApp', []);
						app.controller('myCtrl', function($scope) {
							$scope.cars = [
								{font : "Courier New", back : "#ED5565", text : "#00ffff"},
								{font : "Times New Roman", back : "#DA4453", text : "#000000"},
								{font : "Arial Narrow", back : "#FC6E51", text : "#0000ff"},
								{font : "Candara", back : "#E9573F", text : "#ff00ff"},
								{font : "Monaco", back : "#FFCE54", text : "#008000"},
								{font : "Brush Script MT", back : "#F6BB42", text : "#808080"},
								{font : "Garamond", back : "#A0D468", text : "#00ff00"},
								{font : "loud", back : "#8CC152", text : "#800000"},
								
								{font : "Andale Mono", back : "#48CFAD", text : "#000080"},
								{font : "Georgia", back : "#37BC9B", text : "#808000"},
								{font : "Marlett", back : "#4FC1E9", text : "#800080"},
								{font : "Webdings", back : "#3BAFDA", text : "#ff0000"},
								{font : "Monaco", back : "#5D9CEC", text : "#c0c0c0"},
								{font : "Impact", back : "#AC92EC", text : "#008080"},
								{font : "Verdana", back : "#EC87C0", text : "#ffffff"},
								{font : "Futura", back : "#AAB2BD", text : "#ffff00"},
								
								{font : "Osaka", back : "#434A54", text : "#8b0000"},
								{font : "Capitals", back : "#DA860B", text : "#adff2f"},
								{font : "Optima", back : "#7FFFD4", text : "#4b0082"},
								{font : "Baskerville", back : "#8B4513", text : "mediumblue"},
								
							];
						});
						</script>
				<div class = "login" style="text-align: center;">
					<input class="submit" name="ok" type="submit" value="Submit">
				</div>
			</form>''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
	post=frm.getvalue('post')
	font=frm.getvalue('font')
	back=frm.getvalue('back')
	text=frm.getvalue('text')
	try:
		cursor = config.db8.cursor()
		sql = "INSERT INTO post(post,font,back,text,pid) VALUES ('{}','{}','{}','{}',1)".format(post,font,back,text)
		cursor.execute(sql)
		config.db8.commit()
		config.db8.close()
		print('''<h1 style="color:green;">Upload successfull</h1>''')
	except Exception as e:
		print(e)
print('''
		</div>
	</body>
</html>
''')