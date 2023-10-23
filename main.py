from  datetime import datetime
from pprint import pprint
import atcoder


def main() -> None:
    d = datetime(year=2023, month=9, day=22)
    problems = atcoder.get_users_problems_from_datetime("MagePetrus", d)
    pprint(problems)


if __name__ == "__main__":
    main()
