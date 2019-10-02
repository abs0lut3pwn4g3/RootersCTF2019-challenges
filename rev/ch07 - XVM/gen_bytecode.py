from pwn import *

#key is f00dbab3


bytecode = "XVM2"
bytecode += p32(0x0f000000) # r7 = key
bytecode += p32(0x04010000)	# movi ebx, 0x906ddad3
bytecode += p32(0x906ddad3)
bytecode += p32(0x04020000) # movi ecx, 0x41414141
bytecode += p32(0x41414141)
bytecode += p32(0x01010200) # eax = xor ebx, ecx
bytecode += p32(0x04010000)
bytecode += p32(0x21212121)
bytecode += p32(0x01000100)
bytecode += p32(0x05000700) # eax == r7
bytecode += p32(0x06000000)
bytecode += "XVM by X3eRo0"


a = open("bytecode","wb")
a.write(bytecode)
a.close()