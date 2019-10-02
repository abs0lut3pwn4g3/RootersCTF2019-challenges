all:
	gcc -o vm vm.c vm_func.c -ggdb
	python gen_bytecode.py
	cat code msg.jpg > bytecode
	rm code
	strip vm

clean:
	rm vm bytecode