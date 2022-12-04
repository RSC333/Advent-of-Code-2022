output = 0
with open('input.txt') as f:
    for line in f.readlines():
        line = line.replace('\n','').split(',')
        range1min = int(line[0].split('-')[0])
        range1max = int(line[0].split('-')[1])
        range2min = int(line[1].split('-')[0])
        range2max = int(line[1].split('-')[1])
        intersection = list(set([x for x in range(range1min,range1max+1)]).intersection([x for x in range(range2min,range2max+1)]))
        if len(intersection)>0:
            output+=1
    print(output)