input = "C:\\Users\\irem3\\Downloads\\rosalind_dna.txt"
output = input.replace(".txt", "_output.txt")

count_dict = {"A": 0, "C": 0, "G": 0, "T": 0}

# -> readlines: breaks file into list of lines,
# keeps the newline characters (\n) at the end of each line
# can iterate over the list to access individual lines
# -> read returns file as a string
# -> readline: moves the file cursor to the beginning of the next line after each call,
# returns an empty string ('') when the end of the file is reached

with open(input, "r") as my_file, open(output, "w") as my_output:
    string = my_file.read().replace("\n","") #replace, da newline auch gezählt wurde
    for nucleotides in string:
        if nucleotides in count_dict:
            count_dict[nucleotides] += 1
        else:
            count_dict[nucleotides] = 1

    for key in count_dict:
        my_output.write(str(count_dict[key]) + " ")


# meiner meinung nach elegantere lösung, aber rosalind möchte die int in einer bestimmten reihenfolge
# rosalind: A C G T, bei dieser methode: A G C T oder so

#count_dict2 = {}

#for nucleotides in string:
    #count_dict2[nucleotides] = count_dict2.get(nucleotides, 0) + 1
    #wenn der key nucleotide nicht gefunden wird, wird 0 an seiner stelle notiert

#print(count_dict2)

#1. methode für rosalind: {'A': 20, 'C': 12, 'G': 17, 'T': 21}
#elegantere methode: {'A': 20, 'G': 17, 'C': 12, 'T': 21}