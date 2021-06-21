import os
from pprint import pprint

from dotenv import load_dotenv

from utils.hellotracks.client import HellotracksClient

load_dotenv()

ht = HellotracksClient(
    user=os.environ.get("HELLOTRACKS_USER"),
    api_key=os.environ.get("HELLOTRACKS_API")
)

pprint(ht.get_accounts().json())
