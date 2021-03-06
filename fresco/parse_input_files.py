import numpy as np

#Given an open file that maps group names to object names, get maps of group -> object, object -> group  
#Each line of the file should be a tab-separated list of names, where object names follow group name     
#For example:                                                                                            
#[GROUP NAME 1]\t[OBJECT NAME 1]\t[OBJECT NAME 2]                                                        
#[GROUP NAME 2]\t[OBJECT NAME 3]                                                                         
def read_split_file(split_file):
    group_to_object = {}
    object_to_group = {}

    while True:
        line = split_file.readline()
        if line == '':
            break
        entries = line.split('\t')
        group_to_object[entries[0]] = entries[1:]
        for obj in entries[1:]:
            object_to_group[obj] = entries[0]

    return group_to_object, object_to_group

def read_mapping_file(mapping_file):
    rows = [row for row in mapping_file]
    
    #first line describes the columns
    #ignore first letter (#)
    header = rows[0][1:]
    headerfields = header.split("\t")

    samplemap = {}
    
    for row in rows[1:]:
        fieldmap = {}
        fields = row.split("\t")
        for i in range(1, len(fields)):
            fieldmap[headerfields[i]] = fields[i]
        samplemap[fields[0]] = fieldmap
    
    return samplemap