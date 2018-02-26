# import packages
import csv

# load csv and compile into list of lists
data_file = 'file_path'
with open(data_file, 'r') as f:
    reader = csv.reader(f) # reader is a special function that does the splitting on the commas for you
    rows = [row for row in reader]

# get rid of column headers
rows = rows[1:]

# replace specific values
rows[0][1] = '13-Jan-2018'
rows[1][1] = '14-Apr-2017'

# replace month values
# solution 1
for row_no, row in enumerate(rows):
    date = row[1]
    if 'Jan' in date:
        rows[row_no][1] = date.replace('Jan','01')
    if 'Feb' in date:
        rows[row_no][1] = date.replace('Feb','02')
    if 'Mar' in date:
        rows[row_no][1] = date.replace('Mar','03')
    if 'Apr' in date:
        rows[row_no][1] = date.replace('Apr','04')
    if 'May' in date:
        rows[row_no][1] = date.replace('May','05')
    if 'Jun' in date:
        rows[row_no][1] = date.replace('Jun','06')
    if 'Jul' in date:
        rows[row_no][1] = date.replace('Jul','07')
    if 'Aug' in date:
        rows[row_no][1] = date.replace('Aug','08')
    if 'Sep' in date:
        rows[row_no][1] = date.replace('Sep','09')
    if 'Oct' in date:
        rows[row_no][1] = date.replace('Oct','10')
    if 'Nov' in date:
        rows[row_no][1] = date.replace('Nov','11')
    if 'Dec' in date:
        rows[row_no][1] = date.replace('Dec','12')

# solution 2
dates = ['Jan','Feb','Mar','Apr','May','Jun',
         'Jul','Aug','Sep','Oct','Nov','Dec']

for row_no, row in enumerate(rows):
    for date_no, date in enumerate(dates):
        date_ = row[1]
        if date in date_:
            rows[row_no][1] = date_.replace(date, str(date_no+1))

# solution 3
months    = ['Jan','Feb','Mar','Apr','May','Jun',
             'Jul','Aug','Sep','Oct','Nov','Dec']

months_no = ['01','02','03','04','05','06',
             '07','08','09','10','11','12']

for row_no, row in enumerate(rows):
    for month_no, month in enumerate(months):
        for no_index, no_ in enumerate(months_no):
            month = row[1]
            if date in date_:
                rows[row_no][1] = date_.replace(date, str(date_no+1))

# best solution
months    = ['Jan','Feb','Mar','Apr','May','Jun',
             'Jul','Aug','Sep','Oct','Nov','Dec']

months_no = ['01','02','03','04','05','06',
             '07','08','09','10','11','12']

for row_no, row in enumerate(rows):
    for month_no, month in enumerate(months):
        month_ = row[1]
        if month in month_:
            rows[row_no][1] = month_.replace(month, months_no[month_no])

# convert standard date formate to new format
for row_no, row in enumerate(rows):
    date = row[1]
    val = rows[row_no][1]
    rows[row_no][1] = val.replace(val,('20' + val[-2:] + val[-6:-2] + val[-7] + 'T00:00:00'))

# turn the df into a dictionary
palantir_dict = {}

palantir_dict['column']         = [row[0] for row_no, row in enumerate(rows)]
palantir_dict['date']           = [row[1] for row_no, row in enumerate(rows)]
palantir_dict['something']      = [row[2] for row_no, row in enumerate(rows)]

# write to csv(?)
dict_data = {'key1': [1, 2, 3], 'key2': [4, 5, 6]}

with open("dict2csv.txt", 'w') as outfile:
   csv_writer = csv.writer(outfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

   for k,v in dict_data.items():
       csv_writer.writerow([k] + v)
