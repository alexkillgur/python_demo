import csv
import os
import re

MARKERS = ("WARNING", "ERROR", "CRITICAL")


def is_marker_exist(line):
    for marker in MARKERS:
        if line.find(marker) != -1:
            return True
    return False


def parse_line(line):
    # parse date_time
    match = re.search(r'(?P<date_time>\d{4}[-/]\d{2}[-/]\d{2} \d{2}:\d{2}:\d{2})', line)
    date_time = match.group("date_time")
    # parse marker
    marker = re.findall(r"(?=("+'|'.join(MARKERS)+r"))", line)[0]
    # parse description
    description = re.sub(r'^\W*\w+\W*', '', line.split(marker)[-1].strip())
    return date_time, marker, description


def get_dict(line_id, date_time, marker, description):
    return {'line_id': line_id,
            'marker': marker,
            'date_time': date_time,
            'description': description}


def count(all_lines, line):
    counter = 0
    for current_line in all_lines:
        if current_line['description'] == line:
            counter += 1
    return counter

# create all_data.csv
filename_for_all = "../HT_4/report/all_data.csv"
os.makedirs(os.path.dirname(filename_for_all), exist_ok=True)
field_names = ['line_id', 'marker', 'date_time', 'description']
file_writer = csv.DictWriter(open(filename_for_all, "w", newline=''), delimiter=';', fieldnames=field_names)
file_writer.writeheader()

# array for counting duplicates
all_lines = []

# write all_data.csv by markers
with open("openerp-server.log", "r") as log_file:
    line_id = 0
    for log_line in log_file:
        line_id += 1
        log_line = log_line.strip()
        if is_marker_exist(log_line):
            # get parsing parameters
            date_time, marker, description = parse_line(log_line)
            # get dictionary to write
            dictionary = get_dict(line_id, date_time, marker, description)
            file_writer.writerow(dictionary)
            # fill array for counting duplicates
            all_lines.append(dictionary)

# array for unique description for counting duplicates
set_of_description = []

# create unique.csv
filename_for_unique = "../HT_4/report/unique.csv"
field_names = ['count', 'marker', 'date_time', 'description']
file_writer = csv.DictWriter(open(filename_for_unique, "w", newline=''), delimiter=';', fieldnames=field_names)
file_writer.writeheader()

# read all_data.csv and write unique.csv
file_reader = csv.DictReader(open(filename_for_all, 'r', newline=''), delimiter=';')
for row in file_reader:
    if row['description'] not in set_of_description:
        set_of_description.append(row['description'])
        file_writer.writerow({'count': count(all_lines, row['description']),
                              'marker': row['marker'],
                              'date_time': row['date_time'],
                              'description': row['description']})
