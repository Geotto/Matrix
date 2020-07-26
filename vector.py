#!/bin/env python
#!-*- encoding: UTF-8 -*-
from __future__ import print_function

class Vector:	
	def __init__(self, size):
		if size < 0:
			raise Exception("size must great than or equals to 0");

		self.__size = size
		self.__data = []
		for i in range(0, size):
			self.__data.append(0.0)

	def set(self, index, value):
		if index < 0 or index >= self.__size:
			raise Exception("invalid index")

		self.__data[index] = value;

	def get(self, index):
		return self.__data[index]

	def size(self):
		return self.__size

	def printMe(self):
		output = ''
		skip =  True
		output += '('
		for i in range(0, self.__size):
			if skip:
				skip = False
			else:
				output +=", "
			output += str(self.__data[i])

		output += ')'
		print(output)

	# 转化为列表类型
	def toList(vector):
		result = [];
		for i in range(0, vector.size()):
			result[i] = vector.get(i);

		return result

	# 从列表生成
	def fromList(list):
		vector = Vector(len(list))
		for i in range(0, len(list)):
			vector.set(i, list[i])

		return vector

if __name__ == '__main___':
	vector = Vector(0)
	vector.printMe()
	print(vector.size())

	vector = Vector(1)
	vector.set(0, 1)
	vector.printMe()
	print(vector.size())

	vector = Vector(2)
	vector.set(0, 1)
	vector.set(1, 2)
	vector.printMe()
	print(vector.size())

	vector = Vector.fromList([1, 2, 3])
	vector.printMe();
	print(vector.get(0))
	print(vector.get(1))
	print(vector.get(2))