import datetime

t = datetime.datetime.now()

## only date

d = t.date()
print(d)

## year
print(f"Year is : {d.year}")

## month
print(f"Month is : {d.month}")

## day
print(f"Day is : {d.day}")


## how to change date format 

df = d.strftime('%d/%m/%y')
print(df)
df1 = d.strftime('%d/%m/%Y')
print(df1)

## how to print day using date format
dfd = d.strftime("%a %d / %m / %y")
print(dfd)
dfd1 = d.strftime("%A %d / %m / %y")
print(dfd1)


## how to set date
y = datetime.date(2000,4,6)
print(y)
y1 = y.strftime('%A')
print(y1)