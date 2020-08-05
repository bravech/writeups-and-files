from pwn import *
context.log_level='debug'
def make(x):
    checksum = sum([ord(h) for h in x]) & 0xff
    pk = '$%s#%s' % (x, '0' * (2 - len(hex(checksum)[2:])) + hex(checksum)[2:])
    return pk

s = remote('localhost', 1234)

s.send('+')
s.send(make('multiprocess+;xmlRegisters=i386;qRelocInsn+'))

print(s.recv()) # +$Hgp0.0#ad

s.send('+')
s.send(make('OK'))

print(s.recv()) # +$qTStatus#49

s.send('+')
s.send(make('Trunning;tnotrun:0'))

print(s.recv()) # +$qTfV#81

s.send('+')
s.send(make('1:0:1:74'))

print(s.recv()) # +$qTsV#8e

s.send('+')
s.send('$#00')

print(s.recv()) # ?

s.send('+')
s.send(make('S00'))

print(s.recv()) # Hc-1

s.send('+')
s.send(make('OK'))

print(s.recv()) # qC

s.send('+')
s.send(make('OK'))

print(s.recv()) # qAttached:a410

s.send('+')
s.send(make('1'))
