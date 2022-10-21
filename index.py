

x= [1,23,6,34534,76,12,5,2323,4,9]



def maxArray(n):

    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if(n[j] >= n[j+1]):
                temp = n[j]
                n[j]= n[j+1]
                n[j+1] = temp

    


maxArray(x)
print(x[-1])














