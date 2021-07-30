# Creating a Universal Wallet Script
# Import dependencies
import subprocess
import json
import os
from dotenv import load_dotenv

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("mnemonic")
numderive=os.getenv("numderive")
coin=os.getenv("coin")

# Import constants.py and necessary functions from bit and web3
from constants import *
from bit import *
from bit.network import NetworkAPI
from web3 import Web3
from web3.middleware import geth_poa_middleware


# Create a function called `derive_wallets` by using the following three variables: 
#  mnemonic, coin, numderive
# Popen will excecute the command in the variable, then reads the subprocess, then waits
# for the subprocess to finish
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=path,address,privkey,pubkey --format=json'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = process.communicate()
    process_status = process.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
# For example, the ethereum dictionary will have "ETH" as its coin, and the Bitcoin
# dictionary will have "BTCTEST" as its coin.
# The numdervice will output three results each for the ETH and BTCTEST wallets
coins = {"ETH": derive_wallets(mnemonic, ETH, numderive), 
"BTCTEST": derive_wallets(mnemonic, BTCTEST, numderive)}
numderive = 3

# print the outputs - json objects change to string format, with the keys sorted
print(json.dumps(coin, indent=2, sort_keys=True))

# Create the BTCTEST and ETH private keys
# Converting the PrivateKey objects into strings for printing
priv_key_eth = coin[ETH][0]["PrivateKey"]
priv_key_btctest = coin[BTCTEST][0]["PrivateKey"]
print(json.dumps(priv_key_eth))
print(json.dumps(priv_key_btctest))

# Placing the poa middleware into its appropriate layer. The geth Ethereum node 
# is placed at the deepest layer, 0
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
# If the coin is Ethereum or BTCTEST, they will be sent to their appropriate account object.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privatekeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key) 

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
#def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
#def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE




 
