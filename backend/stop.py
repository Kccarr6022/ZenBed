from classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed(connected=True)
    zenbed.stop()
    zenbed.status()
    return 0

stop()