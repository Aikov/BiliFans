import csv
import time

import requests

uid = 1473830  # Test Uid
file = open('data.csv', 'a', newline='')
writer = csv.writer(file)
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


def log_fans(uid):
    count = 0
    while True:
        a = get_fans(uid)
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
