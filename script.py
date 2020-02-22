from blockchain import Blockchain

block_one_transactions = {"sender":"Guy", "receiver": "Pal", "amount":"1"}
block_two_transactions = {"sender": "Buddy", "receiver":"Friend", "amount":"20000"}
block_three_transactions = {"sender":"Pal", "receiver":"Guy", "amount":"75"}
fake_transactions = {"sender": "Friend", "receiver":"Guy", "amount":"0.1"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()

local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

#Adding a fake transaction to test blockchain security
#local_blockchain.chain[2].transactions = fake_transactions
#local_blockchain.validate_chain()
