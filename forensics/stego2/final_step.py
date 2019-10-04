import binascii
filename = 'original.png' #open the original image
with open(filename, 'rb') as f:
    content = f.read()
content=binascii.hexlify(content)
content=content[::-1] #reverse the contents
print content 
file2 = open(r"new","w+") # saving it as a new file
file2.write(content)