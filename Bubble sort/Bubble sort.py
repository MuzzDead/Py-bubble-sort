
n = int(input())
massive = list(map(int,input().split()))
count = 0
for run in range(n-1): # n-1 because without last element
    for i in range(n-1-run):
        if massive[i] > massive[i+1]:
            count += 1
            massive[i], massive[i+1] = massive[i+1], massive[i]

print("Final result =", *massive)
print("count =", count)