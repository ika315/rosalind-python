

file = "C:\\Users\\irem3\\Downloads\\rosalind_ini2(2).txt"
res = []

with open(file, "r") as my_file:
    for line in my_file:
        x = line.split()
        for i in x:
            if i.isnumeric():
                res.append(int(i))

a = res[0]
b = res[1]

c = a * a + b * b

print(c)
