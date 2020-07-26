#!/bin/env python
#!-*- encoding: UTF-8 -*-

import sys
import math
from vector import Vector

class Matrix:
	def __init__(self, rows):
		if rows < 0:
			raise Exception("rows must great than or equals to 0")

		self.__rows = rows
		self.__cols = []

	def add(self, vector):
		if  isinstance(vector, Vector) == False:
			raise Exception("argument must be a vector")
		if vector.size() != self.__rows:
			raise Exception("invalid vector size")

		self.__cols.append(vector)

	# 设置元素值
	def set(self, row, col, value):
		if self.__rows <= row or row < 0:
			raise Exception("argument row is invalid")
		if len(self.__cols) <= col or col < 0:
			raise Exception("argument col is invalid")
		self.__cols[col].set(row, value)

	# 获取元素值
	def get(self, row, col):
		if self.__rows <= row or row < 0:
			raise Exception("argument row is invalid")
		if len(self.__cols) <= col or col < 0:
			raise Exception("argument col is invalid")
		return self.__cols[col].get(row)

	# 打印矩阵
	def printMe(self):
		for row in range(0, self.__rows):
			for col in range(0, len(self.__cols)):
				print("%12.4f" % (self.__cols[col].get(row)), end='')
				if col < len(self.__cols) - 1:
					print(' ', end='')
			print()

	# 矩阵乘法
	def multiple(self, vector):
		if vector.size() != len(self.__cols):
			raise Exception("illegal vector size")

		result = Vector(self.__rows)
		for row in range(0, self.__rows):
			s = 0.0
			for col in range(0, len(self.__cols)):
				s += vector.get(col) * self.__cols[col].get(row)

			result.set(row, s)

		return result

	# 转为简化阶梯型
	def simplify(self, printOut=False):
		# 复制矩阵
		result = Matrix(self.__rows)
		for col in range(0, len(self.__cols)):
			vector = Vector(self.__rows)
			for row in range(0, self.__cols[col].size()):
				vector.set(row, self.get(row, col))
			result.add(vector)

		dstRow = 0
		for col in range(0, len(result.__cols)):
			if dstRow >= result.__rows:
				break;
			
			# 查找绝对值最小的行
			minRow = -1
			minRowValue = sys.maxsize
			for row in range(dstRow, result.__rows):
				if result.__cols[col].get(row) != 0.0 and abs(result.__cols[col].get(row)) < minRowValue :
					minRow = row
					minRowValue = abs(result.__cols[col].get(row))

			if(minRow == -1):
				continue

			for row in range(0, result.__rows):
				if row == minRow:
					continue

				if result.__cols[col].get(row) == 0:
					continue

				weight = - result.__cols[col].get(row) / result.__cols[col].get(minRow)
				for index in range(0, len(result.__cols)): # 优化：从col开始
					value = result.__cols[index].get(minRow) * weight + result.__cols[index].get(row);
					result.set(row, index, value)

			# 重排
			if minRow != -1:
				if minRow != dstRow:
					tmpList = []
					for i in range(0, len(result.__cols)):
						tmp = result.__cols[i].get(minRow)
						result.__cols[i].set(minRow, result.__cols[i].get(dstRow))
						result.__cols[i].set(dstRow, tmp)
				dstRow += 1

			if printOut:
				result.printMe()
				for i in range(0, len(result.__cols) * 13):
					print("*", end='')
				print()

		# 归一化
		for row in range(0, result.__rows):
			# 查找第一个非零列
			weight =  0.0
			for col in range(0, len(result.__cols)):
				if weight == 0.0 and result.__cols[col].get(row) != 0.0:
					weight = 1.0 / result.__cols[col].get(row)
				
				if weight != 0.0:
					result.__cols[col].set(row, result.__cols[col].get(row) * weight)

		return result

	def create(cols):
		if len(cols) == 0:
			return Matrix(0)
		
		matrix = Matrix(len(cols[0]))
		for col in cols:
			vector = Vector.fromList(col)
			matrix.add(vector)
		
		return matrix

if __name__ == '__main__':
	""" matrix = Matrix(0)
	matrix.printMe()

	matrix = Matrix(1)
	matrix.printMe()
	matrix.add(Vector.fromList([1]))
	matrix.printMe()
	matrix.add(Vector.fromList([2]))
	matrix.printMe()
	matrix.set(0, 1, 3)
	matrix.printMe()

	matrix = Matrix(3)
	matrix.add(Vector.fromList([1, 2, 3]))
	matrix.add(Vector.fromList([2, 3, 4]))
	vector = Vector.fromList([1, 2]);
	result = matrix.multiple(vector);
	result.printMe()

	m = matrix.simplify()
	m.printMe() """

	""" matrix = Matrix(4)
	matrix.add(Vector.fromList([0, -1, -2, 1]))
	matrix.add(Vector.fromList([-3, -2, -3, 4]))
	matrix.add(Vector.fromList([-6, -1, 0, 5]))
	matrix.add(Vector.fromList([4, 3, 3, -9]))
	matrix.add(Vector.fromList([9, 1, -1, -7]))
	m = matrix.simplify();
	m.printMe() """

	print()

	matrix = Matrix(3)
	matrix.add(Vector.fromList([0, 3, 3]))
	matrix.add(Vector.fromList([3, -7, -9]))
	matrix.add(Vector.fromList([-6, 8, 12]))
	matrix.add(Vector.fromList([6, -5, -9]))
	matrix.add(Vector.fromList([4, 8, 6]))
	matrix.add(Vector.fromList([-5, 9, 15]))
	m = matrix.simplify(printOut=True)
	m.printMe()