#Question 1

def repeated_letters():
    string_input = input("Enter the statement: ")
    letter_input = input("Enter the letter you want to know repetition of in the statement: ")

    repeated_letter = []
    for i in range(len(string_input)):
        if letter_input == string_input[i]:
            repeated_letter.append(i)

    print(repeated_letter)

repeated_letters()


#Question 2
def multiplication_table():
    num1 = int(input("Enter the number: "))
    table = []
    
    for i in range(1, num1 + 1):
        row = []
        for j in range(1, i + 1):
            row.append(i * j)
        table.append(row)
    return table

result = multiplication_table()
print("List of Lists:", result)


