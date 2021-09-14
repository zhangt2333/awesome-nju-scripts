# -*- coding: utf-8 -*-
# !/usr/bin/env python
# Author-Github: github.com/zhangt2333
# spider.py 2021/9/13 14:00
# Credits: https://github.com/Super-Special-Pookies/Sleepy-Course-Selector. I fixed some bugs and refactor code from it.

import requests
import json
from time import sleep
import uniform_login_des
import config
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import time


def get_captcha():
    try:
        resp = requests.get("https://yjsxk.nju.edu.cn/yjsxkapp/sys/xsxkapp/login/4/vcode.do")
        if resp.status_code == 200:
            vtoken = json.loads(resp.text)['data']['token']
            resp = requests.get("https://yjsxk.nju.edu.cn/yjsxkapp/sys/xsxkapp/login/vcode/image.do?vtoken=" + vtoken)
            plt.imshow(Image.open(BytesIO(resp.content)))
            plt.axis('off')
            plt.show(block=False)
            captcha = input('Please input the captcha:')
            plt.close()
            return vtoken, captcha
    except Exception as e:
        print("Error: get captcha.", e)
        exit(-1)


def login(username, password):
    password = uniform_login_des.strEnc(password, "1", "2", "3")
    while True:   # 输入验证码直到正确
        vtoken, captcha = get_captcha()
        data = {
            'loginName': username,
            'loginPwd': password,
            'verifyCode': captcha,
            'vtoken': vtoken
        }
        try:
            response = requests.post(
                url='https://yjsxk.nju.edu.cn/yjsxkapp/sys/xsxkapp/login/check/login.do',
                data=data,
                headers=config.HEADERS
            )
            result = json.loads(response.text)
            if result["code"] == "1":
                return response.cookies
            print("Error: password don't match" if result["code"] == "2" else "Error: captcha don't match")
        except Exception as e:
            print("Error: login", e)
            exit(-1)


def get_csrfToken(cookies, sleep_time):
    while True:
        try:
            response = requests.get('https://yjsxk.nju.edu.cn/yjsxkapp/sys/xsxkapp/xsxkHome/loadPublicInfo_course.do', cookies=cookies)
            result = json.loads(response.text)
            if result.get('csrfToken'):
                return result.get('csrfToken')
            print(result.get('msg'))
        except Exception as e:
            pass
        sleep(sleep_time)


def choose(course_id, csrfToken, cookies):
    data = {
        'csrfToken': csrfToken,
        'lx': 2,
        'bjdm': course_id,
    }
    try:
        res = requests.post(
            url="https://yjsxk.nju.edu.cn/yjsxkapp/sys/xsxkapp/xsxkCourse/choiceCourse.do",
            headers=config.HEADERS,
            data=data,
            cookies=cookies
        )
        result = json.loads(res.text)
        if result["code"] == 1:
            print("Info: success", config.courses.get(course_id))
            return True
        print("Info: failed", config.courses.get(course_id), result['msg'])
    except Exception as e:
        print(e)
        pass
    return False


def main(username, password, sleep_time):
    # 登录
    cookies = login(username, password)
    # 等待选课开始
    csrfToken = get_csrfToken(cookies, sleep_time)
    # 开始选课
    chosen = set()
    while len(config.courses) != len(chosen):
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        for k, v in config.courses.items():
            if k not in chosen and choose(k, csrfToken, cookies):
                chosen.add(k)
        sleep(sleep_time)
