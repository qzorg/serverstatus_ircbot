import subprocess

def get_memusage():
    memfree = "Total/Free: " + subprocess.check_output("free -gh | cut -c15-39 | tail -n 2 | head -n 1", shell=True)
    return memfree
def get_cpuusage():
    cpuuse = subprocess.check_output("uptime | cut -c39-", shell=True)
    return cpuuse
def get_hddfull():
    hddfull = subprocess.check_output("df -k .", shell=True)
    return hddfull
def collect(command):
    
    if "mem" in command:
        return get_memusage()
    elif "cpu" in command:
        return get_cpuusage()
    elif "hdd" in command:
        return get_hddfull()
    else:
        return "not a command"


