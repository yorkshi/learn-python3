fish_records=['1月1日','鲫鱼',18,10.5,'1月1日','鲤鱼',8,6.2,'1月1日','鲢鱼',7,4.7,'1月2日','草鱼',2,7.2,'1月2日','鲫鱼',3,12,'1月2日','黑鱼',6,15,'1月3日','乌龟',1,71,'1月3日','鲫鱼',1,9.8]
stat_list=['1月1日','',0,0]
j=0
while j<len(fish_records):
    get_list=fish_records[j:j+4]
    if get_list[0]==stat_list[0]: #同一个日期统计
        if get_list[2]%2==0:      #能被2整除,是偶数
            stat_list[2]+=get_list[2] #统计当日的偶数累计数
        print(get_list)          #打印同日钓鱼记录
    else:
        print('%s,偶数累计为%d'%(stat_list[0],stat_list[2]))
        stat_list=get_list       #获取新日期的初始累计
        print(get_list)          #打印新同日第一条钓鱼记录
        stat_list[1]=''
        if get_list[2]%2!=0:
           stat_list[2]=0
    j+=4
print('%s,偶数累计为%d'%(stat_list[0],stat_list[2]))