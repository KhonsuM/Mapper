
# Input File Name
infile = input()

# Output file name
outfile = input()

# Read Method Mappings
methods = open("methods.txt" ,'r')
fields = open("fields.txt", 'r')

method_data_first = methods.read().splitlines()
field_data_first = fields.read().splitlines()

method_data_second = []
field_data_second = []

for line in method_data_first:
    method = line.split(",")

    method_data_second.append(method[0] + ":::" + method[1])

for line in field_data_first:
    field = line.split(",")

    field_data_second.append(field[0] + ":::" + field[1])

methods.close()
fields.close()

a = open(infile, 'r')
data = a.read()
a.close()

for s in method_data_second:
    nice = s.split(":::")

    data = data.replace(nice[0], nice[1])

for s in field_data_second:
    nice = s.split(":::")

    data = data.replace(nice[0], nice[1])

b = open(outfile, 'w')
b.write(data)
b.close()