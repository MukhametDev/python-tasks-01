number = 10
count = 1
arr = []
index = 0
while count <= number:
    arr.append(count)
    count += 1

for dig in range(len(arr)):
    dig = 0
    while dig != arr[index]:
        print('#', end="")
        dig+=1
    dig = 0
    index += 1
    print()