def isValidSubsequence(array, sequence):
    posA = 0
    posS = 0
    while posA < len(array) and posS < len(sequence):
        if array[posA] == sequence[posS]:
            posS+=1
        posA += 1
    return posS == len(sequence)