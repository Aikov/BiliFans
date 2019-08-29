import _thread as thread
import tkinter as tk

from tools import *

uid_test = 1473830  # Test Uid
window = tk.Tk()
window.title('AIChannel Fans')
window.geometry('500x200')
window.configure(background='violet')
string = tk.StringVar()
l_head = tk.Label(window, bg='violet', width=200, height=1)
l_head.pack()
l = tk.Label(window, textvariable=string, bg='green', fg='pink', font=('Arial', 18), width=20, height=2)
l.pack()

on_hit_1 = False
on_hit_2 = False


def hit_me_1():
    a = get_fans(uid_test)
    if a[2]:
        string.set(a[1])

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
thread.start_new_thread(log_fans, (uid_test,))  # TODO:Change this value after Finish input part
window.mainloop()
# TODO：一个视窗，用于让用户输入UID
# TODO：粉丝数量异常变化的分析和记录
