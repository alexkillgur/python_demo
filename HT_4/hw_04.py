import re
import csv
import os

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


# with open('all_data.csv', 'w') as csvfile:
    # file_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    # file_writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # file_writer = csv.writer(csvfile, delimiter=',', quotechar='|')
    # file_writer = csv.writer(csvfile, delimiter=',')

filename = "../HT_4/report/all_data.csv"
os.makedirs(os.path.dirname(filename), exist_ok=True)

file_writer = csv.writer(open(filename, "w", newline=''), delimiter=';')

with open("openerp-server.log", "r") as log_file:
    line_id = 0
    for log_line in log_file:
        line_id += 1
        log_line = log_line.strip()
        if is_marker_exist(log_line):
            # print(log_line)
            date_time, marker, description = parse_line(log_line)
            # print(str(line_id) + " " + str(date_time) + " " + str(marker) + " " + str(description))
            file_writer.writerow([line_id, marker, date_time, description])



