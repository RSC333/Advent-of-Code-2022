output = 0
with open('input.txt') as f:
    for line in f.readlines():
        line = line.replace('\n','')
        
    print(output)