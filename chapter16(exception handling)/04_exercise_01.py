## make a function 'divide'
# divide(a,b)

def divide(a,b):
    try:
        z = a/b
        print(z)
    except ZeroDivisionError:
        print("Please don't divide by zero")
    except Exception as e:
        print(f"Error is {e}")
    except:
        print("Unexcepted error")

divide(10,2)
divide(4,0)
divide('10',2)