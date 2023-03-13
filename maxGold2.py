from sys import stdin


def maximum_gold(capacity, weights):
    twoDimList =  [[0 for c in range(0,capacity+1)] for i in range(0,len(weights)+1)]
    for v in range(1, len(weights)+1): 
        for c in range(0,capacity +1):
            twoDimList[v][c]= twoDimList[v-1][c]
            if weights[v-1]<= c:
                val = twoDimList[v-1][c-weights[v-1]]+weights[v-1]
                if twoDimList[v][c]< val:
                    twoDimList[v][c]= val
    return twoDimList[len(weights)][capacity]
    
    #return twoDimList
#capacity = 10 
#weights = [1,4,8]

#print(maximum_gold(capacity, weights))

#if weights[v-1] <= c and twoDimList[v-1][c-weights[v-1]]+weights[v-1] >= twoDimList[v-1][c]: 
                #twoDimList[v][c]=twoDimList[v-1][c-weights[v-1]]+weights[v-1]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
