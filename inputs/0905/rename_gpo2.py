#This script renames the files for the short names used in the notebooks

import os

# define the list of prefixes to match and the corresponding replacements
prefixes = ["Cab","Cul", "Guas", "Guay", "Herm", "Maz","Moch","Nav", "Nog","Obr"]
replacements = ["Cab_","Cul_", "Guas_","Guay_", "Herm_", "Maz_","Moch_","Nav_", "Nog_","Obr_"]

# loop through each file in the directory
for filename in os.listdir():
    # check if the file matches any of the prefixes
    for prefix, replacement in zip(prefixes, replacements):
        if filename.startswith(prefix):
            # construct the new filename using the replacement prefix
            
            last_8_digits = filename[-12:-4]
            new_filename = replacement + last_8_digits + ".csv"
            # rename the file
            os.rename(filename, new_filename)
            # print a message to confirm the file was renamed
            print(f"Renamed {filename} to {new_filename}")


