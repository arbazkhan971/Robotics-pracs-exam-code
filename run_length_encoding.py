from collections import defaultdict
def rle(data):
    count = 1
    ans = []
    d = defaultdict(list)
    for i in range(1,len(data)):

        if data[i] == data[i-1]:
            count+= 1
        else:
            ans.append([data[i-1],count])
            count = 1
    else:
        ans.append([data[i],count])
    
    for k, v in ans:
         d[k].append(v)
    print(d)

inp = input("enter data")
print(inp)
print(type(inp))
print(len(str(inp)))
print(rle(str(inp)))
