"""
Contains code to plot ABF data using pyABF and matplotlib
"""

import pyabf
import numpy as np
import matplotlib as plt

import os

import analysis_functions as af

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

# Plots
af.iv_plots(iv_files, current_cell, day, PATH_DATA)
af.cc_plots(cc_files, current_cell, day, PATH_DATA)
