## how to create a binary file
# rb (read binary file mode)
# extension is .dat

l = list(range(0,20))
f = open('binary.dat', 'wb')
f.write(bytes(l))
f.close()