from dagster import execute_job
from assets import defs

if __name__ == "__main__":
    job = defs.get_implicit_global_asset_job_def()
    result = job.execute_in_process()
    print("Pipeline execution completed: ",result.success)
