import os
from pprint import pprint

from dotenv import load_dotenv

from utils.hellotracks.client import HellotracksClient

load_dotenv()

ht = HellotracksClient(
    user=os.environ.get("HELLOTRACKS_USER"),
    api_key=os.environ.get("HELLOTRACKS_API")
)

r = ht.edit_account(worker="jose.duarte@humanforest.co.uk",
                    # status_label="On duty",
                    vehicle_capacity=3
                    )
pprint(r.json())
