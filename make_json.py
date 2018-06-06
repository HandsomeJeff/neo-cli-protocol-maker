import json
import ast
import requests


url = "https://raw.githubusercontent.com/neo-project/neo-cli/master/neo-cli/protocol.json"
protocol = ast.literal_eval(requests.get(url).text.encode('utf-8'))

def writeToJSON(seedlist, protocol=protocol):
    protocol["ProtocolConfiguration"]["SeedList"] = seedlist
    with open('protocol.json', 'w') as fp:
        json.dump(protocol, fp, indent=4)
