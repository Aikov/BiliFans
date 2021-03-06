import _thread as thread
import tkinter as tk

from tools import *

uid_test = 1473830  # Test Uid
InputWindow = tk.Tk()  # I finish this window after below one
InputWindow.title('Input')
InputWindow.geometry('500x200')  # InputWindow use the same config with main Window
InputWindow.configure(bg='violet')
la = tk.Label(InputWindow, bg='green', text='Input The UID', fg='black', width=20, height=2,
              font=('Arial', 14))
la.place(x=130, y=20)
entry = tk.Entry(InputWindow, bg='white')  # In fact I want them to look same
entry.place(x=175, y=75)


def input_hit_me_1():  # get the value for uid
    global uid
    uid = entry.get()
    InputWindow.destroy()


def input_hit_me_2():
    file.close()
    error_log.close()
    exit()


Ibutton_1 = tk.Button(InputWindow, text='Confirm', font=('Arial', 18), width=10, height=1, command=input_hit_me_1,
                      bg='#2d32ff')
Ibutton_1.place(x=80, y=120)
Ibutton_2 = tk.Button(InputWindow, text='Exit', font=('Arial', 18), width=10, height=1, command=input_hit_me_2,
                      bg='#f64141')
Ibutton_2.place(x=270, y=120)
InputWindow.mainloop()
window = tk.Tk()  # This is the window I finish first
window.title(get_name(uid))

window.geometry('500x200')
window.configure(background='violet')
string = tk.StringVar()
l_head = tk.Label(window, bg='violet', width=200, height=1)
l_head.pack()
l = tk.Label(window, textvariable=string, bg='green', fg='pink', font=('Arial', 18), width=20, height=2)
l.pack()


def hit_me_1():
    a = get_fans(uid)
    if a[2]:
        string.set(a[1])
        window.after(1000, hit_me_1, )
    else:
        string.set('Error,Check the log file.')


def hit_me_2():
    file.close()
    error_log.close()
    exit()


b1 = tk.Button(window, text='Update', font=('Arial', 18), width=10, height=1, command=hit_me_1, bg='#2d32ff')
b1.place(x=80, y=100)
b2 = tk.Button(window, text='Exit', font=('Arial', 18), width=10, height=1, command=hit_me_2, bg='#f64141')
b2.place(x=270, y=100)
thread.start_new_thread(log_fans, (uid, get_name(uid)))
# I change this value, first uid_test to_uid, second I add param 'name' to func 'log_fans'
window.mainloop()
# TODO：粉丝数量异常变化的分析和记录
