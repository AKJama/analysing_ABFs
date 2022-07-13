import pyabf

import os

import analysis_functions as af
import cursor

PATH_HERE = os.path.abspath(os.path.dirname(__file__))
PATH_PROJECT = os.path.abspath(PATH_HERE+"/../")
PATH_DATA = os.path.abspath(PATH_PROJECT+"/data/abfs") + "/"

day = '2021_08_05'
current_cell = 3
start = 17  # ID of the first file
end = 24  # ID of the final file

# file_ids in the correct format
iv_files = af.file_ids(day, start, end)[0]
cc_files = af.file_ids(day, start, end)[1]

for count, iv_file_name in enumerate(iv_files):
    path = PATH_DATA + day + "/" + iv_file_name + ".abf"
    abf = pyabf.ABF(path)  # One IV file
    for i in range(abf.sweepCount):
        abf.setSweep(i)  # One sweep
        y_data = abf.sweepY  # sweep y-axis data

        cursor_1 = cursor.Cursors(y_data, 298)
        cursor_2 = cursor.CursorB(y_data, 4181)

        cursor_1.get_vm()
        cursor_2.get_vm()

        cursor_2.get_diff_time(cursor_1)
        cursor_2.get_min(cursor_1)
