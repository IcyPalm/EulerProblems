#!python3
previous = 1
current = 2
output = 0
while current < 4000000:
	if (current % 2) == 0:
		output += current
	temp = current
	current += previous
	previous = temp
print(output)