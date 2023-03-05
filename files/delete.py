import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n''')
frm=cgi.FieldStorage()
pid=frm.getvalue('pid')

try:
    cursor=config.db8.cursor()
    upd="DELETE from post WHERE sid='{}'".format(pid)
    cursor.execute(upd)
    config.db8.commit()
    config.db8.close()
    print('''<script>
    window.location="adminPost.py?msg=Successfully posted in HOME page"
    </script>''')
except Exception as e:
    print('''<script>
    window.location="adminPost.py?msg={}"
    </script>'''.format(e))