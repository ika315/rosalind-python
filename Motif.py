import re

input = "C:\\Users\\irem3\\Downloads\\rosalind_subs.txt"
output = input.replace(".txt", "_output.txt")

with open(input, "r") as my_file, open(output, "w") as my_output:
    lines = my_file.read().splitlines() #reads lines from the txt document separated by newline
    sequence = lines[0]
    motif = lines[1]

    #letzte for loop von: https://www.geeksforgeeks.org/python-program-to-find-indices-of-overlapping-substrings/

    for m in re.finditer('(?={0})'.format(re.escape(motif)), sequence):
        my_output.write(str(m.start()+1) + " ")

#escape: escapes the special characters

#format: replaces the value of the placeholder ( {0} ) with re.escape(motif)

# '(?=0)': positive lookahead: (?=element) syntax means if element follows match
# then it will be a match otherwise match will technically not be a match and will not be declared as a match
# die 0 wird nicht benutzt! 0 ist nur ein platzhalter für das erste argument was in format kommt
