
#Youngho's First Python coding interview practice (GOOGLE)
#Question from: https://practice.geeksforgeeks.org/problems/find-the-frequency/1
#Difficulty: Easy

def findFreq(num, x):
    count = 0
    intList = list(map(int, num)) #split 1 2 3 4 -> 1,2,3,4 as an integer
    print(intList)
    for i in intList:
        count = intList.count(x)
    print(count)

findFreq("54221423",4)
        
    


