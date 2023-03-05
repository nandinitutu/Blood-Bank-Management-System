import cgi, cgitb, http.cookies, config
cgitb.enable()
frm=cgi.FieldStorage()
email=frm.getvalue('email')
password=frm.getvalue('password')
cursor=config.db8.cursor()
src="SELECT * FROM registration WHERE email='{}' AND psw='{}'".format(email,password)
cursor.execute(src)
rs=cursor.fetchall()
if rs:
    c=http.cookies.SimpleCookie()
    #print('''Content-type:text/html\r\n\r\n''')
    #print(rs[0])
    rec=""
    i=0
    for data in rs[0]:
        if i>0:
            rec+=","
        rec+=str(data)
        i=i+1
    c['u_info']=rec
    c['u_info']['expires'] = 60*60*24*30
    print(c)
    print('Content-type:text/html\n')
    print("")
    print("")
    print('''<script>
    window.location="paitentprofile.py"
    </script>''')
else:
    print('''Content-type:text/html\r\n\r\n
    <script>
        window.location="paitentlogin.py?msg=Invalid email or password"
    </script>''')