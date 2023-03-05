import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<!DOCTYPE HTML>
<html>
<meta http-equiv="content-type" content="text/html;charset=UTF-8" />
<head>
	<title>Paitent Registration</title>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" >
	<meta name="keywords" content="Airline Booking Form Responsive Widget,Login form widgets, Sign up Web forms , Login signup Responsive web form,Flat Pricing table,Flat Drop downs,Registration Forms,News letter Forms,Elements">
	<script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>

<style>
* {
  box-sizing: border-box;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen-Sans, Ubuntu, Cantarell, "Helvetica Neue", sans-serif;
}
.clear {
    clear: both;
}
img {
    max-width: 100%;
}
body {
    font-family: 'Roboto', sans-serif;
    font-size: 100%;
    background-image: url('images/acb.jpg');
    background-size: 100; 
}
.booking-form-w3layouts {
    box-sizing: border-box;
    padding: 3em 3em;
    background: rgba(0, 0, 0, 0.78);
    width: 50%;
    margin: 0 auto;
    border-radius: 60px;
    margin-top: 50px;
}

h2.sub-heading-agileits,
h3.sub-heading-agileits {
    display: inline-block;
    text-align: left;
    font-size: 24px;
    color: #60baee;
    text-transform: capitalize;
    margin-bottom: .4em;
    padding: 0px 25px 10px 0px;
    font-weight: 400;
    letter-spacing: 2px;
    border-bottom: 2px solid #fff;
    font-family: 'Raleway', sans-serif;
}
.radio-section {
    text-align: left;
    margin: 0.7em 0;
}
.radio-section h6 {
    display: inline;
    margin-top: 10px;
    color: #60baee;
    font-size: 19px;
    text-transform: capitalize;
    margin-bottom: .7em;
    font-weight: 400;
    letter-spacing: 2px;
    font-family: 'Raleway', sans-serif;
    font-size: x-large;
}
.radio-section ul {
    display: inline;
}
.radio-buttons-w3-agileits li input[type="radio"] {
    cursor: pointer;
}
.radio-buttons-w3-agileits li label {
    color: rgb(255, 255, 255);
    font-size: 13.5px;
    font-weight: 400;
    letter-spacing: 1px;
    font-family: 'Raleway', sans-serif;
    font-size: large;
}
.booking-form-w3layouts input[type="text"],
.booking-form-w3layouts input[type="email"],
.booking-form-w3layouts textarea,
select.form-control,
input#datepicker {
    width: 100%;
    font-weight: 300;
    color: rgb(255, 255, 255);
    font-size: 14px;
    letter-spacing: 1.2px;
    padding: 10px 10px;
    outline: none;
    background: rgba(255, 255, 255, 0);
    border: none;
    border-bottom: 1px solid rgb(230, 82, 82);
    box-sizing: border-box;
    font-family: 'Roboto', sans-serif;
    font-size: large;
    overflow: hidden;
}
.booking-form-w3layouts input[type="date"]{
    width: 100%;
    font-weight: 300;
    color: rgb(255, 255, 255);
    font-size: 14px;
    letter-spacing: 1.2px;
    padding: 7px 10px;
    outline: none;
    background: rgba(255, 255, 255, 0);
    border: none;
    border-bottom: 1px solid rgb(230, 82, 82);
    box-sizing: border-box;
    font-family: 'Roboto', sans-serif;
    font-size: large;
    overflow: hidden;
    margin-right: 250px;

}
.booking-form-w3layouts textarea {
    resize: none;
    height: 80px;
}
.field-agileinfo-spc {
    margin-bottom: 2em;
}
.form-w3-agile-text {
    width: 100%;
}
select.form-control option {
    background: #000;
}
.booking-form-w3layouts input[type="submit"] {
    text-transform: capitalize;
    background: #0091cd;
    color: #bac1c9;;
    padding: 0.5em 4em;
    border: none;
    font-weight: 500;
    font-size: 1.6em;
    margin-top: 1em;
    float: left;
    outline: none;
    letter-spacing: 1px;
    -webkit-transition: .5s all;
    -moz-transition: .5s all;
    transition: .5s all;
    cursor: pointer;
    font-family: 'Raleway', sans-serif;
}
.booking-form-w3layouts input[type="submit"] {
    margin-right: 1.5em;
    background: #d2741c;
    border-radius: 12px;
    height:60px;
    width: 280px;
    
}
.booking-form-w3layouts input[type="submit"]:hover {
    background: #0091cd;
    color: #fff;
    margin-right: 5px;
}
.booking-form-w3layouts ::-webkit-input-placeholder {
    color: rgb(255, 255, 255);
    font-size: large;
}
ul.radio-buttons-w3-agileits li {
    display: inline-block;
    margin: 0em 2em;
}
.textbox{
	width: 430px;
	overflow: hidden;
	padding: 8px;
	margin: 8px 8px;
	text-align: left;
	border-bottom:2px solid rgb(230, 82, 82);
    margin-bottom: 30px;
    
}
.textbox input[type="password"]{
	background: none;
	border: none;
	color:white;
	transition: 0.25s;
	text-align:left;
	outline: none;
    margin-bottom: 10px;  
}
.textbox input[type="password"]:focus{
	width:300px;
	font-size:20px;
}
#message {
  display:none;
  background:rgba(0, 0, 0, 0.7);
  color: #000;
  position: relative;
  padding: 15px;
  margin-top: 10px;
  width: 600px;
  height: 310px;
  text-align: center;
  left: 34%;
  border: 2px solid rgb(255, 156, 156);
  border-radius: 15px;
 
}
#message p {
  padding: 10px 35px;
  font-size: 18px;
}
.valid {
  color: green;
}
.invalid {
  color: red;
}
li a:hover {
    background-color: rgb(230, 82, 82);
  }
