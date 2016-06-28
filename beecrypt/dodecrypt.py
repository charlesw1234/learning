from Crypto.Cipher import AES

aesobj = AES.new('-' * 32, AES.MODE_CBC, '+' * 16)
open('test1.plain', 'wb').write(aesobj.decrypt(open('test.cipher', 'rb').read()))
