print('''Content-type:text/html\r\n\r\n''')
import cgi, cgitb, config
cgitb.enable()
frm=cgi.FieldStorage()
uid=frm.getvalue('uid')
bid=frm.getvalue('bid')
try:
    cursor = config.db3.cursor()
    sql = "INSERT INTO account(uid,bid) VALUES ('{}','{}')".format(uid, bid)
    cursor.execute(sql)
    config.db3.commit()
    config.db3.close()
except Exception as e:
    print(e)

bid=frm.getvalue('bid')
sub=1
try:
    cursor=config.db3.cursor()
    upd="UPDATE books SET status='{}' WHERE bid='{}'".format(sub,bid)
    cursor.execute(upd)
    config.db3.commit()
    config.db3.close()
    print('''<script>
    window.location="details.py?msg=Successfully booked"
    </script>''')
except Exception as e:
    print('''<script>
    window.location="details.py?msg={}"
    </script>'''.format(e))

