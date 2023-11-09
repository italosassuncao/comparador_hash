import hashlib


arquivo_1 = "h1.txt"
arquivo_2 = "h2.txt"

hash1 = hashlib.new("ripemd160")
hash1.update(open(arquivo_1, "rb").read())

hash2 = hashlib.new("ripemd160")
hash2.update(open(arquivo_2, "rb").read())

if hash1.digest() != hash2.digest():
    print(f"O arquivo {arquivo_1} é diferente do arquivo {arquivo_2}")
    print("Hash arquivo 1: ", hash1.hexdigest())
    print("Hash arquivo 2: ", hash2.hexdigest())
else:
    print(f"O arquivo {arquivo_1} é igual ao arquivo {arquivo_2}")
    print("Hash arquivo 1: ", hash1.hexdigest())
    print("\nHash arquivo 2: ", hash2.hexdigest())
