import os
import random
from datetime import date

from dotenv import load_dotenv

from utils.hellotracks.client import HellotracksClient

load_dotenv()

ht = HellotracksClient(
    user=os.environ.get("HELLOTRACKS_USER"),
    api_key=os.environ.get("HELLOTRACKS_API")
)

job_list = []

for _ in range(10):
    job = ht.create_job_object(
        job_type=2,
        team_id=1,
        order_id=random.randint(10001, 10200),
        day=int(date.today().strftime('%Y%m%d')),
        destination_lat=random.uniform(51.47690572136774, 51.538636920666406),
        destination_lng=random.uniform(-0.18411568297429584, -0.07517897752823008),
        destination_name="Battery Swapping",
        items_to_dropoff=1,
    )
    job_list.append(job)

ht.create_jobs(job_list=job_list, auto_assign=True)
