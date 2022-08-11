my_file = open("read_this.txt")
my_file.seek(0)

for line in my_file.readlines():
    print(line, end='')
