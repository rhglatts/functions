#Rebecca Glatts
#Lab 4

#Task 1.1
def  prob1 () :
    for i in range (4) :
        print(i, end = ' ' )
print(prob1())
"""
Output:
0 1 2 3 None
"""

#Task 1.2
def fun (x = 1, y = 2):
    x = x + y
    y += 1
    return x*y


print(fun(3, 2))
fun(3, )
fun(x=3, y=2)
fun(3,2)
a = fun(3, 2)


"""
Output:
15

"""


#Task 2
test_score = int(input("What test score did you get? "))
def score (test_score):
    if test_score >= 0 and test_score < 60:
        grade = "F"
    elif test_score >= 60 and test_score < 70:
        grade = "D"
    elif test_score >= 70 and test_score < 80:
        grade = "C"
    elif test_score >= 80 and test_score < 90:
        grade = "B"
    elif test_score >= 90 and test_score <= 100:
        grade = "A"
    else:
        grade = "Invalid score"
    return grade

print(score(test_score))

"""
Output:
What test score did you get? 100
A

What test score did you get? 63
D

What test score did you get? 104
Invalid score

What test score did you get? 89
B

What test score did you get? 75
C

What test score did you get? -2
Invalid score

What test score did you get? 17
F

"""