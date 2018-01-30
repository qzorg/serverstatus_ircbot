import socket
import sys
import config
from util import *
import re

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defines the socket
print "connecting to:"+ config.botconf['server']
irc.connect((config.botconf['server'], int(config.botconf['port'])))                                                         #connects to the server
irc.send("USER "+ config.botconf['botnick'] +" "+ config.botconf['botnick']+" "+ config.botconf['botnick'] +" :This is a fun bot!\n") #user authentication
irc.send("NICK "+ config.botconf['botnick'] + "\n")                            #sets nick
#irc.send("PRIVMSG nickserv :iNOOPE\r\n")    #auth
irc.send("JOIN "+ config.botconf['channel'] +"\n")        #join the chan

def sendmsg(msg):
    irc.send('PRIVMSG '+ config.botconf['channel'] +' :' + str(msg) + '\r\n')
 


while 1:    #puts it in a loop
    text=irc.recv(2040)  #receive the text
    print text   #print text to console

    if text.find('PING') != -1:                          #check if 'PING' is found
        irc.send('PONG ' + text.split() [1] + '\r\n') #returnes 'PONG' back to the server (prevents pinging out!)
    if "PRIVMSG" in text and config.botconf['channel'] in text and ":!servinfo" in text:
        if contains_word(text, config.botconf['botnick']) or text.find(".all") != -1:
            output = find_command(text)
            for msg in output:
                sendmsg(msg)
        elif text.find(".help") != -1:
            output = get_help(text)
            for msg in output:
                sendmsg(msg)
        
       
    else:
        pass


