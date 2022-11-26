def count_target_pair(l,target):
    k = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==target:
                k=k+1
    return f"Amount of pairs={k}"


arr = [1, 3, 6, 2, 2, 0, 4, 5]
target = 5
print(count_target_pair(arr, target))
