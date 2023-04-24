# %%
import json
from functools import cached_property
from datetime import datetime, timedelta


# %%
# read a json file based on the directory structure in the reports folder
def read_json(path):
    with open(path) as f:
        return json.load(f)


# %%
class Report:
    def __init__(self, yy, mm):
        self.yy = yy
        self.mm = mm

    def _sum(self, property, accessor, readable):
        return sum([p[accessor] for p in getattr(self, property)]) / (
            1e18 if readable else 1
        )

    def _countif(self, property, condition):
        return len([p for p in getattr(self, property) if condition(p)])

    # readers

    @property
    def path(self):
        return f"../reports/{self.yy}-{self.mm}"

    @cached_property
    def distribution(self):
        return read_json(f"{self.path}/json/distribution.json")

    @cached_property
    def slashed(self):
        return read_json(f"{self.path}/json/slashed.json")

    @cached_property
    def claims(self):
        return read_json(f"{self.path}/claims.json")

    @cached_property
    def rewards(self):
        return read_json(f"{self.path}/json/rewards.json")

    @cached_property
    def reporter_db(self):
        return read_json(f"{self.path}/reporter-db.json")

    # aggregators

    @cached_property
    def total_distributed(self, readable=True):
        return self._sum("distribution", "amount", readable)

    @cached_property
    def total_slashed(self, readable=True):
        return self._sum("slashed", "slice_amount", readable)

    @cached_property
    def total_rewards(self, readable=True):
        return self._sum("rewards", "amount", readable)

    @cached_property
    def total_claims(self, readable=True):
        return sum(int(c["amount"]) for c in self.claims["recipients"].values()) / (
            1e18 if readable else 1
        )

    @cached_property
    def total_users(self):
        return self._countif("distribution", lambda _: True)

    @cached_property
    def distributed_users(self):
        return self._countif("distribution", lambda p: p["amount"] != 0)

    @cached_property
    def non_distributed_users(self):
        return self._countif("distribution", lambda p: p["amount"] == 0)

    @property
    def total_rewards_distributed(self):
        return int(self.claims["totalRewardsDistributed"]) / 1e18

    def total_for_state(self, state):
        return (
            sum(
                r["slice_amount"]
                for r in self.reporter_db["accounts"].values()
                if r["state"] == state
            )
            / 1e18
        )

    def count_for_state(self, state):
        return len(
            [r for r in self.reporter_db["accounts"].values() if r["state"] == state]
        )

    @cached_property
    def total_active_slice(self):
        return self.total_for_state("active")

    @cached_property
    def total_inactive_slice(self):
        return self.total_for_state("inactive")

    @cached_property
    def total_active_user(self):
        return self.count_for_state("active")

    @cached_property
    def total_inactive_user(self):
        return self.count_for_state("inactive")

    @cached_property
    def total_slashed_user(self):
        return self.count_for_state("slashed")

    # print all the above in a nicely formatted print statement
    def report(self):
        print(f"********* REPORT FOR {self.yy}-{self.mm} *********")
        print()
        print("----- TOTALS -----")
        print(f"Total rewards distributed: {self.total_rewards_distributed}")
        print(f"Total distributed in epoch: {self.total_distributed}")
        print(f"Total slashed: {self.total_slashed}")
        print(f"Total rewards: {self.total_rewards}")
        print(f"Total claims: {self.total_claims}")
        print(f"Total Active SLICE: {self.total_active_slice}")
        print(f"Total Inactive SLICE: {self.total_inactive_slice}")
        print()
        print("----- USERS -----")
        print(f"Total users: {self.total_users}")
        print(f"Distributed users (non zero): {self.distributed_users}")
        print(f"Non Distributed users: {self.non_distributed_users}")
        print(f"Total Active Users: {self.total_active_user}")
        print(f"Total Inactive Users: {self.total_inactive_user}")
        print(f"Total Slashed Users: {self.total_slashed_user}")
        print()


# %%
def create_reports(start: tuple[int, int], end: tuple[int, int]):
    reports = {}
    date = datetime(start[0], start[1], 1)
    end_date = datetime(end[0], end[1], 1)

    while date <= end_date:
        year = date.year
        month = date.month
        reports[f"{year}-{month}"] = Report(year, month)
        date += timedelta(days=32)  # advance to next month
        date = date.replace(day=1)  # reset day to 1 for the next iteration

    return reports


# %%
reports = create_reports((2021, 1), (2023, 3))

# %%
print("Year: 2022-9, Total Distributed:", reports["2022-9"].total_rewards_distributed)
print("Year: 2022-10, Total Distributed:", reports["2022-10"].total_rewards_distributed)
print("Year: 2022-11, Total Distributed:", reports["2022-11"].total_rewards_distributed)
print("Year: 2022-12, Total Distributed:", reports["2022-12"].total_rewards_distributed)
print("Year: 2023-1, Total Distributed:", reports["2023-1"].total_rewards_distributed)
print("Year: 2023-2, Total Distributed:", reports["2023-2"].total_rewards_distributed)
print("Year: 2023-3, Total Distributed:", reports["2023-3"].total_rewards_distributed)


# %%
reports["2022-9"].report()
reports["2022-10"].report()
reports["2022-11"].report()
reports["2022-12"].report()
reports["2023-1"].report()
reports["2023-2"].report()
reports["2023-3"].report()

# %%
