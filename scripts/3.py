######################## part1
import re

with open('data/3.txt', 'r') as f:
    matches = re.findall(r'(?:(?<=mul)\(\d{1,3},\d{1,3}\))', f.read())

#split and flatten multiply and sum numbers in list 
def flat_and_sum(matches):
    numbers = [int(x) for match in matches for x in match.strip('()').split(',')]

    list1 = numbers[0::2]
    list2 = numbers[1::2]
    result = (i*j for i,j in zip(list1, list2))

    return sum(result)

print(flat_and_sum(matches))

######################## part2
#does not work, beacause of edge cases, where the .sub pattern doesn't match the input.
#remove disabled mults and select enabled
with open('data/3.txt', 'r') as f:
    don = re.sub(r"don't\(\).*?(?=do\(\))", "", f.read())
    rest = re.findall(r"(?:(?<=mul)\(\d{1,3},\d{1,3}\))", don)

print(flat_and_sum(rest))

########################### part2 from stranger
sum_mul = 0
do_sum = True

with open('data/3.txt', 'r') as f:
    mem = f.read()

for x in re.finditer(r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)', mem):
    match x[0]:
        case 'do()':
            do_sum = True
        case 'don\'t()':
            do_sum = False
        case _:
            if do_sum:
                sum_mul += int(x[1]) * int(x[2])

print(sum_mul)