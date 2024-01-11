input = "C:\\Users\\irem3\\Downloads\\rosalind_revc.txt"
output = input.replace(".txt", "_output.txt")

with open(input, "r") as my_file, open(output, "w") as my_output:
    for line in my_file:
        complement = ""
        for word in line:
            string = ''.join(word)
            for letter in string:
                match letter:
                    case "A":
                        complement += "T"
                    case "T":
                        complement += "A"
                    case "G":
                        complement += "C"
                    case "C":
                        complement += "G"


        my_output.write(complement[::-1]+"\n")

#alternative
#complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
    #for line in input_file:
        #complement = [complement_dict[letter] for letter in line.strip()[::-1]]
        #output_file.write("".join(complement) + "\n")
