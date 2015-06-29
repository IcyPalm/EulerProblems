#!python3
v  = int(input('3 - 5 Multiple determinator : '))
output = 0
for i in range(1,v):
	if(i % 3) == 0:
		output += i
	elif(i % 5) == 0:
		output += i
print(output)