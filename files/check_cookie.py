import os, cgitb, http.cookies
cgitb.enable()
print('Content-type:text/html\n\n')
if 'HTTP_COOKIE' in os.environ:
    c=http.cookies.SimpleCookie()
    cookie_data=os.environ.get('HTTP_COOKIE')
    c.load(cookie_data)
    try:
        #print(c['u_info'].value)
        user_data = c['u_info'].value.split(',')
        #print(user_data)
    except KeyError:
        print('''<script>
        window.location="paitentprofile.py"
        </script>''')
else:
    print('''<script>
    window.location="paitentprofile.py"
    </script>''')