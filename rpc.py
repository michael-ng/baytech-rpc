#!/usr/bin/python
import getpass
import sys
import telnetlib

DEBUG = True

class rpc3:
    def __init__(self,host,login=None, passwd=None):
        print ("Initializing")
        self.host = host
        self.login = login
        self.passwd = passwd
        self.status = "offline"
        # 8 outlets
        self.outlets = ();
        
    def connect(self):
        print ("Making connection to " + self.host)
        if (DEBUG is True):
            if (self.login is not None ):
                if (self.passwd is not None):
                    print ("as " + self.login +  "/" + self.passwd)
                else:
                    print ("as " + self.login)
        # use telnetlib
        self.conn = telnetlib.Telnet(self.host)
#        conn.read_until("login: ")
#        if (self.login is not False):
#            conn.write(self.login = "\n")
#        print (self.conn.read_until("for a list of commands"))

    def disconnect(self):
        if self.status == "online":
            self.conn.write("Logoff\n")
            self.status = "offline"

    def getStatus(self):
        isPrompt = False
        while isPrompt is False:
            # remove \n\r at the end.
            # rstrip("\n\r") leave some empty at the end
            # rstrip() seems work better by treating all as whitespaces
            line = self.conn.read_until('\n').rstrip()
            if DEBUG is True:
                print ("  read:<" + line + ">")
            if "for a list of commands" in line:
                print ("Done")
                isPrompt = True
            elif ").."
    

# main
myrpc1 = rpc3 ("192.168.10.150")
myrpc1.connect()
myrpc1.getStatus()
myrpc1.disconnect()
#myrpc2 = rpc3 ("192.168.100.150","mng")
#myrpc2.connect()
#myrpc3 = rpc3 ("192.168.100.150","ngm","ok")
#myrpc3.connect()
