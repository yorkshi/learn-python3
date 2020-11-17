def find_factor(nums):
		i=1
		str1=''
		while i<nums:
				if nums%i==0:
						str1=str1+''+str(i)
						i+=1
				return str1

num2_L=[10,15,18,25]
i=0
num_len=len(num2_L)
return_str=''
while i<num_len:
		return_str=find_factor(num2_L[i])
		print('%d的因数是:%s'%(num2_L[i],return_str))
		i+=1
		
