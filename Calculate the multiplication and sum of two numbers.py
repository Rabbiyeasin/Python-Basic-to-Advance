#Calculate the multiplication and sum of two numbers
#Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
#Given Number : 
    # number1 = 20  number1 = 40
    #number2 = 30   number2 = 30
#output: The result is 600  ,The result is 70

#Analysis
#Create a function that will take two numbers as parameters
# Next, Inside a function, multiply two numbers and save their product in a product variable
#Next, use the if condition to check if the product >1000. If yes, return the product
# Otherwise, use the else block to calculate the sum of two numbers and return it.

def multiplication_or_sum(value1,value2):
    product= value1*value2
    if product<=1000:
        return product
    else:
        return value1+value2
    
result = multiplication_or_sum(30,40)
print("The result is",result)
result = multiplication_or_sum(20,30)
print("The result is",result)

