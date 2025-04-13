def read_and_write():
    with open("ds.csv","r") as input_file:
        input_lines=input_file.readlines()
    with open("ds.tsv","w") as output_file:
        for line in input_lines:
            newline=line.replace('","', '"\t"')
            newline=newline.replace(',true,true,', '\ttrue\ttrue\t')
            newline=newline.replace(',false,true,', '\tfalse\ttrue\t')
            newline=newline.replace(',true,false,', '\ttrue\tfalse\t')
            newline=newline.replace(',false,false,', '\tfalse\tfalse\t')
            output_file.write(newline)


if __name__=='__main__':
    read_and_write()