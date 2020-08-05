
Hello, fellow space enthusiasts!

I have been tracking a specific satellite and managed to intercept an interesting 
piece of data. Unfortunately, the data is encrypted using an AES-128 key with ECB-Mode.

Encrypted Data: a69bf8eb895bcacc01af3dc97893816968c37d6e26dea8bd695356703b40f5aac28308133f2dc80aba9e920fbf3f2f1102dd3022d3af408f5477c1d748fc036b6320b6f82ba08e5e19249e4ab7a5a97a42752758f9e40317f093bb780f160722fcfba2c95e2d3f09779264fae2e50d53f0de4c1e76dcac8a2bffb8c915cc7438

Using proprietary documentation, I have learned that the process of generating the 
AES key always produces the same first 6 bytes, while the remaining bytes are random:

Key Bytes 0..5: 558d11711da4

The communication protocol hashes every message into a 128bit digest, which is encrypted
with the satellite key, and sent back as an authenticated ACK. This process fortunately 
happens BEFORE the satellite attempts to decrypt and process my message, which it will
immediately drop my message as I cannot encrypt it properly without the key.

I have read about "side channel attacks" on crypto but don't really understand them, 
so I'm reaching out to you for help. I know timing data could be important so I've 
already used this vulnerability to collect a large data set of encryption times for 
various hash values. Please take a look!

