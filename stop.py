from curses.textpad import rectangle
from classes.zenbedclass import Zenbed

def stop():
    zenbed = Zenbed()
    zenbed.pattern(rectangle)
    zenbed.off()
    zenbed.status()
    return 0

stop()