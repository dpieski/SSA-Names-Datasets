# SSA Names Datasets
Script used to compile the Names/Gender datasets hosted here: https://data.world/dpieski/namesgender

Source of the data: https://www.ssa.gov/oact/babynames/limits.html

Folder structure:
names_gender.py
|-'SSA Names List'
|-|-'yobDATE.txt' files

Output is:
names_gender.csv (Compiled list of all names, a gender and the total count of that gender)
names_gender_percent.csv (Compiled list of all names, the more common gender, and the percent of people with that name that are the more common gender)
names_gender_year.csv (Same as names_gender but on a per year basis)
names_gender_year_percent.csv (Same as names_gender_percent but on a per year basis)

Use:
`python3 names_gender.py`
