with open('except/data.txt') as f:
    lines = f.readlines()

print(len(lines))
print(type(lines))
for i in lines:
    print(i.strip())
