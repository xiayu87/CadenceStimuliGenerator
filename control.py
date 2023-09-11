import sys


def control_pattern(nb, np, pn, output_file):
    """
    This function takes the input file name and output file name as input
    and copies the content of input file to output file
    """
    # Open the output file and write the contents of the input file
    with open(output_file, 'a') as f:
        f.write("\n/////////////////////////////\n//CONTROL SIGNALS START HERE//\n/////////////////////////////\n\n")
        for j in range(int(np)):
            for i in range(int(nb)):
                f.write("{}{} pattern data=\"e,e,e\"\n".format(pn[j], i))
        for j in range(int(np)):
            for i in range(int(nb)):
                f.write("n{}{} pattern data=\"e_n,e_n,e_n\"\n".format(pn[j], i))
    print("File contents written to", output_file)


