import os
from pprint import pprint

from dotenv import load_dotenv

from utils.hellotracks.client import HellotracksClient

load_dotenv()

ht = HellotracksClient(
    user=os.environ.get("HELLOTRACKS_USER"),
    api_key=os.environ.get("HELLOTRACKS_API")
)

jobs = ht.get_all_jobs_for_day(day=20210620).json()["jobs"]

pprint(jobs)
