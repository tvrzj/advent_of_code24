######################## part1
with open('data/1.txt', 'r') as f:
    file = [i.strip('\n') for i in f.readlines()]
    data = [int(word) for line in file for word in line.split()]
    list1 = sorted(data[0::2])
    list2 = sorted(data[1::2])

result = [abs(f - s) for f, s in zip(list1, list2)]
print(sum(result))

######################## part2
result2 = 0
for val in list1:
    result2 += val * list2.count(val)
    
print(result2)