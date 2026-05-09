from solcx import compile_source, install_solc
from web3 import Web3
import json

install_solc("0.8.0")

with open("blockchain/Vault.sol", "r") as file:
    contract_source = file.read()

compiled_sol = compile_source(
    contract_source,
    output_values=["abi", "bin"],
    solc_version="0.8.0"
)

contract_id, contract_interface = compiled_sol.popitem()
abi = contract_interface["abi"]
bytecode = contract_interface["bin"]

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

if not web3.is_connected():
    raise Exception("⚠️ Could not connect to Ganache. Please check it's running.")

account = web3.eth.accounts[0]
web3.eth.default_account = account

Vault = web3.eth.contract(abi=abi, bytecode=bytecode)
tx_hash = Vault.constructor().transact()
tx_receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

contract_address = tx_receipt.contractAddress
print(f"✅ Contract deployed at: {contract_address}")

with open("config.py", "w") as f:
    f.write(f"CONTRACT_ADDRESS = '{contract_address}'\n")
    f.write(f"ABI = {json.dumps(abi)}\n")
    f.write(f"ACCOUNT = '{account}'\n")
    f.write(f"GANACHE_URL = '{ganache_url}'\n")
