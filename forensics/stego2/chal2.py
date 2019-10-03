import binascii
filename = 'original.png'
with open(filename, 'rb') as f:
    content = f.read()
content=binascii.hexlify(content)
content=content[::-1]
print content
file2 = open(r"new","w+") 
file2.write(content)