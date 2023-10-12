import math

#(точка)
class Point:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

# Класс Vector (вектор)
class Vector:
	def __init__(self, start, end):
		self.start = start
		self.end = end
		self.dx = end.x - start.x
		self.dy = end.y - start.y
		self.dz = end.z - start.z

	def length(self):
		return math.sqrt(self.dx**2 + self.dy**2 + self.dz**2)

	def dot_product(self, other):
		return self.dx * other.dx + self.dy * other.dy + self.dz * other.dz

	def cross_product(self, other):
		cross_dx = self.dy * other.dz - self.dz * other.dy
		cross_dy = self.dz * other.dx - self.dx * other.dz
		cross_dz = self.dx * other.dy - self.dy * other.dx
		return Vector(Point(0, 0, 0), Point(cross_dx, cross_dy, cross_dz))

	def is_collinear(self, other):
		return self.cross_product(other).length() == 0

	def is_coplanar(self, other1, other2):
		cross_product = self.cross_product(other1)
		return cross_product.is_collinear(other2)

# Пример использования
point1 = Point(1, 2, 3)
point2 = Point(4, 5, 6)
point3 = Point(7, 8, 9)

vector1 = Vector(point1, point2)
vector2 = Vector(point2, point3)
vector3 = Vector(point1, point3)

length = vector1.length()#длина первого вектора
dot_product = vector1.dot_product(vector2)#скаляр
cross_product = vector1.cross_product(vector2)#в-рное произв
collinear_check = vector1.is_collinear(vector2)
coplanar_check = vector1.is_coplanar(vector2, vector3)

print("Длина вектора:", length)
print("Скалярное произведение векторов:", dot_product)
print("Векторное произведение векторов:", cross_product.dx, cross_product.dy, cross_product.dz)
print("Коллинеарность векторов:", collinear_check)
print("Компланарность векторов:", coplanar_check)
