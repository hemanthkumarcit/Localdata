a = input(" Enter a num and num: ")

num1,num2 = a.split(",")

addition = int(num1)+int(num2)
sub = int(num1)-int(num2)
multiplication = int(num1)*int(num2)
division = int(num1)/int(num2)

print("Addition:",addition,"Subtraction:",sub,"Multiplication:",multiplication,"Division:",division,sep=",")


