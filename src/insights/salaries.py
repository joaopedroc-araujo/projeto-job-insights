from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self):
        max_salary = max(
            float(job["max_salary"])
            for job in self.jobs_list
            if job["max_salary"].isdigit()
        )
        return int(max_salary)

    def get_min_salary(self) -> int:
        min_salary = min(
            float(job["min_salary"])
            for job in self.jobs_list
            if job["min_salary"].isdigit()
        )
        return int(min_salary)

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        if "min_salary" not in job or "max_salary" not in job:
            raise ValueError("Minimum and maximum salary are required")
        min_salary = job["min_salary"]
        max_salary = job["max_salary"]
        if (
            not str(min_salary).lstrip("-").isnumeric()
            or not str(max_salary).lstrip("-").isnumeric()
        ):
            raise ValueError("Minimum and maximum salary must be numeric")
        min_salary = int(min_salary)
        max_salary = int(max_salary)
        if min_salary > max_salary:
            raise ValueError(
                "Minimum salary cannot be greater than maximum salary"
            )
        if not str(salary).lstrip("-").isnumeric():
            raise ValueError("Salary must be numeric")
        salary = int(salary)
        return min_salary <= salary <= max_salary

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
