from backend.classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed()
    zenbed.stop()
    zenbed.status()

stop()