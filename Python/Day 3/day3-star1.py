output = 0
dupe = ''
with open('input.txt') as f:
    for line in f.readlines():
        line = line.replace('\n','')
        compartment1 = line[int(len(line)/2):]
        compartment2 = line[:int(len(line)/2)]
        for c1item in compartment1:
            if compartment2.count(c1item)!=0:
                    dupe = c1item
        if 96<ord(dupe)<123:
            output += ord(dupe)-96
        else:
            output += ord(dupe)-38
    print(output)
