import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE html>
<html>
	<head>
	  	<meta charset="utf-8">
		 <title>Feedback</title>
		 <meta name="viewport" content="width=device-width, initial-scale=1.0">
		 <script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>
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
   color: #fff;
   font-size: 13px;
   margin: 0;}
   input, textarea, select, button {
   font-family: "Poppins-Regular";
   color: white;
   font-size: 16px;
   font-size: medium; }
   p, h1, h2, h3, h4, h5, h6, ul {
  margin: 0; }
  img {
  max-width: 100%; }
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
  align-items: center; }
 .inner {
  padding:2px;
  background: rgb(218, 60, 60);
  width: 840px;
  height: 850px;
  margin: auto;
  display: flex; 
  border-radius: 10px;
  border: 2px solid rgb(245, 241, 241);
  margin-top:320px ;}
  .inner .image-holder {
    width: 0%;}
  .inner form {
    width: 90%;
    padding-top: 36px;
    padding-left: 50px;
    padding-right: 10px; }
  .inner h3 {
    text-transform: uppercase;
    font-size: 25px;
    font-family: "Poppins-SemiBold";
    text-align: center;
    font-size: x-large;}
  .form-group {
  display: flex;
  width: 100%; }
 .form-group input {
    width: 50%; }
.form-group input:first-child {
    margin-right: 25px; }
.form-wrapper {
  position: relative; }
.form-control {
  border: 1px solid #fff;
  border-top: none;
  border-right: none;
  border-left: none;
  display: block;
  width: 100%;
  height: 30px;
  padding: 0;
  background-color: transparent;
  margin-bottom: 25px; }
.form-control::-webkit-input-placeholder {
  font-size: 13px;
  color: #000;
  font-family: "Poppins-Regular"; 
  font-size: large;}
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
  width: 180px;
  height: 51px;
  margin: auto;
  margin-top: 56px;
  margin-right: 240px;
  border-radius: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
  background: rgb(65, 142, 187);
  font-size: 16px;
  color: #fff;
  vertical-align: middle;
  -webkit-transform: perspective(1px) translateZ(0);
  transform: perspective(1px) translateZ(0);
  -webkit-transition-duration: 0.3s;
  transition-duration: 0.3s; }
.button i {
    margin-left: 10px;
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
      height: 50px;
      overflow: hidden;
      background-color: hsl(0, 54%, 47%); }
 li {
      float: right;}
li a {
      display: block;
      color: white;
      text-align: center;
      padding: 14px 16px;
      text-decoration: none;
      font-size: large;}
li a:hover {
   background-color: rgb(230, 82, 82);}
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
  .button {
    margin-top: 60px; } } 
</style>
  <body style="background-image: url(img/aa.png) ; background-repeat: no-repeat; background-size: 100% 100%;">
		  <ul>
			  <li><a class="active" href="index.py"><i class="fas fa-home"></i>  Back To Home</a></li>
      </ul>
	  <div class="wrapper" >
		  <div class="inner">
			  <form name="frm" method="post">
             <h3 style="margin-left: 70px;margin-bottom: 80px;">Give Your Feedback <i class="far fa-comments" style="font-size: 42px;"></i></h3>
            <div class="form-wrapper" style="font-size: 17px;"><i class="far fa-user"></i> USER NAME<br><br>
						   <input type="text" name="name" placeholder="Your Full Name..." class="form-control">	
					  </div>
            <div class="form-wrapper" style="font-size: 17px;"><i class="far fa-envelope"></i> EMAIL ID<br><br>
						  <input type="email" name="email" placeholder="Email Address..." class="form-control">
					  </div>
            <div class="form-wrapper" style="font-size: 20px;"><i class="far fa-question-circle"></i> Any suggestion....<br><br>       
              <input type="text" class="form-control" name="qa2" placeholder="Answer..." required>
            </div>
            <div class="form-wrapper" style="font-size: 20px;"><i class="far fa-question-circle"></i> How can we improve....</p><br>     
              <input type="text" class="form-control" name="qa3" placeholder="Answer..." required>
            </div>
            <div class="form-wrapper" style="font-size: 20px;"><i class="far fa-question-circle"></i> If you were describing this web page to a friend, would you say this web page is....</p><br>  
              <input type="text" class="form-control" name="qa4" placeholder="Answer..." required>
            </div>
            <div class="form-wrapper" style="font-size: 20px;"><i class="far fa-question-circle"></i> Are there any feature which you would like to see add or expanded on the future?</p><br>     
              <input type="text" class="form-control" name="qa5" placeholder="Answer..." required>
            </div>
					  <div class="button">
              <input type="submit" name="ok" value="SEND FEEDBACK" style="background-color:rgb(65, 142, 187);color:#fff;border:none;">
              <i class="fas fa-arrow-right"></i>
            </div>
			  ''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    post=frm.getvalue('name')
    font=frm.getvalue('email')
    sug=frm.getvalue('qa2')
    imp=frm.getvalue('qa3')
    frnd = frm.getvalue('qa4')
    ftr = frm.getvalue('qa5')
    try:
        cursor = config.db8.cursor()
        sql = "INSERT INTO fdbk(name,email,sug,imp,frnd,ftr) VALUES ('{}','{}','{}','{}','{}','{}')".format(post,font,sug,imp,frnd,ftr)
        cursor.execute(sql)
        config.db8.commit()
        config.db8.close()
        print('''<br><br><h1 style="color:green; text-align:center; ">Thank You</h1>''')
    except Exception as e:
        print(e)
print('''
		</form></div>  
	  </div>	
  </body>
</html>''')