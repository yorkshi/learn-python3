def factor_no_para():
		i=1
		nums=10
		print('%d的因数是:'%(nums))
		while i<=nums:
				if nums%i==0:
						print('%d'%(i))
				i+=1
#==============================自定义函数体结束，下面为调用自定义函数
factor_no_para()
tt=type(factor_no_para)
print(tt)
