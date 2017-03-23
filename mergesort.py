def mergesort(a):
	if(len(a) <= 1):
		return a
	else:
		left = a[0:len(a)/2]
		right = a[len(a)/2:len(a)]
		left = mergesort(left)
		right = mergesort(right)
		return merge(left,right)
def merge(b, c):
	result = []
	l = b[:]
	e = c[:]
	i = 0
	j = 0
	while(len(l) != i or len(e) != j):
		if(i == len(l)):
			result += e[j:]
			break
		elif(j == len(e)):
			result += l[i:]
			break
		elif(l[i] > e[j]):
			result.append(e[j])
			j+=1
		else:
			result.append(l[i])
			i+=1
	return result
nums = [1,22,3,34,55,2,11,233,44,12]
print(mergesort(nums))
