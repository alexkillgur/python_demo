import operator
import re
import csv
import os
import itertools

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

filename = "../HT_4/report/all_data.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)

field_names = ['line_id', 'marker', 'date_time', 'description']
file_writer = csv.DictWriter(open(filename, "w", newline=''),
                             delimiter=';', fieldnames=field_names)
file_writer.writeheader()

# write all_data.csv by markers
with open("openerp-server.log", "r") as log_file:
    line_id = 0
    for log_line in log_file:
        line_id += 1
        log_line = log_line.strip()
        if is_marker_exist(log_line):
            date_time, marker, description = parse_line(log_line)
            file_writer.writerow({'line_id': line_id,
                                  'marker': marker,
                                  'date_time': date_time,
                                  'description': description})

set_of_description = set()
unique_lines = []

file_reader = csv.DictReader(open(filename, 'r', newline=''),
                             delimiter=';', fieldnames=field_names)
for row in file_reader:
    if row['description'] not in set_of_description:
        print(row['line_id'])
        unique_lines.append(row)
        set_of_description.add(row['description'])

print(set_of_description)
print(unique_lines)