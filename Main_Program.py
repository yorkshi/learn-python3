class Box1():
		'''求立方体的类'''
		def __init__(self,length1,width1,height1):
				self.length=length1
				self.width=width1
				self.height=height1
		def volume(self):
				return self.length*self.width*self.height
#======================================================
class Box2(Box1):
		def __init__(self,length1,width1,height1):
				super().__init__(length1,width1,height1)
				self.color='white'
				self.material='paper'
				self.type='fish'
		def area(self):
				re=self.length*self.width+self.length*self.height+self.width*self.height
				return re*2
class SHost():
		name='TOM'
		age=20
		address='china'
		call='28380000'