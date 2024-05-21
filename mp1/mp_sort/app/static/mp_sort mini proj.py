from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):
	numbers = list(range(number))
	random.seed(seed)
	random.shuffle(numbers)
	return numbers

def generate():
	number = 10
	seed = 200
	array = gen_random_int(number,seed)
	# call gen_random_int() with the given number and seed
	# store it to the variable array
	

	array_str = ','.join(map(str, array)) + '.'
	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	document.getElementById("generate").innerHTML = array_str
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	return array_str


def sortnumber1(array_str):
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	array_str = document.getElementById("generate").innerHTML 
	n = len(array_str)
	array_ls = list(map(int, array_str.split(',')))
	swapped = True
	while swapped:
		swapped = False
		for i in range(1, n):
			if array_ls[i-1] > array_ls[i]:
				array_ls[i-1], array_ls[i] = array_ls[i], array_ls[i-1]
				swapped = True
	array_str = ','.join(map(str, array_ls)) + '.'
	document.getElementById("sorted").innerHTML = array_str
	return array_str



def sortnumber2():
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
	

	else:
		array_ls = list(map(int, value.split(',')))
		n = len(array_ls)
		swapped = True
		while swapped:
			swapped = False
			for i in range(1, n):
				if array_ls[i-1] > array_ls[i]:
					array_ls[i-1], array_ls[i] = array_ls[i], array_ls[i-1]
					swapped = True
		array_str = ','.join(map(str, array_ls)) + '.'
	print(array_str)	
	document.getElementById("sorted").innerHTML = array_str
	return array_str


