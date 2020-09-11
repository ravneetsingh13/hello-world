def isPossible(s1,s2):
	count = [0]*58
	for ch in s2:
		count[ord(ch) - 97] += 1
	for ch in s1:
		if count[ord(ch)-97]==0:
			return 'Not Possible'
		count[ord(ch)-97] -= 1
	
	return 'Possible'
		
#Main
s1="GeeksforGeeks"
s2="rteksfoGrdsskGeggehes"
print(isPossible(s1,s2))