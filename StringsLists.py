number_list = []
string_list = []

file = "C:\\Users\\irem3\\Downloads\\rosalind_ini3(2).txt"
with open(file, "r") as my_file:
    for line in my_file:
        x = line.split()

        for word in x:
            if word.isnumeric():
                number_list.append(int(word))
            else:
                string_list.append(word)

a, b, c, d = number_list[0], number_list[1], number_list[2], number_list[3]
print(string_list[0][a:b + 1] + " " + string_list[0][c:d + 1])
