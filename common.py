import sys

def copy_file(input_file, output_file):
    """
    This function takes the input file name and output file name as input
    and copies the content of input file to output file
    """
    # Open the input file and read its contents
    with open(input_file, 'r') as f:
        input_data = f.read()
    # Open the output file and write the contents of the input file
    with open(output_file, 'w') as f:
        f.write(input_data)
    print("File contents written to", output_file)

