from web3 import Web3
import config

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider(config.GANACHE_URL))

# Load contract
contract = web3.eth.contract(address=config.CONTRACT_ADDRESS, abi=config.ABI)

def store_password(label: str, encrypted_password_hex: str):
    
    '''Stores a password label and AES-encrypted password (hex encoded) on the blockchain.'''
    
    tx_hash = contract.functions.storePassword(label, encrypted_password_hex).transact({'from': config.ACCOUNT})
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"✅ Stored on blockchain (TX: {receipt.transactionHash.hex()})")

def get_passwords():
    
    '''Retrieves a list of (label, encrypted_password_hex) from the blockchain for the current user.
    Returns a list of tuples.'''
    
    result = contract.functions.getPasswords().call({'from': config.ACCOUNT})
    return [(entry[0], entry[1]) for entry in result]
