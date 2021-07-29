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

# Create a function called `derive_wallets` by using the following three variables, 
# shown in ()
def derive_wallets(mnemonic, coin, numderive):
    command = f'php ./derive -g --mnemonic="{mnemonic}" --coin="{coin}" --numderive="{numderive}" --cols=path,address,privkey,pubkey --format=json'
    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
# For example, the ethereum dictionary will have "ETH" as its coin, and the Bitcoin
# dictionary will have "BTC" as its coin.
# The numdervice will output three results each for the ETH and BTCTEST wallets
coins = {"ETH": derive_wallets(mnemonic, ETH, numderive), 
"BTC": derive_wallets(mnemonic, ETH, numderive)}
numderive = 3
print(json.dumps(coin, indent=2, sort_keys=True))

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(# YOUR CODE HERE):
    # YOUR CODE HERE

# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(# YOUR CODE HERE):
    # YOUR CODE HERE




 
