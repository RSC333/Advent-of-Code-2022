output = 0
with open('day1-input.txt') as f:
    count = int(0)
    for line in f.readlines():
        if line == "\n":
            count=0
        else:
            count+=int(line)
            if count>output:
                output = count
    print(output)