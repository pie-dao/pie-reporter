#!/bin/bash

export NEW_REPORT=$1;
export OLD_REPORT=$2;

python ./reporter/run.py conf
python ./reporter/run.py build  "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"
python ./reporter/run.py report "./reports/$NEW_REPORT" "./reports/$OLD_REPORT"

python ./reporter/double_checker/double_checker.py check "./reports/$NEW_REPORT/reporter-db.json" "./reports/$NEW_REPORT/diff/epoch-$NEW_REPORT.json" > "./reports/$NEW_REPORT/diff/diff.json"

yarn ts-node ./scripts/CreateClaims.ts -i "./reports/$NEW_REPORT/claims.json" -o $NEW_REPORT 