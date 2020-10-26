import os
import csv

root = os.path.abspath(os.getcwd())
print('root: {}'.format(root))

namesfolder = r"SSA Names List"

namespath = os.path.join(root, namesfolder)
print('namespath: {}'.format(namespath))

names_gender_year = dict()
names_gender = dict()

for namefile in os.listdir(namespath):
    if (namefile[:3] == "yob" and namefile[-3:] == "txt"):
        with open(os.path.join(namespath, namefile)) as csv_file:
            nameyear = namefile[3:7]
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                # name, gender, year
                ngy_key = (row[0], row[1], nameyear)
                # name, gender
                ng_key = (row[0], row[1])

                if ngy_key in names_gender_year:
                    names_gender_year[ngy_key] += int(row[2])
                else:
                    names_gender_year[ngy_key] = int(row[2])

                if ng_key in names_gender:
                    names_gender[ng_key] += int(row[2])
                else:
                    names_gender[ng_key] = int(row[2])

ngyp_dict = dict()
ngp_dict = dict()

for ngy_key, ngy_value in names_gender_year.items():
    # Key is name, year
    ngyp_key = (ngy_key[0], ngy_key[2])
    # value is list[gender, percent]
    ngy_key_m = (ngy_key[0], "M", ngy_key[2])
    ngy_key_f = (ngy_key[0], "F", ngy_key[2])
    percent = float(0)
    total = 0
    males = 0
    ngyp_value = []
    if ngy_key_m in names_gender_year:
        total = males = names_gender_year[ngy_key_m]
    if ngy_key_f in names_gender_year:
        total += names_gender_year[ngy_key_f]
    if males/total > 0.5:
        ngyp_value = ['M', males/total]
    else:
        ngyp_value = ['F', (1-males/total)]

    ngyp_dict[ngyp_key] = ngyp_value

for ng_key, ng_value in names_gender.items():
    # Key is name
    ngp_key = ng_key[0]
    # value is list[gender, percent]
    ng_key_m = (ng_key[0], "M")
    ng_key_f = (ng_key[0], "F")
    percent = float(0)
    total = 0
    males = 0
    ngp_value = []
    if ng_key_m in names_gender:
        total = males = names_gender[ng_key_m]
    if ng_key_f in names_gender:
        total += names_gender[ng_key_f]
    if males/total > 0.5:
        ngp_value = ['M', males/total]
    else:
        ngp_value = ['F', (1-males/total)]

    ngp_dict[ngp_key] = ngp_value

if names_gender_year:
    with open(os.path.join(namespath, 'names_gender_year.csv'), 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Gender', 'Year', 'Count'])
        for key, value in names_gender_year.items():
            # print("{}, {}, {}, {}".format(key[0], key[1], key[2], value))
            filewriter.writerow([key[0], key[1], key[2], str(value)])

if names_gender:
    with open(os.path.join(namespath, 'names_gender.csv'), 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Gender', 'Count'])
        for key, value in names_gender.items():
            # print("{}, {}, {}".format(key[0], key[1], value))
            filewriter.writerow([key[0], key[1], str(value)])

if ngp_dict:
    with open(os.path.join(namespath, 'names_gender_percent.csv'), 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Gender', 'Percent'])
        for key, value in ngp_dict.items():
            # print("{}, {}, {}".format(key[0], key[1], value))
            filewriter.writerow([key, str(value[0]), str(value[1])])

if ngyp_dict:
    with open(os.path.join(namespath, 'names_gender_year_percent.csv'), 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Name', 'Gender', 'Year', 'Percent'])
        for key, value in ngyp_dict.items():
            # print("{}, {}, {}".format(key[0], key[1], value))
            filewriter.writerow([key[0], str(value[0]), key[1], str(value[1])])
