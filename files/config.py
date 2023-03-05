#print('Content-type:text/html\r\n\r\n')
import pymysql, sys
try:
    db8=pymysql.connect(host="localhost", user="root", passwd="", db="bbms")
except Exception as e:
    sys.exit(e)
    #print(e)