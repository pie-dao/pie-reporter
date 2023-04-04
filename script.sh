#!/bin/bash

export OLD_REPORT=2022-10
export NEW_REPORT=2022-11

python3 ./reporter/run.py conf
python3 ./reporter/run.py build "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
python3 ./reporter/run.py report "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
# cp ./reports/saved/epoch-$NEW_REPORT.json ./reports/$NEW_REPORT/epoch-$NEW_REPORT.json
# python3 ./reporter/double_checker/double_checker.py check "./reports/$NEW_REPORT/reporter-db.json" "./reports/$NEW_REPORT/epoch-$NEW_REPORT.json"

export OLD_REPORT=2022-11
export NEW_REPORT=2022-12

python3 ./reporter/run.py conf
python3 ./reporter/run.py build "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
python3 ./reporter/run.py report "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
cp ./reports/saved/epoch-$NEW_REPORT.json ./reports/$NEW_REPORT/epoch-$NEW_REPORT.json
python3 ./reporter/double_checker/double_checker.py check "./reports/$NEW_REPORT/reporter-db.json" "./reports/$NEW_REPORT/epoch-$NEW_REPORT.json"

export OLD_REPORT=2022-12
export NEW_REPORT=2023-1

python3 ./reporter/run.py conf
python3 ./reporter/run.py build "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
python3 ./reporter/run.py report "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
cp ./reports/saved/epoch-$NEW_REPORT.json ./reports/$NEW_REPORT/epoch-$NEW_REPORT.json
python3 ./reporter/double_checker/double_checker.py check "./reports/$NEW_REPORT/reporter-db.json" "./reports/$NEW_REPORT/epoch-$NEW_REPORT.json"

export OLD_REPORT=2023-1
export NEW_REPORT=2023-2

python3 ./reporter/run.py conf
python3 ./reporter/run.py build "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
python3 ./reporter/run.py report "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
cp ./reports/saved/epoch-$NEW_REPORT.json ./reports/$NEW_REPORT/epoch-$NEW_REPORT.json
python3 ./reporter/double_checker/double_checker.py check "./reports/$NEW_REPORT/reporter-db.json" "./reports/$NEW_REPORT/epoch-$NEW_REPORT.json"
