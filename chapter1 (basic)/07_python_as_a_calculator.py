# python as a calculator

# operator    ||     description    
# "+"               "Addition"      
# "-"               "substraction"
# "*"               "Multiply"
# "/"               "float division"
# "//"              "integer division"
# "%"               "modulo, it gives remainder"
# "**"              "Exponent or power"

# addition
print(3+4)

# substraction
print(4-3)

# multiplication
print(4*3)

# float division
print(4/2)
print(2/4)

# integer division
print(4//2)
print(2//4)

# modulo
print(3%2)

# exponent or power
print(2**3)
print(2**0.5)

# round function
print(round(2**0.5, 4))


################ precedence and associativity rule ##############

## opertors         ||          precendence and associativity rule
# "parenthesis"                 "Highest"
# "Exponent"                    "Right to Left"
# "*,/,//,%"                    "Left to Right"
# "+,-"                         "Left to Right" 


print((2+3)*5/2%6)
print(2**3**2)

