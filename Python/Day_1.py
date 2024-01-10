f_lines = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
 
# getting numbers from string
result = 0
line = f_lines.split("\n")
print(f_lines)
for i in line:
    first_number = 0
    second_number = 0

    for x in i:
        if i.isdigit():
            first_number = i
            break

    line = line[::-1]

    for j in line:
        for x in i:
            if i.isdigit():
                second_number_number = j
                break

result = first_number + second_number

# print result
print("The numbers list is : " + str(result))