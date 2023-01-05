from web3 import Web3
import random
import json
import time
bsc = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc))
sender_address = "" #your address wallet to send token
privateKey = ''#your private key to send token
contract_address = "" #your token contract address

#List of acount to get token
accountList = [          
    '0x025F8a23d5BE041B91fB059091eb143197488056',
    '0x810e60F042BdC321D52879405ce724d5d93Ee6D4',
    '0xD21c6605C1A865C5055d6252Da485F715d204A1A',
    '0x41a1c6497cC6022350B8f5B1c848CEaA5e2bdc64',
    '0xE728ce82d36b72E74679c5e51f0341A3b64a4512',
    '0xf364fad2834fFe1710A32052f66978AbFd81d83E',
    '0xaf2500A7500D4Fe1237f685Ac22769c03756b220',
    '0x6fbC46bcb327da1De9acEB31b2c7Fe8Fc8889a90',
    '0xAC62b186e25198d9E878eB773D8E4E6aC1f47045',
    ]
AmountSent = 4 # amount of token will disibute
E = 1000000000000000000
AmountinWie = AmountSent*E
print("START-SEND")
print("Connect: "+ str(web3.isConnected()))
balance = web3.eth.get_balance(sender_address)
humanReadable = web3.fromWei(balance,'ether')
print(humanReadable)

# Abi of Your Token Contract
tokenAbi = [ 
    
        {
            "inputs": [],
            "stateMutability": "nonpayable",
            "type": "constructor"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "owner",
                    "type": "address"
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "spender",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Approval",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "issuer",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "bool",
                    "name": "value",
                    "type": "bool"
                }
            ],
            "name": "IssuerRights",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "from",
                    "type": "address"
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "to",
                    "type": "address"
                },
                {
                    "indexed": False,
                    "internalType": "uint256",
                    "name": "value",
                    "type": "uint256"
                }
            ],
            "name": "Transfer",
            "type": "event"
        },
        {
            "anonymous": False,
            "inputs": [
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "previousOwner",
                    "type": "address"
                },
                {
                    "indexed": True,
                    "internalType": "address",
                    "name": "newOwner",
                    "type": "address"
                }
            ],
            "name": "TransferOwnership",
            "type": "event"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "allowance",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_spender",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "approve",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "balanceOf",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "burn",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_from",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "burnFrom",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "decimals",
            "outputs": [
                {
                    "internalType": "uint8",
                    "name": "",
                    "type": "uint8"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "getOwner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "name": "isIssuer",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "",
                    "type": "bool"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "mint",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "name",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "owner",
            "outputs": [
                {
                    "internalType": "address",
                    "name": "",
                    "type": "address"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_issuer",
                    "type": "address"
                },
                {
                    "internalType": "bool",
                    "name": "_value",
                    "type": "bool"
                }
            ],
            "name": "setIssuerRights",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "symbol",
            "outputs": [
                {
                    "internalType": "string",
                    "name": "",
                    "type": "string"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [],
            "name": "totalSupply",
            "outputs": [
                {
                    "internalType": "uint256",
                    "name": "",
                    "type": "uint256"
                }
            ],
            "stateMutability": "view",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "transfer",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_from",
                    "type": "address"
                },
                {
                    "internalType": "address",
                    "name": "_to",
                    "type": "address"
                },
                {
                    "internalType": "uint256",
                    "name": "_amount",
                    "type": "uint256"
                }
            ],
            "name": "transferFrom",
            "outputs": [
                {
                    "internalType": "bool",
                    "name": "success",
                    "type": "bool"
                }
            ],
            "stateMutability": "nonpayable",
            "type": "function"
        },
        {
            "inputs": [
                {
                    "internalType": "address",
                    "name": "_newOwner",
                    "type": "address"
                }
            ],
            "name": "transferOwnership",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function"
        }
    ]


TokenContract = web3.eth.contract(contract_address, abi=tokenAbi)
balanceDox = TokenContract.functions.balanceOf(sender_address).call()
name = TokenContract.functions.symbol().call()
readable = web3.fromWei(balanceDox, 'ether')
print("Balance: " + str(readable) + " " + name)
for i in range(0,len(accountList)):
    print("Start sending-----------------------------------")
    TokenContract = web3.eth.contract(contract_address, abi=tokenAbi)
    balance = web3.eth.get_balance(sender_address)
    humanReadable = web3.fromWei(balance,'ether')
    print(humanReadable)
    raw_txn = {
    "from": sender_address, 
    "gasPrice": web3.eth.gasPrice,
    "gas": 60000,
    "to": contract_address,
    "value": "0x0",
    "data": TokenContract.encodeABI('transfer', args=( Web3.toChecksumAddress(accountList[i]),AmountinWie)),
    "nonce": web3.eth.getTransactionCount(sender_address)
    }    
    signed_txn = web3.eth.account.signTransaction(raw_txn, private_key=privateKey)
    tx_token= web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    print("Sent " + str(i)+ " to " +accountList[i])
    #print("TX " + web3.toHex(tx_token))
    balanceDox = TokenContract.functions.balanceOf(sender_address).call()
    readable = web3.fromWei(balanceDox, 'ether')
    print("Balance: " + str(readable) + " " + "DOX")
    print("Done sent-------------" + str(i)+ "-------------------------")    
    print("==================================================")
    time.sleep(30)
    
signed_txn = web3.eth.account.signTransaction(raw_txn, private_key=privateKey)
tx_token= web3.eth.send_raw_transaction(signed_txn.rawTransaction)
