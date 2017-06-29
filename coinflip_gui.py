from tkinter import *
from tkinter import ttk
import time
from sys import *
from random import randint
        
def tosstime(*args):
    StartTime=0
    h=0
    t=0
    try:
        value = int(tossnum.get())
    except ValueError:
        exit

    StartTime=time.time()
    for i in range (value):
        x = randint(0, 99)
        if (x%2 == 0):
            h = h + 1 
        else:
            t = t + 1
    heads.set(h)
    tails.set(t)
    PercentHeads.set("{:.2f}%".format((h/value)*100))
    PercentTails.set("{:.2f}%".format((t/value)*100))
    Duration.set("{:.3f} seconds".format(time.time() - StartTime))

root = Tk()
root.title("COINFLIP SIMULATOR")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

tossnum = StringVar()
heads = StringVar()
tails = StringVar()
PercentHeads = StringVar()
PercentTails = StringVar()
Duration = StringVar()

tossnum_entry = ttk.Entry(mainframe, width=12, textvariable=tossnum)
tossnum_entry.grid(column=2, row=1, sticky=(W,E))

ttk.Label(mainframe, textvariable=heads).grid(column=2, row=2, sticky=(W, E))
ttk.Label(mainframe, textvariable=tails).grid(column=2, row=3, sticky=(W, E))
ttk.Label(mainframe, textvariable=PercentHeads).grid(column=2, row=4, sticky=(W, E))
ttk.Label(mainframe, textvariable=PercentTails).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=Duration).grid(column=2, row=6, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=tosstime).grid(column=1, row=1, sticky=E)

ttk.Label(mainframe, text="Coin Flips").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="Times landed on 'Heads':").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="Times landed on 'Tails':").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="Chance of getting 'Heads': ").grid(column=1, row=4, sticky=E)
ttk.Label(mainframe, text="Chance of getting 'Tails': ").grid(column=1, row=5, sticky=E)
ttk.Label(mainframe, text="Time it took to calculate: ").grid(column=1, row=6, sticky=E)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

tossnum_entry.focus()
root.bind('<Return>', tosstime)

root.mainloop()
