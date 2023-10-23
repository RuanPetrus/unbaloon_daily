import requests, json
import os, time
from  datetime import datetime
from pprint import pprint
from dataclasses import dataclass
from core import Problem, RESOURCES_PATH, SEP

ATCODER_PROBLEM_INFORMATION_PATH = RESOURCES_PATH + "problem_info.json"

def download_problems_info() -> None:
    problem_information_url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    r = requests.get(problem_information_url)
    info = r.json()
    pprint(info)
    problem_information = {
            name: info[name]["difficulty"] 
            for name in info.keys() 
            if "difficulty" in info[name]
    }
    with open(ATCODER_PROBLEM_INFORMATION_PATH, "w") as f:
        f.write(json.dumps(problem_information))

def get_problems_info() -> dict[str, int]:
    with open(ATCODER_PROBLEM_INFORMATION_PATH, "r") as f:
        problems_info = json.loads(f.read())
        return problems_info

def get_rating(problem_id: str, problems_info: dict[str, int]) -> int:
    x = problems_info.get(problem_id, 0)
    return 3/4 * x + 800


def get_users_problems_from_datetime(user_id: str, date: datetime) -> set[Problem]:
    unix_second = time.mktime(date.timetuple())
    user_submission_url = f"https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user={user_id}&from_second={int(unix_second)}"

    r = requests.get(user_submission_url)
    problems_from_request = r.json()
    problems_info = get_problems_info()

    problems: set[Problem] = set(
        Problem(
           website="atcoder", 
           id="atcoder_"+p["problem_id"],
           rating=get_rating(p["problem_id"], problems_info),
           date=datetime.fromtimestamp(int(p["epoch_second"]))
        )
        for p in problems_from_request
        if p["result"] == "AC"
    )
    return problems

def main() -> None:
    d = datetime(year=2023, month=9, day=22)
    problems = get_users_problems_from_datetime("MagePetrus", d)
    pprint(problems)


if __name__ == "__main__":
    main()
