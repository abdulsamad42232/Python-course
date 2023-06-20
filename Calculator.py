def sub(a,b):
  result=a-b
  return result
def add(a,b):
  result=a+b
  return result
def mult(a,b):
  result=a*b
  return result
def div(a,b):
  result=a/b
  return result
a=int(input("Enter first Integer :"))
b=int(input("Enter second Integer :"))
add(a,b)
sub(a,b)    
mult(a,b)
div(a,b)

print("the Addition of given integer is :",add(a,b))
print("the subtraction of given integer is :",sub(a,b))
print("the Multiplication of given integer is :",mult(a,b))
print("the Division of given integer is :",div(a,b))