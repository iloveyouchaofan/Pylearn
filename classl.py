#classl.py
#coding:UTF-8
#Python 3.7.0?

class abc1(object):

	_a = None
	_b = None

	def __init__(self, d, e):
		self.d = d
		self.e = e
	'''
	1、
	__init__是一个特殊函数，用于给对象绑定属性。
		目前abc1中绑定了 d c 两个属性。
	注意：init 前后两个短下划线
	2、
	self可以理解为指向abc1，也就是指向自己。
		在构造类的时候，函数的第一个变量必须是self。
		不影响外调用。其他参数同函数。
	'''

#debug
f = abc1('str', 1)
print(f.d, f.e)