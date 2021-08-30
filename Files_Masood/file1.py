lines = ['Sample data', 'Writing sample data into new text file']
with open('oper.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
        f.write('\n')
        
more_lines = ['', 'Appending data ', 'This is new data ']
with open('oper.txt', 'a') as f:
    f.write('\n')
    f.writelines('\n'.join(lines))
    f.write('\n')
    f.writelines('\n'.join(more_lines))

