#三酷猫钓鱼记录查找
fish_record='鲫鱼5条、鲤鱼8条、鲢鱼7条、草鱼2条、黑鱼6条、乌龟1只'
print(len(fish_record))
record_len=len(fish_record)
i=0
while i<record_len:       #从字符串最左下标0开始，以5为间隔，循环查找是否存在乌龟记录
			if fish_record[i:i+2]=='乌龟':
						if int(fish_record[i+2])/2==0:
									print("找到乌龟了，是%d只，偶数"%(int(fish_record[i+2])))
						else:
									print("找到乌龟了，是%d只，奇数"%(int(fish_record[i+2])))
			i+=5
