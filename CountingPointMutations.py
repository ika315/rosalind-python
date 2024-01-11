input = "C:\\Users\\irem3\\Downloads\\rosalind_hamm.txt"
output = input.replace(".txt", "_output.txt")

strings = []
mismatch = 0

with open(input, "r") as my_file, open(output, "w") as my_output:
    for line in my_file:
        strings += line.split()
    seq_1 = strings[0]
    seq_2 = strings[1]

    for char1, char2 in zip(seq_1,seq_2):
        if char1 != char2:
            mismatch += 1

    my_output.write(str(mismatch))