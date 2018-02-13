import subprocess

def get_memusage():
    memfree = "Total/Free: " + subprocess.check_output("free -gh | cut -c15-39 | tail -n 2 | head -n 1", shell=True)
    return memfree
def get_cpuusage():
    cpuuse = subprocess.check_output("uptime | cut -c39-", shell=True)
    return cpuuse
def get_hddfull():
    hddfull = "space used: " + subprocess.check_output("df / | awk 'END{print $5}'", shell=True)
    return hddfull
def get_kernelinfo():
    kernelv = subprocess.check_output("uname -a", shell=True)
    return kernelv
def get_uptime():
    uptime = subprocess.check_output("w | cut -c2-26 | head -n 1", shell=True)
    return uptime
def get_ipaddr():
    ip = subprocess.check_output("hostname -I", shell=True)
    return ip

def collect(command):
    options = {
        "mem": get_memusage(),
        "cpu": get_cpuusage(),
        "hdd": get_hddfull(),
        "kernel": get_kernelinfo(),
        "uptime": get_uptime(),
        "ip": get_ipaddr(),
    }

    return options.get(command, "no such command")

