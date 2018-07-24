import struct
import base58
import hashlib
import ecdsa
import binascii
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


#get the Bitcoin Core local node credentials
rpc_user=raw_input('Enter your Bitcoin Core RPC User Name:')
rpc_password=raw_input('Enter your Bitcoin Core RPC Password:')

#open RPC connection to the Bitcoin Core
rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))

#Find list of unspent transaction
unspent_tx = rpc_connection.listunspent()

#find one unspent transaction to pay for fee
prv_txid = unspent_tx[0]['txid'].encode('ascii','ignore')

#learnd about it after lots of stuggle, persistence, and persevrance -:)
prv_tx_vout = long(unspent_tx[0]['vout'])

#my testnet wallet address
wallet_address = unspent_tx[0]['address'].encode('ascii','ignore')

#get the hashed key and remember to hexlify the bytes
wallet_hashed_pubkey = base58.b58decode_check(wallet_address)[1:].encode("hex")

#grab the unspent amount from the transaction
unspent_amount = long(unspent_tx[0]['amount'] * 100000000) #convert to satoshis

#get the fee estimate. There are sophisticated ways to estimate but for this assignment I am using the simple method
feeestimate = rpc_connection.estimatesmartfee(6)
tx_fee = long(feeestimate['feerate']*100000000) #satoshis

# calculate the change amount
change_amount = unspent_amount - tx_fee #satoshis

# 1. Create the raw transaction without using any bitcoin python library
# 2. This transaction have 1 input and two output
# 3. Input = prv_txid and 2 Outputs are a) OP_RETURN and b) Change

# define the raw_tx class
class raw_tx:
	version 		= struct.pack("<L", 2)
	tx_in_count 	= struct.pack("<B", 1)
	tx_in 			= {} #TEMP
	tx_out_count	= struct.pack("<B", 2)
	tx_out1			= {} #TEMP
	tx_out2 		= {} #TEMP
	lock_time 		= struct.pack("<L", 0)

# function to flip the bytes (little endian)
def flip_byte_order(string):
	flipped = "".join(reversed([string[i:i+2] for i in range(0, len(string), 2)]))
	return flipped

# create the class
rtx = raw_tx()

rtx.tx_in["txouthash"] 		= flip_byte_order(prv_txid).decode("hex") #flip for little endian
rtx.tx_in["tx_out_number"]	= struct.pack("<B", prv_tx_vout)
rtx.tx_in["tx_out_index"] 	= struct.pack("<L", 0)
rtx.tx_in["script"] 		= ("76a914%s88ac" % wallet_hashed_pubkey).decode("hex")
rtx.tx_in["scrip_bytes"] 	= struct.pack("<B", len(rtx.tx_in["script"]))
rtx.tx_in["sequence"]		= "ffffffff".decode("hex")

def OP_RETURN_bin_to_hex(string):
	return binascii.hexlify(string)

# create output 1: OP_RETURN
rtx.tx_out1["value"]			= struct.pack("<Q", 0)

# Capture the user message input
user_message = raw_input('Enter your favorite message or quote:')

op_return_data 					= OP_RETURN_bin_to_hex(user_message) #data to be stored on blockchain
len_data 						= hex(len(op_return_data)/2)[2:].zfill(2) #divide by 2 to convert into bytes 
#hex codes for the script (https://en.bitcoin.it/wiki/Script): 6a - OP_RETURN
pk_script_data 					= "6a{}{}".format(len_data, op_return_data) 
rtx.tx_out1["pk_script"] 		= pk_script_data.decode("hex")

# Create output 2: Change
rtx.tx_out1["pk_script_bytes"] 	= struct.pack("<B", len(rtx.tx_out1["pk_script"]))
rtx.tx_out2["value"]			= struct.pack("<Q", change_amount) #pay change to self
#hex codes for the script (https://en.bitcoin.it/wiki/Script) -->
# a9 - OP_HASH160, 20 - 14, 87 - OP_EQUAL
rtx.tx_out2["pk_script"] 		= ("a914%s87" % wallet_hashed_pubkey).decode("hex")
rtx.tx_out2["pk_script_bytes"] 	= struct.pack("<B", len(rtx.tx_out2["pk_script"]))

