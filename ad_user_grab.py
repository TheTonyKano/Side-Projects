#This program will grab a list of users from Active Directory.
#With this list it would be able to then sort and filter out users who have logged in within 60 days
#users who are 60 days and over will be processed to a separate file to be processed for disabling.
from ldap3 import Connection, Server

user = input('Enter your username: ')
password = input('Enter your password: ')
server = Server('dc.cflccss.com')
conn = Connection(server, user, password, auto_bind=True)
print(server.info)
