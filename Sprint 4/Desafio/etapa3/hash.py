import hashlib

string = ""
print("======================TRANSFORMADOR DE STRING PARA HASH======================")

while string.lower() != 'sair':
    string = input("Digite uma frase ou digite 'sair' para sair: ")
    string_para_hash = hashlib.sha1(string.encode()).hexdigest()
    
    if string.lower() != 'sair':
        print(f"A frase: '{string}' em Hash é: '{string_para_hash}' ")