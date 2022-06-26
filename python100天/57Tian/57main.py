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
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('57index.html')


if __name__ == "__main__":
    app.run()
