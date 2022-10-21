

x= {1,23,6,34534,76,12,5,2323,4,9}



def maxArray(n):

    for i in range(len(x)-1):
        for j in range(len(x)):
            if(n[i] >= n[i+1]):
                temp = 0
                n[i]= n[i+1]
                n[i+1] = temp





maxArray(x)









