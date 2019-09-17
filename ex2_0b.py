class triangle:
	def __init__(self,angle1,angle2,angle3):
		self.angle1=angle1
		self.angle2=angle2
		self.angle3=angle3
	
	no_of_sides=3

	def check_angles(self):
		if self.angle1+self.angle2+self.angle3 ==180:
			return 1
		else:
			return 0 

	
my_triangle=triangle(30,60,80)
print(my_triangle.no_of_sides)
print(my_triangle.check_angles())


	
	
