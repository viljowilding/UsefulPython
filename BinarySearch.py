"""
Binary Search Algorithms
Viljo Wilding - December 2018
"""

import random, time

def randomList(length, min=0, max=10000):
	ls = []
	for i in range(length):
		ls.append(random.randint(min, max))
	ls.sort()
	return ls

def ibs(ls, value):
	low = 0
	high = len(ls) - 1
	while low <= high:
		mid = int((low + high) / 2)
		if(ls[mid] > value):
			high = mid - 1
		elif(ls[mid] < value):
			low = mid + 1
		else:
			return mid
	return None

def rbs(ls, value, low, high):
	if(high < low):
		return None
	mid = int((low + high) / 2)
	if(ls[mid] > value):
		return rbs(ls, value, low, mid-1)
	elif(ls[mid] < value):
		return rbs(ls, value, mid+1, high)
	else:
		return mid

def BinarySearch():
	global searchList, start, end
	searchList = []
	searchValue = ""
	search = False
	while len(searchList) == 0:
		print("Enter the ordered list of numbers that you wish to search.\n")
		sl = """global searchList
searchList = """ + input("List: ")
		try:
			exec(sl)
		except Exception as e:
			print("some sort of error just happened wew\nError: " + str(e))
			searchList = []
	while searchValue == "":
		print("Enter the value to search for.\n")
		sv = input("Value: ")
		searchValue = int(sv)
	while not search:
		print("Which method should be used?\n[I] Iterative\n[R] Recursive\n")
		st = input("Method: ").upper()
		if st == "I":
			search = True
			index = ibs(searchList, searchValue)
			print("{} can be found at searchList[{}].".format(searchValue, index))
		elif st == "R":
			search = True
			index = rbs(searchList, searchValue, 0, len(searchList)-1)
			print("{} can be found at searchList[{}].".format(searchValue, index))

if __name__ == "__main__":
	print("Here's a random list of numbers. You could use this by copy/pasting it below, or input your own list of numbers.\n{}\n".format(randomList(50)))
	BinarySearch()
