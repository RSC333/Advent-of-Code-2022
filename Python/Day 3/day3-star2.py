output = 0
dupe = ''
elf = 0
with open('input.txt') as f:
    for line in f.readlines():
        elf+=1
        line = line.replace('\n','')
        itemset = ''.join(set(line))
        for c1item in itemset:
            if line.count(c1item)!=0:
                dupe+=c1item
        if elf%3==0:
            dupeset = ''.join(set(dupe))
            for item in dupeset:
                if dupe.count(item)==3:
                    if 96<ord(item)<123:
                        output += ord(item)-96
                    else:
                        output += ord(item)-38
            dupe = ''
    print(output)
