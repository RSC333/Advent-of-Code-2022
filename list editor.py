type  = input("int:1  str:2 float:3")
text = input("input list")
separator = input("separator")
mid = text.split(separator)
output = []
if type == "1":
    for i in mid:
        output.append(int(i))
if type == "2":
    for i in mid:
        output.append(str(i))
if type == "3":
    for i in mid:
        output.append(float(i))
print(output)
