#Question 1

total_bill=47.28*1.15
print (f"total bill: {total_bill} USD")
tip=47.28*0.15
print(f"tip: {tip} USD")
each=total_bill/2
print(f"each person's share: {each} USD")



#Question 2
num1=input("enter first number: ")

if(num1.isdigit()):
 num1=int(num1)
else:
 {
 print("Enter digit number: ")
 }

 num2=input("enter second number: ")
if(num2.isdigit()):
 num2=int(num2)
result=num1/num2
print(result)

#Question 3


# word1 = "How" 
# word2 = "do" 
# word3 = "you" 
# word4 = "like" 
# word5 = "{}" 
# word6 = "so" 
# word7 = "far?"

# print(f"{word1} {word2} {word3} {word4} {word5} {word6} {word7}")

#question 4

# word7 = "far?"
# word5 = "{}" 

# word7=word7.replace('?', '!')
# print(word7)

# word5=word5.format("python")
# print(word5)




#Question 5

# statment=input("enter a astatment");
# statment_len=len(statment);
# print(f"the length of the statment is {statment_len}");


#Question 6
num1 = float(input("Enter a number: "))
choice = input("Enter choice (1=+ , 2=- , 3=* , 4=/): ")
num2 = float(input("Enter another number: "))

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
        result = num1 / num2
else:
    result = "Invalid choice"

print(f"Result: {result}")