# Create the raw transaction to sign
raw_tx_str = (
	rtx.version
	+ rtx.tx_in_count
	+ rtx.tx_in["txouthash"]
	+ rtx.tx_in["tx_out_number"]
	+ rtx.tx_in["tx_out_index"]
	+ rtx.tx_in["sequence"]
	+ rtx.tx_out_count
	+ rtx.tx_out1["value"]
	+ rtx.tx_out1["pk_script_bytes"]
	+ rtx.tx_out1["pk_script"]
	+ rtx.tx_out2["value"]
	+ rtx.tx_out2["pk_script_bytes"]
	+ rtx.tx_out2["pk_script"]
	+ rtx.lock_time

	)

#print raw_tx_str.encode("hex")

#Sign the transaction
signed_tx = rpc_connection.signrawtransaction(raw_tx_str.encode("hex"))

#Publish the transaction on the Bitcoin blockchain
confirm_txid =	rpc_connection.sendrawtransaction(signed_tx['hex'])

print("Congratulations! You have just published a transaction to the Bitcoin blockchain.")
print("Previoux TxnId: " + prv_txid)
print("New TxnId: " + confirm_txid)

# prv_txid = 55bf02507db97fcd2c5df39f9e56cfce29ac59280a7cf854d6d8a79bd6ea6d0d
# New TxnID = 4058196f0f2653bc8848eee5bbeedefef2f1a0f4385afe7948ff6dba05353cd5
# Confirmed with command line output
"""
bitcoin-cli gettransaction "4058196f0f2653bc8848eee5bbeedefef2f1a0f4385afe7948ff6dba05353cd5"
{
  "amount": 0.00000000,
  "fee": -0.01000000,
  "confirmations": 1,
  "blockhash": "000000000000003562e0a8a470e212cca3919b8061ea2bed7d1647f44a33bf2a",
  "blockindex": 1,
  "blocktime": 1532307346,
  "txid": "4058196f0f2653bc8848eee5bbeedefef2f1a0f4385afe7948ff6dba05353cd5",
  "walletconflicts": [
  ],
  "time": 1532307310,
  "timereceived": 1532307310,
  "bip125-replaceable": "no",
  "details": [
    {
      "account": "",
      "category": "send",
      "amount": 0.00000000,
      "vout": 0,
      "fee": -0.01000000,
      "abandoned": false
    },
    {
      "account": "",
      "address": "2N3Z9c4H6J2sJzfgtdi69He8PVfxfkB4Uuh",
      "category": "send",
      "amount": -0.09000000,
      "label": "",
      "vout": 1,
      "fee": -0.01000000,
      "abandoned": false
    },
    {
      "account": "",
      "address": "2N3Z9c4H6J2sJzfgtdi69He8PVfxfkB4Uuh",
      "category": "receive",
      "amount": 0.09000000,
      "label": "",
      "vout": 1
    }
  ],
  "hex": "020000000001010d6dead69ba7d8d654f87c0a2859ac29cecf569e9ff35d2ccd7fb97d5002bf55010000001716001478c85c23f05bd31a70498966e2f1000ca75f3a1cffffffff0200000000000000000e6a0c68656c6c6f20776f726c6421405489000000000017a91471151612c822f42b500b070300cd6827e5edc443870247304402202c4b5ca7f6ae63014196768a516f3f8641f415c5031f5eec695d23f37a69a136022056b1e7d165c5a48674f439f1389e37f1c22459d35f2ef52e80e4204f68bfd1ab0121024192f61f4c55e4bad3736eb49931d28eed0fb0f810baf4af891521a284349a6600000000"
}
"""