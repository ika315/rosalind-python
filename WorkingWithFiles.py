input = "C:\\Users\\irem3\\Downloads\\rosalind_ini5(2).txt"
output = input.replace(".txt", "_output.txt")

with open(input, "r") as my_file, open(output, "w") as my_output:
    result = list(my_file)[1::2]

    for line in result:
        my_output.write(line.strip() + "\n")






