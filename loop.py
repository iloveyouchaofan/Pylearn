#循环语句测试
'''
4、循环测试
	break
		必须在循环内
		if 是条件语句
		跳出当前一层的循环
		无法跳出上上一层的循环。
		同样，continue也只是略过当前循环的语句！
	continue
		循环内
		continue 从头开始，略过后边的语句。
	return
		必须在函数内
		也就是说，执行到这个语句，函数就有结果了！
'''

while True:
	for x in [1,2,3,4]:
		if True:
			print('if end', x)
			break #再次输入测试的
		print('for end', x)
	print('while end')