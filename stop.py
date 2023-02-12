from classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed()
    zenbed.stop()
    zenbed.status()
    return 0

stop()