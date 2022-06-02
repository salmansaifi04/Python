import datetime

t = datetime.datetime.now()

## how to print time

t1 = t.time()
print(t1)

## hour
print(f'Hour is : {t1.hour}')

## minute
print(f"Minute is : {t1.minute}")

## second
print(f'Second is : {t1.second}')

## millisecond
print(f'Microsecond is : {t1.microsecond}')

## how to change time format
dt = t1.strftime('%H-%M-%S')
print(dt)

## how to set 12 hour clock
f = t1.strftime('%I-%M-%S')
print(f)

## 'AM/PM'
f1 = t1.strftime('%I-%M-%S %p')
print(f1)

## how to set time
f2 = datetime.time(8,9,20)
h = f2.strftime('%H-%M-%S %p')
print(h)