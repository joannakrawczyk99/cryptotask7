import json
from flask import Flask

from blockchain import Blockchain

#Flask for creating a REST API
app = Flask(__name__)
blockchain = Blockchain()


@app.route('/', methods=['GET'])
def get_chain():
    """
    Defining web app, creating local blockchain, creating endpoint for displaying info of blockchain.
    :return: info about blockchain
    """
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return {"length": len(chain_data), "chain": chain_data}

app.run(debug=True, port=5000)