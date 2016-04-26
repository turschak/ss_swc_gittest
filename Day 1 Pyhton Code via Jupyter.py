###Example Python Code

print("hello world")

#load numpy library
import numpy
data=numpy.loadtxt(fname='inflammation-01.csv',delimiter=',')
type(data)
data.mean()
data.std()
data.mean(axis=0)


#load library and rename it
import matplotlib.pyplot as plt
#allows plots to show up in jupyter window
%matplotlib inline

#plot columnwise averages
avg_inflammation = data.mean(axis = 0)
avg_plot = plt.plot(avg_inflammation)

#plot columnwise std
std_inflammation = data.std(axis = 0)
avg_plot = plt.plot(std_inflammation)

################################################
#Exercise 1

#load numpy library
import numpy
data=numpy.loadtxt(fname='inflammation-01.csv',delimiter=',')
#load library and rename it
import matplotlib.pyplot as plt
#allows plots to show up in jupyter window
%matplotlib inline
#plot columnwise averages
avg_inflammation = data.mean(axis = 0)
avg_plot = plt.plot(avg_inflammation)
#plot columnwise std
std_inflammation = data.std(axis = 0)
avg_plot = plt.plot(std_inflammation)


#plot avg, min, max in line
avg_inflammation = data.mean(axis = 0)
min_inflammation = data.min(axis = 0)
max_inflammation = data.max(axis = 0)

fig = plt.figure(figsize=(10.0,3.0))
axes1 = fig.add_subplot(1,3,1)
axes2 = fig.add_subplot(1,3,2)
axes3 = fig.add_subplot(1,3,3)

axes1.set_ylabel('average')
axes1.plot(avg_inflammation)

axes2.set_ylabel('minimum')
axes2.plot(min_inflammation)

axes3.set_ylabel('maximum')
axes3.plot(max_inflammation)

plt.show()

###################################################
odds=[1,3,5,7]
print(odds)

odds.append(9)
print(odds)

names=["Hopper","Turing"]
print(names)

element='helium'
print(element)
type(element)

odds[2]
print(odds)

#indexing examples
element[2]
element='oxygen'
element[:4]
element[4:]
element[:]
element[-1]
element[1:-1]

####################################################

word='lead'
for character in word:
	print(character)
print(word)

length = 0
for num in odds:
		length = length + 1
print(length)		

#make a character list from word
word='hello'
my_list=[]
for letter in word:
	my_list.append(letter)
print(my_list)	

#add 1 to odds	
odds2=[]
for characters in odds:
	odds2.append(characters + 1)
print(odds2)	

###################################################

#import libraries
import numpy
import matplotlib.pyplot as plt
%matplotlib inline
import glob

#load file list
file_name_list=glob.glob("inflammation-*.csv")
print(file_name_list)

#run loop for 1st 3 files
for filename in file_name_list[0:3]:
	data=numpy.loadtxt(fname=filename,delimiter=',')
	#plot columnwise averages
	avg_inflammation = data.mean(axis = 0)
	#avg_plot = plt.plot(avg_inflammation)
	#plot columnwise std
	#std_inflammation = data.std(axis = 0)
	#avg_plot = plt.plot(std_inflammation)


	#plot avg, min, max in line
	avg_inflammation = data.mean(axis = 0)
	min_inflammation = data.min(axis = 0)
	max_inflammation = data.max(axis = 0)

	fig = plt.figure(figsize=(10.0,3.0))
	axes1 = fig.add_subplot(1,3,1)
	axes2 = fig.add_subplot(1,3,2)
	axes3 = fig.add_subplot(1,3,3)

	axes1.set_ylabel('average')
	axes1.plot(avg_inflammation)

	axes2.set_ylabel('minimum')
	axes2.plot(min_inflammation)

	axes3.set_ylabel('maximum')
	axes3.plot(max_inflammation)

	plt.show()
	
##################################################
#Writing Functions
def fahr_to_kelvin(temp):
	temp_k = ((temp-32)*(5/9)+273.15)
	return temp_k 

	
def fence(original,wrapper):
	output = (wrapper+original+wrapper)
	return(output)

print(fence('name','*'))


##################################################
#Create Function for loop
#import libraries
import numpy
import matplotlib.pyplot as plt
%matplotlib inline
import glob

#load file list
file_name_list=glob.glob("inflammation-*.csv")

def analyze(filename):	
	data=numpy.loadtxt(fname=filename,delimiter=',')
	#plot columnwise averages
	avg_inflammation = data.mean(axis = 0)
	#avg_plot = plt.plot(avg_inflammation)
	#plot columnwise std
	#std_inflammation = data.std(axis = 0)
	#avg_plot = plt.plot(std_inflammation)


	#plot avg, min, max in line
	avg_inflammation = data.mean(axis = 0)
	min_inflammation = data.min(axis = 0)
	max_inflammation = data.max(axis = 0)

	fig = plt.figure(figsize=(10.0,3.0))
	axes1 = fig.add_subplot(1,3,1)
	axes2 = fig.add_subplot(1,3,2)
	axes3 = fig.add_subplot(1,3,3)

	axes1.set_ylabel('average')
	axes1.plot(avg_inflammation)

	axes2.set_ylabel('minimum')
	axes2.plot(min_inflammation)

	axes3.set_ylabel('maximum')
	axes3.plot(max_inflammation)

	plt.show()
	
for filename in file_name_list[0:3]:
	analyze(filename)
	
#################################################
#Conditional Statements
temp=71
if temp<75:
	print("pants")
else:
	print("shorts")

if temp < 60:
	print("jacket")
else:
	print("no jacket")
	
temp = 85

if temp < 60:
	print("pants + jacket")
elif temp < 75:
	print ("pants, no jackets")
else:
	print("shorts, no jacket")
	
temp = 85
sky = 'rain'

if (temp < 60)|((temp <75) & (sky=="rain")):
	print("pants + jacket")
elif temp < 75:
	print ("pants, no jackets")
else:
	print("shorts, no jacket")
	