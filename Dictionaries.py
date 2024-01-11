input = "C:\\Users\\irem3\\Downloads\\rosalind_ini6(2).txt"
output = input.replace(".txt", "_output.txt")

words = {}

with open(input, "r") as my_file, open(output, "w") as my_output:
    for line in my_file:
        for word in line.split():
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

    for key, value in words.items():
        my_output.write(key + " " + str(value) + "\n")



