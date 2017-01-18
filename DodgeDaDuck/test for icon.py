import Tkinter
from Tkinter import Tk
root = Tk()
img = Tkinter.Image("photo", file="duckie.gif")
root.tk.call('wm','iconphoto',root._w,img)
