#三酷猫钓鱼记录查找，Python3.6.3版本下执行
fish_record='鲫鱼5条、鲤鱼8条、鲢鱼7条、草鱼2条、黑鱼6条、乌龟1只'
print(len(fish_record))
if fish_record[0:2]=='乌龟':
			print("是乌龟吗？是"+fish_record[0:2])
elif fish_record[5:7]=='乌龟':
			print("是乌龟吗？是"+fish_record[5:7])
elif fish_record[10:12]=='乌龟':
			print("是乌龟吗？是"+fish_record[10:12])
elif fish_record[15:17]=='乌龟':
			print("是乌龟吗？是"+fish_record[15:17])
elif fish_record[20:22]=='乌龟':
			print("是乌龟吗？是"+fish_record[20:22])
elif not fish_record[25:27]!='乌龟':
			if int(fish_record[27])/2==0:
					print("找到乌龟了，是%d只，偶数"%(int(fish_record[27])))
			else:
					print("找到乌龟了，是%d只，奇数"%(int(fish_record[27])))