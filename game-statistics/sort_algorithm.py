lista=["ce faci","unde esti","cand vi","ana","cristi","zzlo"]
def sorting(x):
    for i in range (0,len(x)-1):
        for j in range(0,len(x)-i-1):
            if x[j]>x[j+1]:
                temp=x[j]
                x[j]=x[j+1]
                x[j+1]=temp
    return x
print(sorting)
