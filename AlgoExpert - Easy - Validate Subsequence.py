def isValidSubsequence(array, sequence):
	posSeq = 0
	for i in array:
			if posSeq == len(sequence):
					break
			if sequence[posSeq] == i:
					posSeq += 1
	return posSeq == len(sequence)