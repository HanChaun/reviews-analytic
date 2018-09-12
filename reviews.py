
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

good = []
for d in data:
	if 'good' in d:
		good.append(d) 
print('Total', len(good))

good = [d for d in data if 'good' in d]

print(good)


wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] +=1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 1000000:
		print(word,wc[word])

while True:
	word = input('Please input words: ')
	if word == 'q':
		break
	if word in wc:	
		print(word ,'times', wc[word])
	else:
		print('404 NOTFOUND')
print('Thank you')











# sum_len = 0

# for d in data:
# 	sum_len += len(d)

# print('Average length', sum_len/len(data))

# new = []

# for d in data:
# 	if len(d) < 100:
# 		new.append(d)
# print('Total', len(new), 'leave message length is less than 100')
# print(new[0])
# print(new[1])

# good = []
# for d in data:
# 	if 'good' in d:
# 		good.append(d) 
# print('Total', len(good))

# good = [d for d in data if 'good' in d]

# print(good)

# bad = ['bad' in d for d in data]

# print(bad)



