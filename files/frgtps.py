import cgi, cgitb, config

cgitb.enable()
print('''Content-type:text/html\r\n\r\n
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forget password</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
</head>


<body style="background-image: url(https://wallpaperaccess.com/full/619974.jpg);background-size: 100%;">
    <div class="flex-container" style="display: flex;background:#9EECD9;align-items: center;justify-content: center;width: 480px;height: 570px;position: absolute;left:785px;top: 120px;opacity: 0.5;filter: alpha(opacity=60);-moz-opacity: 0.6;opacity: 0.6;border: 5px black;">
    </div>
        <form method="post" name="frm" id="my_form" class="login-form" style="width: 360px;height: 500px;text-align: center;position: absolute;top: 140;left:850;width: 360;height: 550;filter: alpha(opacity=60);-moz-opacity: 0.6;opacity: 0.6;background: transparent;">
            <h1 style="font-size: 20px;color:#FA5D08;">Forget Password for hospital</h1>
            <div class="form-element" style="padding-top: 80px;font-size: large;">
                <input name="email" style="font-size: 100%;line-height: 30px;" type="email" placeholder="Email id">
                <div class="dropdown"><br>
                    <select name="sques" id="squestion" placeholder="Security question" style="size:480px;width:230px;height:40px;" >
                     <datalist id="squestion" class="squestion">
                        <option value="">
                        <label for="Squestion"> Security Questions </label>
                        </option>''')
squs=["What is your oldest cousins first name?","What is your favourite actor?","What is your favourite food?","What is the title and artist of your favorite song?","What is your work address?","In what city or town did your mother and father meet?","What is your cars license plate number?","What was your first car?","What is the middle name of your oldest child?","what was your first pets name?","In what city or town was your first job?","What was your childhood nickname?","What is your favourite cricket team?"]

for i in squs:
    print('<option value="{}">{}</option>'.format(i, i))
print('''
                     </datalist>
                    </select>
                </div><br>                    
                    <input style="line-height: 30px;" type="text" name="sans" placeholder="Security Answer"/><br><br>
                    <input type="submit" name="ok" value="SHOWS" style="color: rgb(0, 0, 0);background-color: aquamarine;position: absolote;top: 2px;">
                </div><br>
                <a href="#" style="display: flex;position: absolute;left: 130px;top: 400px;background-color: rgb(1, 172, 143);border: 2px black;color: aliceblue;width: 100px;height: 50px;">Back to Homepage</a>
        </form>''')
frm = cgi.FieldStorage()
if frm.getvalue('ok'):
    email = frm.getvalue('email')
    sques = frm.getvalue('sques')
    sans = frm.getvalue('sans')
    try:
        src = "SELECT email,squs,sans FROM registration WHERE email='{}' AND squs='{}' AND sans='{}'".format(email, sques,sans)
        cursor = config.db8.cursor()
        cursor.execute(src)
        rec = cursor.fetchall()
        if rec:
            try:
                drc = "SELECT * FROM registration WHERE email='{}'".format(email)
                cursor = config.db8.cursor()
                cursor.execute(drc)
                rs = cursor.fetchall()
            except Exception as e:
                print(e)
            if rs:
                for rec in rs:
                    '''print(rec)
                    print('<br>')'''
                    print('''<a style="padding-top:20px; padding-left:14px; height:60px; width:200px; color:white; position:absolute; background:blue; center;left:1480px;top: 400px;">Your Password is {}</a>''''</option>'.format(rec[14]))
        else:
            print('''<a style="padding-top:20px; padding-left:14px; height:60px; width:200px; color:white; position:absolute; background:red; center;left:1480px;top: 400px;">please choose Right one</a>''')


    except Exception as e:
        print(e)
print('''             
</body>
</html>''')