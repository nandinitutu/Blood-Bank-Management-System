import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n''')
frm=cgi.FieldStorage()
pid=frm.getvalue('pid')

pid = int(pid)-1
bid=1
try:
    cursor=config.db8.cursor()
    upd="UPDATE bldstck SET ong='{}' WHERE bid='{}'".format(pid,bid)
    cursor.execute(upd)
    config.db8.commit()
    config.db8.close()
    print('''<script>
    window.location="hospitalprofile.py?msg=Successfull"
    </script>''')
except Exception as e:
    print('''<script>
    window.location="hospitalprofile.py?msg={}"
    </script>'''.format(e))