# Merge tsv files resulting from object detection of batch images
# 11 Feb 20

import sys
import pandas as pd

# run command-line:
# python3 merge_tsvs_ELI.py 1 Lepidoptera
# python3 merge_tsvs_ELI.py 2 Lepidoptera
# python3 merge_tsvs_ELI.py 31 Lepidoptera

# python3 merge_tsvs_ELI.py 1 Chiroptera


print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
eli = sys.argv
# print('1st arg:', eli[0])
# print('2nd arg:', eli[1])
num = int(eli[1])
num_str = str(num).zfill(2)
taxon = eli[2]
print('Number is:', num, ' - ', num_str)
print('Taxon is:', taxon)


# File names to be combined
# all_filenames = ["chiroptera_det_crops_20000_a.tsv", "chiroptera_det_crops_20000_b.tsv", "chiroptera_det_crops_20000_c.tsv", "chiroptera_det_crops_20000_d.tsv"]

# all_filenames = ["data_files/input/Lepidoptera/collab/temp1/lepidoptera_det_crops_20000_a.tsv",
#                  "data_files/input/Lepidoptera/collab/temp1/lepidoptera_det_crops_20000_b.tsv"]

if taxon == 'Chiroptera':
    if num == 1:
        all_filenames = ["data_files/input/"+taxon+"/collab/temp" + str(num) + "/"+taxon.lower()+"_det_crops_20000_a.tsv",
                         "data_files/input/"+taxon+"/collab/temp" + str(num) + "/"+taxon.lower()+"_det_crops_20000_b.tsv",
                         "data_files/input/"+taxon+"/collab/temp" + str(num) + "/"+taxon.lower()+"_det_crops_20000_c.tsv"]

if taxon == 'Lepidoptera':
    if num >= 1 and num <= 2:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv"]
    elif num >= 3 and num <= 12:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_c.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_d.tsv"]
    elif num >= 13 and num <= 19:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv"]
    elif num == 20:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_c.tsv"]
    elif num == 21:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv"]
    elif num == 22:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_c.tsv"]
    elif num >= 23 and num <= 31:
        all_filenames = ["data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_a.tsv",
                         "data_files/input/Lepidoptera/collab/temp" + str(num) + "/lepidoptera_det_crops_20000_b.tsv"]
    else:
        print("Will not go here...")


# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='\t', header=0) for f in all_filenames])

# Export to csv
# combined_csv.to_csv( "chiroptera_det_crops_20000.tsv", index=False, sep='\t')

combined_csv.to_csv( "data_files/input/"+taxon+"/final/"+taxon.lower()+"_det_crops_20K_" + num_str + ".tsv", index=False, sep='\t')

# combined_csv.to_csv( "data_files/input/Lepidoptera/final/lepidoptera_det_crops_20000_01.tsv", index=False, sep='\t')
# combined_csv.to_csv( "data_files/input/Lepidoptera/final/lepidoptera_det_crops_20000_02.tsv", index=False, sep='\t')
# combined_csv.to_csv( "data_files/input/Lepidoptera/final/lepidoptera_det_crops_20000_03.tsv", index=False, sep='\t')
