import _thread as thread
import csv
import time
import tkinter as tk

import requests

error_log = open('Error.csv', 'a', newline='')
eWriter = csv.writer(error_log)


def log_error(info):
    eWriter.writerow(info)


def get_fans(uid) -> tuple:
    now_time = time.asctime(time.localtime(time.time()))
    try:
        url = 'https://api.bilibili.com/x/relation/stat'
        params = {'vmid': uid}
        body = requests.get(url=url, params=params)
        body = body.json()
        return now_time, body["data"]["follower"], True
    except Exception as e:
        return now_time, e, False


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
    a = get_fans(1473830)
    if a[2]:
        string.set(a[1])

    else:
        data = [a[0], a[1]]
        log_error(data)
        string.set('Error,Check the log file.')


file = open('data.csv', 'a', newline='')
writer = csv.writer(file)


def log_fans():
    count = 0
    while True:
        a = get_fans(1473830)
        if a[2]:
            write_data = [a[0], a[1]]
            writer.writerow(write_data)
            time.sleep(5)
            count = count + 1
            if count % 10 == 0:
                write_text = ['-------Fuck you Active 8-------']
                writer.writerow(write_text)
        else:
            write_data = [a[0], a[1]]
            log_error(write_data)


def hit_me_2():
    file.close()
    error_log.close()
    exit()


b1 = tk.Button(window, text='Update', font=('Arial', 18), width=10, height=1, command=hit_me_1, bg='#2d32ff')
b1.place(x=80, y=100)
b2 = tk.Button(window, text='Exit', font=('Arial', 18), width=10, height=1, command=hit_me_2, bg='#f64141')
b2.place(x=270, y=100)
thread.start_new_thread(log_fans, ())
window.mainloop()
