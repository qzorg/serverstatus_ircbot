import socket
import sys
import config
import re
from sysutils import collect

def get_help(text):
    output=["COMMAND USAGE: !servinfo [--a,$HOST]  --c[COMMAND,COMMAND,...]","COMMANDS availible: ", "mem   get memory info","cpu   get CPU info","hdd  get hdd info","kernel   get kernel version","uptime   get system uptime","ip  get ip address"]
    return output
def get_output(commandlets_list):
    output=[]
    for command in commandlets_list:
        collected = collect(command)
        output.append(collected)

    return output
def make_returnlist(commandlets):
    commandlets_list = commandlets.split(',')
    return commandlets_list
    
def contains_word(text, word):
   return bool(re.search(r'\b' + re.escape(word) + r'\b', text))
def remove_spaces(commandlets_list):
    temp = []
    for commandlet in commandlets_list:
        commandlet = commandlet.strip()
        
        temp.append(commandlet)
    return temp


def find_command(text):
    index = text.find('--c')
    if index > 0:
        commandlets=text[index+3:]
        commandlets_list = make_returnlist(commandlets)
        commandlets_list = remove_spaces(commandlets_list)
        output = get_output(commandlets_list)
        return output
    else:
        return 0

   
