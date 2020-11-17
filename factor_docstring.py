def find_factor(nums):
		'''
		find_factor是自定义函数
		nums是传递一个正整数的参数
		以字符串形式返回一个正整数的所有因数'''
		i=1
		str1=''
		while i<=nums:
				if nums%i==0:
						str1=str1+''+str(i)
				i+=1
		return str1
help(find_factor)
