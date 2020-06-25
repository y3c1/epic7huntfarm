import win32api
import tkinter as tk


def updateXY():
    x, y = win32api.GetCursorPos()
    xlabel['text'] = "x: " + str(x)
    ylabel['text'] = "y: " + str(y)
    root.after(1, updateXY)

root = tk.Tk()

root.geometry("150x85")
root.resizable(0,0)
xlabel = tk.Label(text="x: 1111")
ylabel = tk.Label(text="y: 1111")
xlabel.config(font=("Arial", 24))
ylabel.config(font=("Arial", 24))
xlabel.pack()
ylabel.pack()

updateXY()
root.mainloop()