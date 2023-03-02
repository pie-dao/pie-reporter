# Note on bug report Feb-2022

Bug was due to using relative timezone instead of UTC timestamps in calculating slashing cutoff points. PieDAO compares the python `pie-reporter` to a nodejs `backend` script to check for differences in calculation of rewards.

A user `0xb8767b8AC030cb2DDb7605F6E79f342f707F73E1` voted at 10:45pm UTC on November 2022. In Dubai that is 2.45am, this registered him as:

- Not voted when running in GCC
- Voted when running the backend script in Europe

The user then did not vote for the next few months, so in January we recorded him as slashed, whereas user should be slashed in Feb.

## Impact:

- User was slashed early by 1 month, but has also failed to dispute the notarization in Jan
- Rest of users are unaffected

## For developers

We have recomputed distributions for Nov - Feb using UTC timestamps. However, due to the notorization process, we cannot retroactively amend Nov - Jan. Feburary data is what we believe to be correct, but there may be other future discrepancies which will require recomputing previous epochs.
