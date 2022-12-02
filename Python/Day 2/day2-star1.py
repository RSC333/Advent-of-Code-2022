score = 0
with open('input.txt') as f:
    for line in f.readlines():
        score+=ord(line[-2])-87
        if ord(line[0])-ord(line[-2])==-23:
            score+=3
        elif line[0]=='A' and line[-2]=='Y':
            score+=6
        elif line[0]=='B' and line[-2]=='Z':
            score+=6
        elif line[0]=='C' and line[-2]=='X':
            score+=6
    print(score)