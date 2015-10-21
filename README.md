# csvtoqbo

Python tool to convert CSV files generated from multiple providers to QBO format for Quickbooks

## What you need

- Find you bank ID number on the list located at https://ofx-prod-filist.intuit.com/qb2600/data/fidir.txt.
- Replace the ID located in qboconst.py `INTUBID = "62160"`

## Usage

`python csvtoqbo.py \<options\> \<csvfiles\>`

### Example

`python csvtoqbo.py -amazon Amazon-CSV-Test.csv`

### Test Suite:

python csvtoqbo-test.py
