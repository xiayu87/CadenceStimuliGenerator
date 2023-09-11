import sys


def ack_pattern(np, pn, output_file):
    """
    This function takes the input file name and output file name as input
    and copies the content of input file to output file
    """
    # Open the output file and write the contents of the input file
    with open(output_file, 'a') as f:
        f.write("\n/////////////////////////////\n//ACK SIGNALS START HERE//\n/////////////////////////////\n\n")
        for j in range(int(np)):
            f.write("{}_rack pattern data=\"e_n,s_n,s_n\"\n".format(pn[j]))
        for j in range(int(np)):
            f.write("{}_nrack pattern data=\"e,s,s\"\n".format(pn[j]))
    print("File contents written to", output_file)


