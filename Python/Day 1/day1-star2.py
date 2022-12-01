elfs = []
with open('day1-input.txt') as f:
    count = int(0)
    for line in f.readlines():
        if line == "\n":
            elfs.append(count)
            count=0
        else:
            count+=int(line)
    elfs.sort()
    output = elfs[-1]+elfs[-2]+elfs[-3]
    print(output)
