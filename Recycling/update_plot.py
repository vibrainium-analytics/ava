import tkinter as tk

import numpy as np
import matplotlib.pyplot as pl
import matplotlib, sys

from tkinter import *

class MyApp()
    def __init__(self, *args, **kwargs)
    container = tk.Frame



app= MyApp()
app.mainloop()

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2*np.pi*t)
plt.plot(t, s)

plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('About as simple as it gets, folks')
plt.grid(True)
plt.savefig("test.png")
plt.show()
