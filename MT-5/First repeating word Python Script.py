a = raw_input()							# input string
charcount = [0 for i in range(127)]		# charcount[i] = a.count(i)
for i in a:								# where i = ASCII value
	charcount[ord(i)] += 1
maxcount = 0
res = ''
for i in a:								
	if charcount[ord(i)] > maxcount:	# Use > to get the first
		res = i 						# maxima, >= to get last
		maxcount = charcount[ord(i)]	# maxima. Since, we need
print res								# first, use '>'