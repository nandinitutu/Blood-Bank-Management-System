import cgi, cgitb,config
cgitb.enable()
frm=cgi.FieldStorage()
email=frm.getvalue('email')
password=frm.getvalue('password')
cursor=config.db8.cursor()
src="SELECT * FROM request WHERE hemail='{}' AND hpass='{}'".format(email,password)
cursor.execute(src)
rs=cursor.fetchall()
if rs:

    #print('''Content-type:text/html\r\n\r\n''')
    #print(rs[0])
    rec=""
    i=0
    for data in rs[0]:
        if i>0:
            rec+=","
        rec+=str(data)
        i=i+1

    print('Content-type:text/html\n')
    print("")
    print("")
    print('''<script>
    window.location="hospitalprofile.py"
    </script>''')
else:
    print('''Content-type:text/html\r\n\r\n
    <script>
        window.location="hospitallogin.py?msg=Invalid email or password"
    </script>''')