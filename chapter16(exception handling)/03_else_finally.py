## Finally :- It is useful to print a compulsary statement if exception is occur or not

## Example 1 ##
try:
    x = 10
    y = 0
    z = x/y
    print(z)
except Exception as e:
    print(e)
finally:
    print("hello")

## we don't use 'except' after the 'finally' keyword

## Example 2 ##

while True:
    try:
        age = int(input("Enter your age : "))
    except ValueError:
        print("Please type integer !!!")
    except:
        print("Unexcepted Error !!!")
    else:
        print(f"user input : {age}")
        break
    finally:
        print("finally block ......")
