source code:
  https://github.com/inauman/op_return

#references

"""
To use this program please make sure you have Bitcoin Core (testnet) running on your machine. You would also need to install some of the common libraries like ecdsa etc.

This program runs on Python 2.7 in interactive mode. When you run the program, you need to provide your favorite message/quote as the input.

Once the message is provided, it will grab one spendable transaction, calculate the fee, and create the raw transaction, sign it, and publish it on the blockchain.

Big thanks to all open source community and all the people who have taken the time and provided wonderful tutorials, videos, and answered the questions for newbees like me.

Constructing a Bitcoin Transaction - 7 awesome youtube videos by Shlomi Zeltsinger
  https://www.youtube.com/playlist?list=PLH4m2oS2ratfeNpZAoVwPlQqEr3HgNu7S
  https://www.youtube.com/playlist?list=PLH4m2oS2ratf2N7l-LSU4qeeGwtbhzfWc

hexadecimal basics by Corey Schafer:
  https://www.youtube.com/watch?v=ZL-LhaaMTTE

ASCII Tutorial by dizauvi (3 videos):
  https://www.youtube.com/watch?v=B1Sf1IhA0j4

Big Endian vs Little Endian by Michael Cote:
  https://www.youtube.com/watch?v=JrNF0KRAlyo

Bits vs Bytes as Fast As Possible by Techquickie: 
  https://www.youtube.com/watch?v=Dnd28lQHquU

Bitcoin Command Line by Christopher
  https://github.com/ChristopherA/Learning-Bitcoin-from-the-Command-Line

Python-Bitcoin/JSON RPC library by Jeff Garzik
  https://github.com/jgarzik/python-bitcoinrpc
"""

"""
    <-- Here is the sample of what the program would look like when you run it locally -->

      Enter your Bitcoin Core RPC User Name:<<<Username>>>
      Enter your Bitcoin Core RPC Password:<<<Password>>>
      Enter your favorite message or quote:<<<Quote>>>
      Congratulations! You have just published a transaction to the Bitcoin blockchain.
      Previoux TxnId: 330788c3dfc18808a04107d8c0c8f598d73eade8b1479e69b3db3ee3aa85aa98
      New TxnId: 52e12ca20970a579bd62107054c45be33b5e21c31faa56de930df61bb043bf80

"""