from sys import stdin


def maximum_gold(capacity, weights):
    testArray = []
    weightsTest = []
    for w in range(0,len(weights)): 
        weightsTest.append(0)
    for i in range(0,capacity+1):
        testArray.append(0)
    for i in range(0, len(testArray)):
        for w in weights: 
            if w <= i:
                if testArray[i-w]+w>=testArray[i]and weightsTest[weights.index(w)]==0:
                    testArray[i]=testArray[i-w]+w
                    weightsTest[weights.index(w)]=1
                    if weights.index(w)>0:
                        for i in range(0, weights.index(w)):
                            weightsTest[i]=0
            else:
                continue
    return testArray[capacity]

capacity = 10 
weights = [1,4,8]

print(maximum_gold(capacity, weights))


"""
if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
"""