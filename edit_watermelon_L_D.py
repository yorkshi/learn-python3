#在自定义函数内部修改直接传递的列表的元素，会影响函数外面的列表对象
def EditFrult(name,attributes):           #attributes将用于传递列表对象
		attributes[0]=attributes[0]*0.9       #打九折，修改列表元素
		return attributes                     #返回修改后的列表对象

#调用EditFruit函数如下		
attri_L=[21,'甜','圆形','绿色']            #21为价格
get_L=EditFrult('西瓜',attri_L)           #调用EditFruit，并返回修改后的列表
print(get_L)                             #打印返回的列表对象
print(attri_L)                           #打印原始列表对象