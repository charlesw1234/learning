from Crypto.Cipher import AES

aesobj = AES.new('-' * 32, AES.MODE_CBC, '+' * 16)
open('test.cipher', 'wb').write(aesobj.encrypt(open('test0.plain', 'rb').read()))
