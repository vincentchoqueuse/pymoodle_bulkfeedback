import os
import shutil
import argparse
import csv

# parameters
zip_folder = "zip"
zip_filename = "moodle_assignements"
result_filename = "result_list.csv"

parser = argparse.ArgumentParser(description='Create a zip file that can be imported in moodle from a pdf folder.')
parser.add_argument('filename', metavar='filename', type=str, help='the moodle csv file for assignement')
args = parser.parse_args()
moodle_filename = args.filename

# extract dict for result_list
result_dict = {}
csvreader = csv.reader(open(result_filename, "r"), delimiter=",")
next(csvreader)
for row in csvreader:
    email = row[0]
    result_dict[email] = {"filename": row[1], "mark": row[2]}

# extract dict for moodle_list
moodle_dict = {}
csvreader = csv.reader(open(moodle_filename, "r"), delimiter=",")
next(csvreader)
for row in csvreader:
    email = row[2]
    id_moodle = row[0].replace("Participant", "")
    foldername = "{}/{}_{}_assignsubmission_file_".format(zip_folder, row[1], id_moodle)
    moodle_dict[email] = {"foldername": foldername, "student": row[1], "mark": row[2]}

# create zip directory
os.makedirs(zip_folder, exist_ok=True)

# move file to zip folder
print("1. Export files to zip folder ({} files)".format(len(result_dict)))
for email in result_dict:
    try:
        dst_dirname = moodle_dict[email]["foldername"]
        extension = os.path.splitext(result_dict[email]["filename"])[1]
        print("  - {}".format(moodle_dict[email]["student"]))
        src_file = "{}".format(result_dict[email]["filename"])
        dst_file = "{}/result{}".format(dst_dirname, extension)
        os.makedirs(dst_dirname, exist_ok=True)
        shutil.copyfile(src_file, dst_file)
    except KeyError:
        print("  - warning: student with email {} not found".format(email))

# convert zip folder to a zip file
print("2. Create file {}.zip".format(zip_filename))
shutil.make_archive(zip_filename, "zip", "zip")

# create result file
output_filename = moodle_filename.replace(".csv", "_result.csv")
print("3. Export result to file: {}".format(output_filename))
csvwriter = csv.writer(open(output_filename, "w"), delimiter=",")

output = ""
csvreader = csv.reader(open(moodle_filename, "r"), delimiter=",")
for index, row in enumerate(csvreader):
    if index > 0:
        try:
            email = row[2]
            mark = result_dict[email]["mark"]
            row[4] = "{}".format(float(mark)).replace(".", ",")
        except KeyError:
            print("  - warning: mark not found for {}".format(moodle_dict[email]["student"]))
    csvwriter.writerow(row)

print("\n-> Upload the file {}.zip in moodle to send the feedback to students".format(zip_filename))
