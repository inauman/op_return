# Publish a Message on Bitcoin Blockchain

As part of my Master in Digital Currencies & Blockchain from University of Nicosia, Cyprus; I have created this program to publish a message on Bitcoin blockchain. 

## Getting Started

This program is written in Python 2.7 and requires the Bitcoin Core node (testnet) running locally on your machine. When you run the program, you need to provide your favorite message/quote as the input. Once the message is provided, it will grab one spendable transaction ([UTXO](https://bitcoin.org/en/glossary/unspent-transaction-output) - Unspent Transaction Output), calculate the fee, create the raw transaction, sign it, and publish it on the blockchain.

### Prerequisite

 1. Install Bitcoin Core node (testnet)
 2. Install Python 2.7
 3. Install required Python modules
 ```
 pip install ecdsa base58 hashlib python-bitcoinrpc python-jsonrpc
```

## Sample
### Input
```
Enter your Bitcoin Core RPC User Name:<<<Username>>>
Enter your Bitcoin Core RPC Password:<<<Password>>>
Enter your favorite message or quote:<<<Quote>>>
```
### Output
```
Congratulations! You have just published a transaction to the Bitcoin blockchain.
**Previoux TxnId:** 330788c3dfc18808a04107d8c0c8f598d73eade8b1479e69b3db3ee3aa85aa98
**New TxnId:** 52e12ca20970a579bd62107054c45be33b5e21c31faa56de930df61bb043bf80
```
## Acknowledgements
Big thanks to all open source community and all the people who have taken the time and provided wonderful tutorials, videos, and answered the questions for newbees like me.

### 7 awesome youtube videos by Shlomi Zeltsinger
 1. [Bitcoin Pyhton Tutorials for Beginners](https://www.youtube.com/playlist?list=PLH4m2oS2ratfeNpZAoVwPlQqEr3HgNu7S)
 2. [Constructing a Bitcoin transaction using python](https://www.youtube.com/watch?v=AjCswCRBHdc&list=PLH4m2oS2ratf2N7l-LSU4qeeGwtbhzfWc)
 
###  Hexadecimal basics by Corey Schafer: 
[Understanding Binary, Hexadecimal, Decimal (Base-10), and more](https://www.youtube.com/watch?v=ZL-LhaaMTTE)

### ASCII Tutorial by dizauvi
[Characters in a computer - ASCII Tutorial](https://www.youtube.com/watch?v=B1Sf1IhA0j4)  

### Big Endian vs Little Endian by Michael Cote
[Big Endian vs Little Endian](https://www.youtube.com/watch?v=JrNF0KRAlyo)

### Bits vs Bytes as Fast As Possible by Techquickie
[Bits vs Bytes as Fast As Possible](https://www.youtube.com/watch?v=Dnd28lQHquU)

### Bitcoin Command Line by Christopher
 [Learning Bitcoin from the Command Line]( https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line)

### Python-Bitcoin/JSON RPC library by Jeff Garzik
[Python interface to bitcoin's JSON-RPC API](https://github.com/jgarzik/python-bitcoinrpc)