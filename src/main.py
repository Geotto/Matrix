from matrix import Matrix
from vector import Vector

matrix = Matrix(4)
matrix.add(Vector.fromList([7, -5, 6, -7]))
matrix.add(Vector.fromList([2, -3, 10, 9]))
matrix.add(Vector.fromList([-5, 4, -2, 2]))
matrix.add(Vector.fromList([8, -9, 7, 15]))
m = matrix.simplify()
# m.printMe()

matrix = Matrix(4)
matrix.add(Vector.fromList([12, -9, -6, 4]))
matrix.add(Vector.fromList([-7, 4, 11, -6]));
matrix.add(Vector.fromList([11, -8, -7, 10]))
matrix.add(Vector.fromList([-9, 7, 3, -5]))
matrix.add(Vector.fromList([5, -3, -9, 12]))
m = matrix.simplify()
# m.printMe()

matrix = Matrix(3)
matrix.add(Vector.fromList([0, 3, 3]))
matrix.add(Vector.fromList([3, -7, -9]))
matrix.add(Vector.fromList([-6, 8, 12]))
matrix.add(Vector.fromList([6, -5, -9]))
matrix.add(Vector.fromList([4, 8, 6]))
matrix.add(Vector.fromList([-5, 9, 15]))
m = matrix.simplify()
# m.printMe()

# Matrix.create([[1,3],[3,9],[4,7],[7,6]]).simplify().printMe()
# Matrix.create([[3, -9, -6],[-4, 12, 8],[2, -6, -4],[0, 0, 0]]).simplify().printMe()
