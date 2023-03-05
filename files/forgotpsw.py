import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n
    <html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="forgetpsswrd.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <script src="https://kit.fontawesome.com/10c78be679.js" crossorigin="anonymous"></script>
    <title>Forget Password For Patient</title>
</head>
<body style="background-image: url('https://c0.wallpaperflare.com/preview/386/354/385/analysis-hospital-doctor-medical.jpg');background-size: 100%;">
    <div style="width: 360px; padding: 8% 0 0; margin: auto;">
        <div style="height: 600px;"class="form"><h1 style="font-size: 20px;color:yellow;"><b>Forget Password For Patient & Donor</b></h1><br>
          <form style="position: relative;z-index: 1;max-width: 360px;margin: 0 auto 100px;padding: 45px;text-align: center;box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);"">
            <input style="font-family: "Roboto", sans-serif;outline: 0;background: #ffffff;width: 100%;border: 0;margin: 0 0 15px;padding: 15px;box-sizing: border-box;font-size: 14px;" type="email" placeholder="Email id"/>
            <div style="font-family: "Roboto", sans-serif;outline: 0;background: #ffffff;width: 100%;border: 0;margin: 0 0 15px;padding: 15px;box-sizing: border-box;font-size: 14px;">
                <select style="width:182px;height:50px;color: blue;" name="Security Question" id="squestion" placeholder="Security question">
                  <datalist id="squestion" class="squestion">
                    <option value="">
                      <label for="Squestion"> Security Questions </label>
                    </option>''')
squs=["What is your oldest cousins first name?","What is your favourite actor?","What is your favourite food?","What is the title and artist of your favorite song?","What is your work address?","In what city or town did your mother and father meet?","What is your cars license plate number?","What was your first car?","What is the middle name of your oldest child?","what was your first pets name?","In what city or town was your first job?","What was your childhood nickname?","What is your favourite cricket team?"]
for i in squs:
    print('<option value="{}">{}</option>'.format(i, i))
print('''         </datalist>
                </select>
            </div><br>
            <input style="font-family: "Roboto", sans-serif;outline: 0;background: #ffffff;width: 100%;border: 0;margin: 0 0 15px;padding: 15px;box-sizing: border-box;font-size: 14px;" type="text" placeholder="Security Answer"/>
            <input style="font-family: "Roboto", sans-serif;outline: 0;background: green;width: 100%;border: 0;margin: 0 0 15px;padding: 15px;box-sizing: border-box;font-size: 14px;" type="submit" name="ok" value="SHOW">
          </form>''')
frm = cgi.FieldStorage()
if frm.getvalue('ok'):
    email = frm.getvalue('email')
    sques = frm.getvalue('sques')
    sans = frm.getvalue('sans')
    try:
        src = "SELECT hemail,sques,sans FROM request WHERE hemail='{}' AND sques='{}' AND sans='{}'".format(email, sques, sans)
        cursor = config.db8.cursor()
        cursor.execute(src)
        rec = cursor.fetchall()
        if rec:
            try:
                drc = "SELECT * FROM request WHERE hemail='{}'".format(email)
                cursor = config.db8.cursor()
                cursor.execute(drc)
                rs = cursor.fetchall()
            except Exception as e:
                print(e)
            if rs:
                for rec in rs:
                    '''print(rec)
                  print('<br>')'''
                print('''<h1 style="color:blue;">Your Password is {}</h1>''''</option>'.format(rec[3]))
            else:
                print('''<h1 style="color:blue;">please choose Right one</h1>''')
    except Exception as e:
        print(e)
print('''        </div> 

        <button style="position:absolute;left:730px;background:#0895cc;font-family: "Roboto", sans-serif;text-transform: uppercase;font-size: 30px;margin-top: -50px;outline: 0;background: #0065fd;width:500px;border: 0;padding: 15px;color: #0a0a0a;font-size: 14px;-webkit-transition: all 0.3 ease;transition: all 0.3 ease;cursor: pointer;margin-left: -70px;border-radius: 18px;" ><a href="#" style="color: black;font-family: "Roboto", sans-serif;text-transform: uppercase;outline: 0;background: #0065fd;width: 100%;border: 0;padding: 15px;color: #7e7c7c;font-size: 14px;-webkit-transition: all 0.3 ease;transition: all 0.3 ease;cursor: pointer;"><i class="fas fa-angle-double-left"></i>Back To Home</button> </div>
</body>
</html>''')