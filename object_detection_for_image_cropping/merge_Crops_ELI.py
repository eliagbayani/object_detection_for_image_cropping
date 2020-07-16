# Jun 5 2020 - By Eli (copied from merge_tsvs.py)

import sys
import pandas as pd

# run command-line:
# python3 merge_Crops_ELI.py Lepidoptera 31
# python3 merge_Crops_ELI.py Aves 21
## Multitaxa batch:
# python3 merge_Crops_ELI.py Squamata 8
# python3 merge_Crops_ELI.py Coleoptera 9
# python3 merge_Crops_ELI.py Carnivora 3
# python3 merge_Crops_ELI.py Anura 4

print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
eli = sys.argv
# print('1st arg:', eli[0])
# print('2nd arg:', eli[1])
taxon = eli[1]
limit = eli[2]
limit = int(limit)
print('Taxon is:', taxon)
print('Limit count is:', limit)
listOfNotMultiTaxa = ["Aves", "Chiroptera", "Lepidoptera"]

# File names to be combined
#==========================================================================================================================
# this block not needed anymore...since 'limit' is now passed as a param.
# if taxon == 'Lepidoptera':
#     limit = 31
# elif taxon == 'Aves':
#     limit = 21
# else:
#     print("Will not go here...")

all_filenames = []
i = 1
while i <= limit:
    num_str = str(i).zfill(2)
    # print(num_str)
    # all_filenames.append("data_files/output/Lepidoptera/crops/lepidoptera_crops_rcnn_20000img_" + num_str + ".tsv") #lepidoptera_crops_rcnn_20000img_01.tsv
                                                                                                                      #       aves_crops_rcnn_20000img_01.tsv
    if taxon in listOfNotMultiTaxa :
        all_filenames.append("data_files/output/"+taxon+"/crops/"+taxon.lower()+"_crops_rcnn_20000img_" + num_str + ".tsv")
    else:
        all_filenames.append("data_files/output/Multitaxa/"+taxon+"/crops/"+taxon.lower()+"_crops_rcnn_i_20000img_" + num_str + ".tsv")
    i += 1
print(all_filenames)
#==========================================================================================================================

# Combine all files in the list
combined_csv = pd.concat([pd.read_csv(f, sep='\t', header=0) for f in all_filenames])

# Export to csv

if taxon in listOfNotMultiTaxa :
    combined_csv.to_csv( "data_files/output/"+taxon+"/crops/"+taxon.lower()+"_crops_rcnn_img.tsv", index=False, sep='\t')
else:
    combined_csv.to_csv( "data_files/output/Multitaxa/"+taxon+"/crops/"+taxon.lower()+"_crops_rcnn_i_img.tsv", index=False, sep='\t')
