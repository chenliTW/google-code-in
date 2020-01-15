from fedora.client.fas2 import AccountSystem
from fedora.client import AuthError

# Get an AccountSystem object.  All AccountSystem methods need to be
# authenticated so you might as well give username and password here.
fas = AccountSystem(username='chenlitw', password="")

username=input("username you want to query : ")

res=fas.people_by_key(key='username', search=username, fields=['human_name', 'email', 'id'])
if len(res):
    out='''
result for username : {}

id : {}
human_name : {}
email : {}
'''.format(username,res[username]['id'],res[username]['human_name'],res[username]['email'])
    print(out)
else:
    print('\033[0;31mError! \nuser not found!!!\033[1;37m')
