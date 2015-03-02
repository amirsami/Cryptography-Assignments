Python 2.7.3 (default, Aug  1 2012, 05:16:07) 
[GCC 4.6.3] on linux2
Type "copyright", "credits" or "license()" for more information.
==== No Subprocess ====
>>> from Crypto.Hash import SHA256
>>> block_size = 1024
>>> f = open('6 - 1 - Introduction (11 min).mp4', 'rb')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f = open('6 - 1 - Introduction (11 min).mp4', 'rb')
IOError: [Errno 2] No such file or directory: '6 - 1 - Introduction (11 min).mp4'
>>> 
>>> f = open('6 - 1 - Introduction (11 min).mp4', 'rb')
>>> f.seek(0,2)
>>> size = f.tell()
>>> last_block_size = size % block_size
>>> lista = range(0,size, block_size)
>>> lista.reverse()
>>> last_hash = ""
>>> for l in lista:
	f.seek(l,0)
	block = f.read(block_size)
	h = SHA256.new()
	h.update(block)
	h.update(last_hash)
	last_hash = h.digest()

	
>>> print last_hash.encode('hex')
5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949
>>> from Crypto.Hash import SHA256
>>> block_size = 1024
>>> f = open('6 - 2 - Generic birthday attack (16 min).mp4', 'rb')
>>> f.seek(0,2)
>>> size = f.tell()
>>> last_block_size = size % block_size
>>> lista = range(0,size, block_size)
>>> lista.reverse()
>>> last_hash = ""
>>> for l in lista:
	f.seek(l,0)
	block = f.read(block_size)
	h = SHA256.new()
	h.update(block)
	h.update(last_hash)
	last_hash = h.digest()

	
>>> print last_hash.encode('hex')
03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8
>>> 
