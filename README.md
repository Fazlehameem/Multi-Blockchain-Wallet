# Multi-Blockchain-Wallet

My new startup requires me to focus on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well. For that purpose I will build out a system that create HD wallets. 

Dependencies


PHP must be installed on your operating system (any version, 5 or 7). Don't worry, you will not need to know any PHP.


You will need to clone the hd-wallet-derive tool.


bit Python Bitcoin library.


web3.py Python Ethereum library.


Project Steps 

Create a project directory called wallet and cd into it.


Clone the hd-wallet-derive tool into this folder and install it using the instructions on its README.md.


Create a symlink called derive for the hd-wallet-derive/hd-wallet-derive.php script into the top level project
directory like so: ln -s hd-wallet-derive/hd-wallet-derive.php derive
This will clean up the command needed to run the script in our code, as we can call ./derive
instead of ./hd-wallet-derive/hd-wallet-derive.php.


Test that you can run the ./derive script properly, use one of the examples on the repo's README.md


Create a file called wallet.py -- this will be your universal wallet script.


Setup Constants 

In a separate file, constants.py, set the following constants:

BTC = 'btc'
ETH = 'eth'
BTCTEST = 'btc-test'



In wallet.py, import all constants: from constants import *


Use these anytime you reference these strings, both in function calls, and in setting object keys.

Send some transactions 

Bitcoin Testnet transaction


Fund a BTCTEST address using this "bitcoin testnet".


Use a block explorer to watch transactions on the address.


Send a transaction to another testnet address (either one of your own, or the faucet's).


Screenshot the confirmation of the transaction like so: [bitcoin_testnet](Screenshot/Send_Tx.png)

Local PoA Ethereum transaction


Add one of the ETH addresses to the pre-allocated accounts in your networkname.json.


Delete the geth folder in each node, then re-initialize using geth --datadir nodeX init networkname.json.
This will create a new chain, and will pre-fund the new account.


Add the following middleware
to web3.py to support the PoA algorithm:


from web3.middleware import geth_poa_middleware

w3.middleware_onion.inject(geth_poa_middleware, layer=0)


Send a transaction from the pre-funded address within the wallet to another, then copy the txid into
MyCrypto's TX Status, and screenshot the successful transaction like so: [TX_Status](Screenshot/TX_Status.png)
