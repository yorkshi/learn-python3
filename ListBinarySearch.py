fish_records=[1,1,2,3,6,7,8,18]              #排序后的钓鱼数量记录
low=0                                        #查找范围下界
high=len(fish_records)-1                     #查找范围上界 
find_value=7                                 #要寻找的值，可以灵活调整
find_OK=False                                #是否找到标志，TTrue为找到
i=1                                          #统计在列表里的查找次数
while low<=high:
		middle=int((low+high)/2)                 #用int取整数，避免浮点数问题的发生
		if find_value==fish_records[middle]:     #找到时
					find_OK=True                       #设置找到标志为True
					break
		elif find_value>fish_records[middle]:    #没有找到，要找的值范围大于中位值时
					low=middle+1                       #范围在middle+1和high之间
		elif find_value<fish_records[middle]:    #没有找到，要找的值范围小于中位值时
					high=middle-1                      #范围在low和middle-1之间
		i+=1                                     #统计列表里的查找次数
if find_OK:                                  #判断是否找到，并打印相应结果
			print('%d在列表下标%d处，找了%d次。'%(find_value,middle,i))
else:
			print('要找的数%d没有！找了%d次。'%(find_value,i))
