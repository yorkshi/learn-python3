def find_factor(nums):                     #带参数nums的求因数的自定义函数
		'''
		find_factor是自定义函数
		nums是传递一个正整数的参数
		以字符串形式返回一个正整数的所有因数'''      #用一对三个单引号来包括描述文档
		if type(nums)!=int:                    #不是整型，提示出错，并终止函数执行
				print('输入值类型出错，必须是整数！')   #提示传递值类型出错
				return                             #终止函数执行
		if nums<=0:                            #小于等于0的证书不在求因数范围之内
				print('输入值范围出错，必须正整数！')   #提示传输值范围出错
				return                             #终止函数执行
		i=1
		str1=''
		while i<=nums:                         #循环求nums传入值的因数
				if nums%i==0:                      #求传入值的因数
						str1=str1+''+str(i)
				i+=1
		return str1                            #返回因数
		
def say_ok():     #第二个自定义函数
		print('OK')