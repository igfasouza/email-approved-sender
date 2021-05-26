import requests
import oci
from oci.config import from_file
from oci.signer import Signer
import datetime
import sys

print(sys.argv[1])

try:
    config = from_file("./config")
except oci.exceptions.ConfigFileNotFound as e:
    config = from_file()

auth = Signer(
tenancy=config['tenancy'],
user=config['user'],
fingerprint=config['fingerprint'],
private_key_file_location=config['key_file'],
pass_phrase=config['pass_phrase']
)
endpoint = 'https://email.' + config['region']  + '.oraclecloud.com/20170907/senders'
body = {'compartmentId': config['compartment_id'],'emailAddress': sys.argv[1],"timeCreated": datetime.datetime.now().strftime("%Z")}
try:
    response = requests.post(endpoint, json=body, auth=auth)
    response.raise_for_status()
    print(response.json())
except Exception as e:
    print(e)