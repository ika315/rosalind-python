x = []

file = "C:\\Users\\irem3\\Downloads\\rosalind_ini4(4).txt"
with open(file, "r") as my_file:
    for line in my_file:
        x = line.split()

a, b = int(x[0]), int(x[1])
sum = 0

for n in range(a, b + 1):
    if (n % 2 != 0):
        sum += n

print(sum)
