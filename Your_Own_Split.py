def mysplit(strng):
    listStrng = strng.split()
    return listStrng

case1 = "To be or not to be, that is the question"
case2 = "To be or not to be,that is the question"
case3 = "   "
case4 = " abc "
case5 = ""

answer_case1 = ['To', 'be', 'or', 'not', 'to', 'be,', 'that', 'is', 'the', 'question']
answer_case2 = ['To', 'be', 'or', 'not', 'to', 'be,that', 'is', 'the', 'question']
answer_case3 = []
answer_case4 = ['abc']
answer_case5 = []

print(mysplit(case1))
print(mysplit(case2))
print(mysplit(case3))
print(mysplit(case4))
print(mysplit(case5))

print(answer_case1 == mysplit(case1) )
print(answer_case2 == mysplit(case2) )
print(answer_case3 == mysplit(case3) )
print(answer_case4 == mysplit(case4) )
print(answer_case5 == mysplit(case5) )

