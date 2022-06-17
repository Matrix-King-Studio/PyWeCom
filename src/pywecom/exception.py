# -*- coding: utf-8 -*-
# @Time        : 2022/6/17 5:49 PM
# @File        : exception.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
class WeComException(Exception):
	def __init__(self, errcode, errmsg):
		self.errcode = errcode
		self.errmsg = errmsg

	def __str__(self):
		return "WeComException Error {errcode}: {errmsg}".format(errcode=self.errcode, errmsg=self.errmsg)
