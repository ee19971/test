#!/usr/bin/env python3
# -*- coding = utf-8 -*-
"""
@FileName文件名:57main.py
@Python version: 3.10.5
@Description描述：
@Author作者：ee19971
@Time时间：2022/6/26 15:12:47
@Department部门：
@My Website我的网站：
@Software软件: PyCharm
@Copyright版权声明：转载请注明出处
"""
# 用法：无
# Section 导入包
from flask import Flask, render_template
import random
import datetime
import requests

# Section 固定变量
app = Flask(__name__)


# Section 根目录
@app.route('/')
def home() -> str:
    """
    网页的根目录
    :return 网页
    """
    num = random.randint(1, 5)
    nian = datetime.datetime.now().year
    return render_template('57index.html', numw=num, nian_fen=nian)


@app.route('/guess/<string:name>')
def guess(name) -> str:
    """
    输入名字猜年龄和性别
    :param name: 网页上写的名字
    :return: 获取的年龄和性别
    """
    url1 = f'https://api.agify.io/?name={name}'  # 猜年龄api
    nian_lin = requests.get(url=url1, )
    nian_lin = nian_lin.json()['age']

    url2 = f'https://api.genderize.io/?name={name}'  # 猜性别api
    sex = requests.get(url=url2)
    sex = sex.json()
    sex = sex['gender']
    return render_template('guess.html', NAME=name, AGE=nian_lin, SEX=sex)


@app.route('/blog')
def get_blog():
    blog_url = 'https://api.npoint.io/90feb61cbf4d59de0133'
    response = requests.get(url=blog_url)
    all_w = response.json()
    return render_template('blog.html', posts=all_w)


# Section 开始
if __name__ == "__main__":
    app.run()
