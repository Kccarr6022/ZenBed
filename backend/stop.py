from backend.classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed(connected=True)
    zenbed.stop()
    zenbed.status()

stop()