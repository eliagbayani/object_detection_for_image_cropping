# Merge tsv files resulting from object detection of batch images
# 28 Apr 2020

import sys
import pandas as pd

# run command-line:
# python3 merge_Crops_ELI.py Lepidoptera

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
eli = sys.argv
# print('1st arg:', eli[0])
# print('2nd arg:', eli[1])
taxon = eli[1]
print('Taxon is:', taxon)


# File names to be combined
#==========================================================================================================================
if taxon == 'Lepidoptera':
    all_filenames = []
    i = 1
    while i <= 31:
        num_str = str(i).zfill(2)
        # print(num_str)
        all_filenames.append("data_files/output/Lepidoptera/crops/lepidoptera_crops_rcnn_20000img_" + num_str + ".tsv") #lepidoptera_crops_rcnn_20000img_01.tsv
        i += 1
    print(all_filenames)
else:
    print("Will not go here...")
#==========================================================================================================================

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='\t', header=0) for f in all_filenames])

# Export to csv
combined_csv.to_csv( "data_files/output/"+taxon+"/crops/"+taxon.lower()+"_crops_rcnn_img.tsv", index=False, sep='\t')