@media(min-width:481px) {
    .main-flex-w3ls-sectns {
        display: -webkit-flex;
        display: flex;
        -webkit-justify-content: space-between;
        justify-content: space-between;
    }
    .form-w3-agile-text1,
    .form-w3-agile-text2 {
        flex-basis: 48.5%;
        -webkit-flex-basis: 48.5%;
    }
}

</style>


</head>

<body style="background-image: url(img/pp.jpg); background-repeat: no-repeat;background-size: 100% 100%;">
	<ul style=" list-style-type: none;margin-top: 1px; padding: 0;overflow: hidden; background-color: hsl(0, 54%, 47%);">
      <li style="float: right;"><a class="active" href="paitentlogin.py" style="display: block;color: white;text-align: center;padding: 14px 16px;text-decoration: none;"><i class="fas fa-home"></i>  Back To Login</a></li>
  </ul>
  <div class="booking-form-w3layouts">
		<h1 style="font-size: 90px; font-weight: 700; text-transform: capitalize; color: rgb(230, 82, 82); text-shadow: 1px 1px 7px #6b6b6b; letter-spacing: 5px; text-align: center; font-family: Brush Script MT; margin-bottom: 40px;">Paitent Registration</h1>
		<!-- Form starts here -->
		<form name="frm" method="post" onsubmit="return login()">
			<h2 class="sub-heading-agileits">Paitent Details</h2>
			<div class="main-flex-w3ls-sectns">
				<div class="field-agileinfo-spc form-w3-agile-text">
					<input  type="text" name="name" placeholder="Your Full Name" required="">
				</div>
	
			</div>
			<div class="main-flex-w3ls-sectns">
				<div class="field-agileinfo-spc form-w3-agile-text1">
					<input type="text" name="fname" placeholder="Father Name" required="">
				</div>
				<div class="field-agileinfo-spc form-w3-agile-text2">
					<input type="text" name="mname" placeholder="Mother Name" required="">
				</div>
			</div>
			<div class="field-agileinfo-spc form-w3-agile-text">
				<input type="email" name="email" placeholder="Email" required="">
			</div>

			<div class="main-flex-w3ls-sectns">
				<div class="field-agileinfo-spc form-w3-agile-text1">
					<label for="email"><p style="font-size: 150%; color: #60baee; ">Date Of Birth</p></label>
			</div>
					<div class="field-agileinfo-spc form-w3-agile-text2">
						<input id="datepicker1" name="dob" type="date"  required="">
				    </div>		
			</div>
			<div class="main-flex-w3ls-sectns">
				<div class="field-agileinfo-spc form-w3-agile-text1">
					<input type="text" name="mob" placeholder="Mobile Number" required maxlength="10">
				</div>
				<div class="field-agileinfo-spc form-w3-agile-text2">
					<input type="text" name="age" placeholder="Age" required="">
				</div>
			</div>
			<div class="radio-section">
				<h6>Gender</h6>
				<ul class="radio-buttons-w3-agileits">
					<li>
						<input type="radio" id="a-option" value="Male" name="gen">
						<label for="a-option">Male</label>
						<div class="check"></div>
					</li>
					<li>
						<input type="radio" id="b-option" value="Female" name="gen">
						<label for="b-option">Female</label>
						<div class="check">
							<div class="inside"></div>
						</div>
					</li>
					<li>
						<input type="radio" id="c-option" value="Others" name="gen">
						<label for="c-option">Others</label>
						<div class="check">
							<div class="inside"></div>
						</div>
					</li>
				</ul>
			</div><br>
			<div class="main-flex-w3ls-sectns">
			<div class="field-agileinfo-spc form-w3-agile-text1">
				<select class="form-control" name="bld">
									<option value="Select">Blood Group</option>''')
bld=["A+","B+","AB+","O+","A-","B-","AB-","O-"]
for i in bld:
    print('<option value="{}">{}</option>'.format(i, i))
print('''    
				</select>
			</div>
			<div class="field-agileinfo-spc form-w3-agile-text2">
				<select class="form-control" name="city">
									<option value="Select">City</option>''')
city=["Kolkata","Siliguri","Medinipur","Bakura","Nodia","Darjeeling","Bardwan","Kharagpur","Haldia","Asansol","Durgapur"]
for i in city:
    print('<option value="{}">{}</option>'.format(i, i))
print('''
				</select>
			</div>
		</div>
		<div class="field-agileinfo-spc form-w3-agile-text">
			<textarea name="addr" placeholder="Your Address..."></textarea>
		</div>
		
		<div class="main-flex-w3ls-sectns">
			<div class="field-agileinfo-spc form-w3-agile-text1">
					<input type="text" name="wght" placeholder="Weight (Kg)" required="">
			</div>
			<div class="field-agileinfo-spc form-w3-agile-text2">
				
				<input type="text" name="hght" placeholder="Height (Feet/Centimeters)" required="">
		    </div>
		</div>
		<div class="main-flex-w3ls-sectns">
		<div class="textbox" >          
			<input type="Password" id="psw" placeholder="Password" name="psw" required maxlength="30">
		</div>
		<div class="textbox">          
			<input type="Password" id="pssw" placeholder="Confirm Password" name="re-password" required maxlength="30" >
			<span id="msg" style="color: red;"></span>
			
		</div>
	</div>
		<div class="main-flex-w3ls-sectns">
			<div class="field-agileinfo-spc form-w3-agile-text1">
				<select class="form-control" name="sques" required>
									<option value="Select">Security Question</option>''')
secu=["What is your oldest cousins first name?","What is your favourite actor?","What is your favourite food?","What is the title and artist of your favorite song?","What is your work address?","In what city or town did your mother and father meet?","What is your cars license plate number?","What was your first car?","What is the middle name of your oldest child?","what was your first pets name?","In what city or town was your first job?","What was your childhood nickname?","What is your favourite cricket team?"]
for i in secu:
    print('<option value="{}">{}</option>'.format(i, i))
print('''							</select>
			</div>
			<div class="field-agileinfo-spc form-w3-agile-text2">
				<div class="field-agileinfo-spc form-w3-agile-text2">
					<input type="text" name="sans" placeholder="Security Answer" required="">
				</div>
			</div>
			</div>
	
			<div class="clear"></div>
			<input type="submit" name="ok" value="Submit">
			<div class="clear"></div>
		</form>''')
frm=cgi.FieldStorage()
if frm.getvalue('ok'):
    name=frm.getvalue('name')
    fname=frm.getvalue('fname')
    mname=frm.getvalue('mname')
    email=frm.getvalue('email')
    dob=frm.getvalue('dob')
    mob=frm.getvalue('mob')
    age=frm.getvalue('age')
    gen=frm.getvalue('gen')
    bld=frm.getvalue('bld')
    city=frm.getvalue('city')
    addr=frm.getvalue('addr')
    wght=frm.getvalue('wght')
    hght=frm.getvalue('hght')
    psw=frm.getvalue('psw')
    sques = frm.getvalue('sques')
    sans = frm.getvalue('sans')
    try:
        cursor = config.db8.cursor()
        src = "SELECT email FROM registration WHERE email='{}'".format(email)
        cursor.execute(src)
        rec = cursor.fetchall()
        if rec:
            print('''<h1 style="font-family: loud; font-size: 50px; text-align: center; color: red">You are already registered</h1>''')
        else:
            sql = "INSERT INTO registration(name,fname,mname,email,dob,mob,age,gen,blood,city,addr,wgh,hgh,psw,squs,sans) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,fname,mname,email,dob,mob,age,gen,bld,city,addr,wght,hght,psw,sques,sans)
            cursor.execute(sql)
            config.db8.commit()
            config.db8.close()
            print('''<h1 style="font-family: loud; font-size: 50px; text-align: center; color: rgb(62, 192, 68);">Registration Successfull</h1>''')
    except Exception as e:
        print(e)
print('''
		<!--// Form starts here -->
	</div>
	<div id="message">
        <h3 style="color: rgb(255, 248, 145);">Password must contain the following:</h3>
        <p id="letter" class="invalid">A <b>lowercase</b> letter</p>
        <p id="capital" class="invalid">A <b>capital (uppercase)</b> letter</p>
        <p id="number" class="invalid">A <b>number</b></p>
        <p id="length" class="invalid">Minimum <b>8 characters</b></p>
    </div>
	<script>
        var myInput = document.getElementById("psw");
        var letter = document.getElementById("letter");
        var capital = document.getElementById("capital");
        var number = document.getElementById("number");
        var length = document.getElementById("length");
        
        // When the user clicks on the password field, show the message box
        myInput.onfocus = function() {
          document.getElementById("message").style.display = "block";
        }
        
        // When the user clicks outside of the password field, hide the message box
        myInput.onblur = function() {
          document.getElementById("message").style.display = "none";
        }
        
        // When the user starts to type something inside the password field
        myInput.onkeyup = function() {
          // Validate lowercase letters
          var lowerCaseLetters = /[a-z]/g;
          if(myInput.value.match(lowerCaseLetters)) {  
            letter.classList.remove("invalid");
            letter.classList.add("valid");
          } else {
            letter.classList.remove("valid");
            letter.classList.add("invalid");
          }
          
          // Validate capital letters
          var upperCaseLetters = /[A-Z]/g;
          if(myInput.value.match(upperCaseLetters)) {  
            capital.classList.remove("invalid");
            capital.classList.add("valid");
          } else {
            capital.classList.remove("valid");
            capital.classList.add("invalid");
          }
        
          // Validate numbers
          var numbers = /[0-9]/g;
          if(myInput.value.match(numbers)) {  
            number.classList.remove("invalid");
            number.classList.add("valid");
          } else {
            number.classList.remove("valid");
            number.classList.add("invalid");
          }
          
          // Validate length
          if(myInput.value.length >= 8) {
            length.classList.remove("invalid");
            length.classList.add("valid");
          } else {
            length.classList.remove("valid");
            length.classList.add("invalid");
          }
        }
        </script>
       
<script>
    function login() {
		        var pwd = document.getElementById("psw").value;
                var pswd = document.getElementById("pssw").value;
			
                if(pwd!=pswd){
					 document.getElementById("msg").innerHTML="**Password are not same";
					  return false;
					
                }
                
    }
            
</script>




	</body>

</html>''')