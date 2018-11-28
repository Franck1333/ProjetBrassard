from Tkinter import * #Python Version 2
import ttk

fenetre = Tk() 

#---PROGRESSBAR TTK---
#Aides: https://gist.github.com/kochie/9f0b60384ccc1ab434eb
ft = ttk.Frame()
ft.pack(expand=False, fill="both", side="top")
pb_hD = ttk.Progressbar(ft, orient='horizontal', mode='indeterminate')
pb_hD.pack(expand=False, fill="both", side="top")
pb_hD.start(7)
#---PROGRESSBAR TTK---

fenetre.mainloop()
