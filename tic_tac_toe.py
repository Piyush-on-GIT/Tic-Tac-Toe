from tkinter import *
from tkinter import font
from tkinter import messagebox

win = Tk()

win.title("TIC-TAC-TOE")
win.resizable(False, False)
win.configure(background="#f00f00")
sc_wd = win.winfo_screenmmwidth()
sc_ht = win.winfo_screenheight()
wd = win.winfo_reqwidth()
ht = win.winfo_reqheight()
x = sc_wd / 2 - wd / 2
y = sc_ht / 2 - ht / 2
win.update_idletasks()
win.geometry("%dx%d+%d+%d" % (wd + 262, ht + 214, x * 5.9, y - 200))
clicked = 0
fnt = font.Font(family="Consolas", size=16, weight="bold")


def checkforwin():
    if btn1["text"] == btn2["text"] == btn3["text"] == "X" or btn4["text"] == btn5["text"] == btn6["text"] == "X" \
            or btn7["text"] == btn8["text"] == btn9["text"] == "X" or btn1["text"] == btn4["text"] == btn7[
        "text"] == "X" \
            or btn2["text"] == btn5["text"] == btn8["text"] == "X" or btn3["text"] == btn6["text"] == btn9[
        "text"] == "X" \
            or btn1["text"] == btn5["text"] == btn9["text"] == "X" or btn3["text"] == btn5["text"] == btn7[
        "text"] == "X":
        messagebox.showinfo("TIC-TAC-TOE", "YOU WON!!!")
        win.destroy()

    elif btn1["text"] == btn2["text"] == btn3["text"] == "O" or btn4["text"] == btn5["text"] == btn6["text"] == "O" \
            or btn7["text"] == btn8["text"] == btn9["text"] == "O" or btn1["text"] == btn4["text"] == btn7[
        "text"] == "O" \
            or btn2["text"] == btn5["text"] == btn8["text"] == "O" or btn3["text"] == btn6["text"] == btn9[
        "text"] == "O" \
            or btn1["text"] == btn5["text"] == btn9["text"] == "O" or btn3["text"] == btn5["text"] == btn7[
        "text"] == "O":
        messagebox.showinfo("TIC-TAC-TOE", "YOU WON!!!")
        win.destroy()


def button(btn):
    global clicked
    if btn["text"] == "" and clicked == 0:
        btn["text"] = "X"
        clicked = 1
    elif btn["text"] == "" and clicked == 1:
        btn["text"] = "O"
        clicked = 0
    if (btn1["text"] and btn2["text"] and btn3["text"]) or (btn4["text"] and btn5["text"] and btn6["text"]) \
            or (btn7["text"] and btn8["text"] and btn9["text"]) or (btn1["text"] and btn4["text"] and btn7["text"]) \
            or (btn2["text"] and btn5["text"] and btn8["text"]) or (btn3["text"] and btn6["text"] and btn9["text"]) \
            or (btn1["text"] and btn5["text"] and btn9["text"]) or (btn3["text"] and btn5["text"] and btn7["text"]):
        checkforwin()


btn1 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn1))
btn1.grid(row=0, column=0)
btn2 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn2))
btn2.grid(row=0, column=1)
btn3 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn3))
btn3.grid(row=0, column=2)
btn4 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn4))
btn4.grid(row=1, column=0)
btn5 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn5))
btn5.grid(row=1, column=1)
btn6 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn6))
btn6.grid(row=1, column=2)
btn7 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn7))
btn7.grid(row=2, column=0)
btn8 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn8))
btn8.grid(row=2, column=1)
btn9 = Button(win, text="", font=fnt, width=12, height=5, bg="#00f0d0", activebackground="#00f0d0",
              command=lambda: button(btn9))
btn9.grid(row=2, column=2)
win.mainloop()
