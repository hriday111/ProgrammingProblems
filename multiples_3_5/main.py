x=[]
def checkMultiples(nums,inp):
    global x
    for i in nums:
        if inp%i==0:
            x.append(inp)
            break
    return x

for i in range(1001):
    checkMultiples([3,5],i)
print(sum(x))