# pymoodle_bulkfeedback

This repo contains a simple script to create a zip files containing student feedbacks for moodle assignment activities.

## Getting started

### Folder structure 

The folder `/pybulkfeedback` should be organized as follows:

```
├── export_zip.py
├── notes_moodle.csv // downloaded from moodle
├── result_list.csv
├── txt
│   ├── student1.txt
│   ├── ...
```

* `notes_moodle.csv`: this file should be downloaded from Moodle
    * In moodle, from the ‘Grading action’ drop-down list, select Download grading worksheet.
    * save the csv file as `notes_moodle.csv`.
* `txt`: a folder containing one feedback file for each student (txt, pdf, ...)
* `result_list.csv`: this file should contain the `email`,`filename`,`mark` for each student. Note that the email is used as a key to join the moodle worksheet and your feedback file.

### Create zip and result files

Run the python script.

```
$ python export_zip.py notes_moodle.csv
```

After the script execution, your folder should have the following structure

```
├── export_zip.py
├── moodle_assignements.zip // file to be uploaded in moodle
├── notes_moodle.csv
├── notes_moodle_result.csv
├── result_list.csv
├── txt
│   ├── student1.txt
│   ├── ...
└── zip
    ├── {student_name}_{moodleid}_assignsubmission_file_
    │   └── result.txt
    ├── ...
    │   └── ...
```

* In Moodle, go to your Assignment activity and click on View all submissions.
* From the ‘Grading action’ drop-down list at the top of the page, select Upload multiple feedback files in a zip and select the the file `moodle_assignements.zip`.

## Example

The folder `/pymoodle_bulkfeedback` contains a simple example. To run this example, go to this folder and the run 

```
$ python export_zip.py notes_moodle.csv
```