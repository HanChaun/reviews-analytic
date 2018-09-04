data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('Toatl:', len(data))

sum_len = 0

for d in data:
	sum_len += len(d)

print('Average length', sum_len/len(data))


new = []

for d in data:
	if len(d) < 100:
		new.append(d)
print('Total', len(new), 'leave message length is less than 100')
print(new[0])
print(new[1])