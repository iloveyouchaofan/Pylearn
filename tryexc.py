#tryexc.py

'''
1、内置错误
	官方文档，标准库第5节
2、错误处理
	try
	except
	finaly
3、错误捕获
	首先要预判可能出现的错误类型
		解释器层面是如何实现的？
	自定义错误类型呢？
'''

try:
	if True:
		raise LALAEr #制造一个错误！LALAEr不存在！
		'''
			抛出错误的信息分两个部分：
			1、错误类型：NameError
			2、错误描述：name 'e' is not defined
			合起来就是完整的错误信息：
			NameError: name 'e' is not defined

			其实，
			错误类型是一个类
			as e 是把这个类实例化了
			因此，e也就包含其中的内容了！
		'''
except NameError as e:
	print('e的是什么？：', type(e))
	print('Catch an Eorro', e)
	'''
	一条语句匹配多条错误类型
		用()包含起来
	多个except
	'''

print('lala') #except不过后继续执行该语句！


#疑问
'''
	1、如何抛出错误？
		如何自定义错误？
		return 是不是只返回一个信息？内容是错误的信息？
	2、如何捕获错误？

'''