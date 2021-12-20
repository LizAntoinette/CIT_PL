str = "3, 5 ,  7, 4.5\n"
values = str.split(',')
print(len(values))
values = [x.strip() for x in values]
print(values)