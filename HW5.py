import re

with open("regex_sum_36347.txt") as f:
	file_contents = f.read()
list_of_nums = re.findall('[0-9]+', file_contents)
list_of_nums = list(map(int, list_of_nums))

y = 0
for x in list_of_nums:
    y = x + y
print (y)