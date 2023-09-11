import sys


def data_pattern(nb, np, pn, output_file):
    """
    This function takes the input file name and output file name as input
    and copies the content of input file to output file
    """
    # Open the output file and write the contents of the input file
    d_list = [["v0_0", "v0_1", "v0_2", "v0_3"],
              ["v1_0", "v1_1", "v1_2", "v1_3"],
              ["v2_0", "v2_1", "v2_2", "v2_3"],
              ["v3_0", "v3_1", "v3_2", "v3_3"]]
    n_list = [["v0_0n", "v0_1n", "v0_2n", "v0_3n"],
              ["v1_0n", "v1_1n", "v1_2n", "v1_3n"],
              ["v2_0n", "v2_1n", "v2_2n", "v2_3n"],
              ["v3_0n", "v3_1n", "v3_2n", "v3_3n"]]
    with open(output_file, 'a') as f:
        f.write("/////////////////////////////\n//DATA SIGNALS START HERE//\n/////////////////////////////\n\n")
        y = 0
        for j in range(int(np)):
            x = 0
            for i in range(int(nb)):
                f.write("{}_l_{} pattern data=\"e,{},e\"\n".format(pn[j], i, d_list[y][x]))
                x = x + 1
                if x == 4:
                    x = 0
            y = y + 1
            if y == 4:
                y = 0
        y = 0
        for j in range(int(np)):
            x = 0
            for i in range(int(nb)):
                f.write("{}_nl_{} pattern data=\"e_n,{},e_n\"\n".format(pn[j], i, n_list[y][x]))
                x = x + 1
                if x == 4:
                    x = 0
            y = y + 1
            if y == 4:
                y = 0
    print("File contents written to", output_file)


