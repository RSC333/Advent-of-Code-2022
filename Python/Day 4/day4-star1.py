output = 0
with open('input.txt') as f:
    for line in f.readlines():
        line = line.replace('\n','').split(',')
        range1min = int(line[0].split('-')[0])
        range1max = int(line[0].split('-')[1])
        range2min = int(line[1].split('-')[0])
        range2max = int(line[1].split('-')[1])
        if range1min-range2min>=0 and range1max-range2max<=0 or range2min-range1min>=0 and range2max-range1max<=0:
            output+=1
    print(output)