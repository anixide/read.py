from sys import argv
script, input_file = argv  #Choose the script the text file chosen to print


# function to print the chosen file into the console
def print_all(f):
    print f.read()

# open the chosen file
current_file = open(input_file)
# Print the file into the console
print_all(current_file)

