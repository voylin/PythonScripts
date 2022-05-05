import sys

"""
Capitalize all words in a CSV file, for this to work you have to make the split value from ',' to a '|' to work.
"""
def main(input_file,output_file = False):
    newlines = []
    # If no output file has been chosen, current file will be overwritten
    if  not output_file:
        output_file = input_file

    # Opening the file 
    with open(input_file,'r') as base_file:
        lines = base_file.readlines()

     # Reading the document line by line so all needed characters will be  found and capitalized
    for l in lines:
        capitalize_next = True
        i = 0
        line = ""
        # Checking each and every character and what comes in front to make sure the next one has to be capitalized
        while i < len(l):
            char = l[i]
            # Checking if the current character is one of the stop characters,
            # meaning that the next character will be the start of a new word.
            if l[i] in '|".;':
                capitalize_next = True
            # It can happen that after those characters a space is present, this should just be skipped.
            elif capitalize_next and l[i] != ' ':
                char = l[i].capitalize()    
                capitalize_next = False
            line += char
            i += 1

        newlines.append(line)
    
    # Overwriting and creating a new csv file with the made changes.
    with open(output_file, 'w') as file:
         file.writelines(newlines)

"""
Getting the CSV file name and a new location if needed
to run: "python, script location, CSV file, Possible new location"
"""
if __name__ == "__main__":
    try:
        input_file = sys.argv[1]
        if len(sys.argv) == 3:
            output_file = sys.argv[2]
            main(input_file,output_file)
        else:
            main(input_file)
    except IndexError:
        "If you don't enter a input_file, you will receive this error"
        print("usage: Infile (Outfile)")
