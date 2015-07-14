import os

sudo = "sudo sysctl -w"
ctl_var = [" net.inet.tcp.win_scale_factor=4", " net.inet.tcp.sendspace=1048576", " net.inet.tcp.recvspace=1048576", " net.inet.tcp.mssdflt=1300"]

for i in ctl_var:
    os.system(sudo + i)
    if "=" in i:
        eq = i.index("=")
        print os.system("sysctl -a " + i[:eq:])


"""
DEFAULTS


net.inet.tcp.win_scale_factor=3
net.inet.tcp.sendspace=131072
net.inet.tcp.recvspace=131072
net.inet.tcp.mssdflt=512
net.inet.tcp.slowstart_flightsize=1
"""
