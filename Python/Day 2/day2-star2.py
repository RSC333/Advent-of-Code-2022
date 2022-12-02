score = 0
with open('input.txt') as f:
    for line in f.readlines():
        if line[-2]=='X':
            if line[0] == 'A':
                score+=3
            else:
                score+=ord(line[0])-65
        if line[-2]=='Y':
            score+=3
            score+=ord(line[0])-64
        if line[-2]=='Z':
            score+=6
            if line[0] == 'C':
                score+=1
            else:
                score+=ord(line[0])-63
    print(score)