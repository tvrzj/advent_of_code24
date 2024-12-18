######################## part1
with open('data/2.txt', 'r') as f:
    file = [[int(num) for num in line.strip().split()] for line in f.readlines()]

def step_analyze(file):
    count=0
    for report in file:
        # Use all() to check if the condition holds for all consecutive elements
        if all(1 <= abs(report[i] - report[i - 1]) <= 3 for i in range(1, len(report))):
            count += 1 

    return count

def inc_analyze(file):
    filtered_file = []
    for report in file:
        # Check if the report is either entirely increasing or entirely decreasing
        inc = all(report[i] > report[i - 1] for i in range(1, len(report)))
        dec = all(report[i] < report[i - 1] for i in range(1, len(report)))
        
        if inc or dec:
            filtered_file.append(report)
    
    return filtered_file

print(step_analyze(inc_analyze(file)))

######################## part2
