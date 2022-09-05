def _digit(number, input=None):
     if input is None:
        return number  #??
     return input(number) #В input будет лямбда-функция

def zero(input=None): return _digit(0, input)
def one(input=None): return _digit(1, input)
def two(input=None): return _digit(2, input)
def three(input=None): return _digit(3, input)
def four(input=None): return _digit(4, input)
def five(input=None): return _digit(5, input)
def six(input=None): return _digit(6, input)
def seven(input=None): return _digit(7, input)
def eight(input=None): return _digit(8, input)
def nine(input=None): return _digit(9, input)

def times(second_operand):
     return lambda first_operand: first_operand * second_operand
def plus(second_operand):
     return lambda first_operand: first_operand + second_operand
def minus(second_operand):
     return lambda first_operand: first_operand - second_operand
def divided_by(second_operand):
     return lambda first_operand: first_operand / second_operand

print(seven(times(five())))   #35
print(four(plus(nine())))     #13
print(eight(minus(three())))  #5
print(six(divided_by(two()))) #6 

#seven(times(five()))   #35
#four(plus(nine()))     #13
#eight(minus(three()))  #5
#six(divided_by(two())) #3 