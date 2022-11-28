def knapshak(values,weights,w):
    ratio=[i/j for i,j in zip(values,weights)]
    index=list(range(len(values)))
    index.sort(reverse=True,key=lambda x:ratio[x])
    profit=0
    for i in index:
            if w > weights[i]:
                profit+=values[i]
                w-=weights[i]
            else:
                profit+=w*ratio[i]
                break
    return profit

values=[100,120,160]
weights=[10,20,30]
w=50
print(sum(values))
print(knapshak(values,weights,w))

TIME COMPL-O(nlogn)
