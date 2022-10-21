from classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed()
    zenbed.off()
    zenbed.status()
    return 0

stop()