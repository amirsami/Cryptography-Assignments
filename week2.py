Python 2.7.3 (default, Aug  1 2012, 05:16:07) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> from Crypto.Cipher import AES
>>> key = "140b41b22a29beb4061bda66b6747e14".decode('hex')
>>> ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode('hex')
>>> size = AES.block_size
>>> iv = ciphertext[:size]
>>> cipher = AES.new(key, AES.MODE_CBC, iv)
>>> msg = cipher.decrypt(ciphertext[16:])
>>> print msg
Basic CBC mode encryption needs padding.
>>> key = "140b41b22a29beb4061bda66b6747e14".decode('hex')
>>> ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode('hex')
>>> size = AES.block_size
>>> iv = ciphertext[:size]
>>> cipher = AES.new(key, AES.MODE_CBC, iv)
>>> msg = cipher.decrypt(ciphertext[16:])
>>> print msg
>>> key = "140b41b22a29beb4061bda66b6747e14".decode('hex')
>>> ciphertext = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81".decode('hex')
>>> size = AES.block_size
>>> iv = ciphertext[:size]
>>> cipher = AES.new(key, AES.MODE_CBC, iv)
>>> msg = cipher.decrypt(ciphertext[16:])
>>> print msg
Basic CBC mode encryption needs padding.
>>> 
KeyboardInterrupt
>>> key = "140b41b22a29beb4061bda66b6747e14".decode('hex')
>>> ciphertext = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253".decode('hex')
>>> size = AES.block_size
>>> iv = ciphertext[:size]
>>> cipher = AES.new(key, AES.MODE_CBC, iv)
>>> msg = cipher.decrypt(ciphertext[16:])
>>> print msg
Our implementation uses rand. IV
>>> key = "36f18357be4dbd77f050515c73fcf9f2".decode('hex')
>>> cyphertext = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
>>> iv1 = cyphertext[:32].decode('hex')
>>> iv2 = hex(int(cyphertext[:32], 16) + 1)[2:][:-1].decode('hex')
>>> iv3 = hex(int(cyphertext[:32], 16) + 2)[2:][:-1].decode('hex')
>>> iv4 = hex(int(cyphertext[:32], 16) + 3)[2:][:-1].decode('hex')
>>> ct1 = cyphertext[32:64].decode('hex')
>>> ct2 = cyphertext[64:96].decode('hex')
>>> ct3 = cyphertext[96:128].decode('hex')
>>> ct4 = cyphertext[128:].decode('hex')
>>> print pycrypto_decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print pycrypto_decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
NameError: name 'pycrypto_decrypt' is not defined
>>> print decrypt(key, iv1, ct1) + decrypt(key, iv2, ct2) + decrypt(key, iv3, ct3) + decrypt(key, iv4, ct4)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print decrypt(key, iv1, ct1) + decrypt(key, iv2, ct2) + decrypt(key, iv3, ct3) + decrypt(key, iv4, ct4)
NameError: name 'decrypt' is not defined
>>> print pycrypto.decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    print pycrypto.decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
NameError: name 'pycrypto' is not defined
>>> def pycrypto_decrypt(key, iv, data):
	crypt = AES.new(key, AES.MODE_CTR, counter=lambda: iv)
	return crypt.decrypt(data)

>>> print pycrypto_decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
CTR mode lets you build a stream cipher from a block cipher.
>>> key = "36f18357be4dbd77f050515c73fcf9f2".decode('hex')
>>> ctr_cyphertext2 = "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
>>> iv1 = ctr_cyphertext2[:32].decode('hex')
>>> iv2 = hex(int(ctr_cyphertext2[:32], 16) + 1)[2:][:-1].decode('hex')
>>> iv3 = hex(int(ctr_cyphertext2[:32], 16) + 2)[2:][:-1].decode('hex')
>>> iv4 = hex(int(ctr_cyphertext2[:32], 16) + 3)[2:][:-1].decode('hex')
>>> ct1 = ctr_cyphertext2[32:64].decode('hex')
>>> ct2 = ctr_cyphertext2[64:96].decode('hex')
>>> ct3 = ctr_cyphertext2[96:128].decode('hex')
>>> ct4 = ctr_cyphertext2[128:].decode('hex')
>>> print pycrypto_decrypt(key, iv1, ct1) + pycrypto_decrypt(key, iv2, ct2) + pycrypto_decrypt(key, iv3, ct3) + pycrypto_decrypt(key, iv4, ct4)
Always avoid the two time pad!
>>> 
