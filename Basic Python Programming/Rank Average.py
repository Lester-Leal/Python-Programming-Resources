# Rank Average // Emulate excel's RANK.AVG function
# Author: Jorn Blaedel Garbosa

grades=[]
for g in range(5):
	print('Input grade of {0}: '.format(g+1), end=' ')
	grades.append(float(input()))
grades.sort(reverse=True)

counts=[]
for i in range(len(grades)):
	counts.append(grades.count(grades[i]))
	
prev=grades[0]
sums=[]
sum=1
for i in range(1,len(grades)):
	if prev!=grades[i]:
		sums.append(sum)
		prev=grades[i]
		sum=i+1
	else:
		sum+=i+1
sums.append(sum)

j=0
ranks=[]
ranks.append(sums[0]/counts[0])
prev=grades[0]
for i in range(1,len(grades)):
	if prev!=grades[i]:
		prev=grades[i]
		j+=1
	ranks.append(sums[j]/counts[i])
		
for i in range(len(grades)):
	print('Person with grade {0} is in Rank {1}'.format(grades[i],ranks[i]))

