import cgi, cgitb, config
cgitb.enable()
print('''Content-type:text/html\r\n\r\n''')
frm=cgi.FieldStorage()
rid=frm.getvalue('pid')

try:
    cursor=config.db8.cursor()
    upd="DELETE from donorbld WHERE did='{}'".format(rid)
    cursor.execute(upd)
    config.db8.commit()
    config.db8.close()
    print('''<script>
    window.location="adminPatients.py?msg=Deleted Successfully "
    </script>''')
except Exception as e:
    print('''<script>
    window.location="adminPatients.py?msg={}"
    </script>'''.format(e))