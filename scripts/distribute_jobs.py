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
job_ids = [v
           for job in jobs
           for k, v in job.items() if k == "id"]
pprint(job_ids)
# print(ht.delete_jobs(job_id_list=job_ids).request.body)
distribute = ht.distribute_jobs(job_id_list=job_ids, regions=1, optimize=1)

print(distribute.json())
print(distribute.request.body)
