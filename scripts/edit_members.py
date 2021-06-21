import os
from pprint import pprint

from utils.hellotracks.client import HellotracksClient

ht = HellotracksClient(
    user=os.environ.get("HELLOTRACKS_USER"),
    api_key=os.environ.get("HELLOTRACKS_API")
)

r = ht.edit_account(worker="jose.duarte@humanforest.co.uk",
                    # status_label="On duty",
                    vehicle_capacity=3
                    )
pprint(r.json())
