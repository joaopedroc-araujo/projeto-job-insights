from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, "r") as file:
            jobs_reader = csv.DictReader(file)
            self.jobs_list = list(jobs_reader)
            return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_jobs = set()
        for job in self.jobs_list:
            job_type = job["job_type"]
            unique_jobs.add(job_type)

        return list(unique_jobs)

    def filter_by_multiple_criteria(self, jobs, filter_criteria):
        if not isinstance(filter_criteria, dict):
            raise TypeError("filter_criteria must be a dictionary")

        filtered_jobs = list()
        for job in jobs:
            if all(
                job.get(key) == value for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)
        return filtered_jobs
