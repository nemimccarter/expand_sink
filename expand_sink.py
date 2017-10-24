import shutil
import os
import pandas as pd

# add generated contents to existing sink materials
# @pre:    newSink: newly-generated directory
#                   from which to move contents
#       masterSink: destination folder containing
#                   all sink materials

def expand_sink(newSink) :

    dataFrame = pd.read_csv(newSink)
    inchiSubstrates = dataFrame['Substrate InChI']
    inchiProducts = dataFrame['Product InChI']

    inchis = inchiSubstrates.append(inchiProducts)

    for row in inchis :
        print(row)
    
#    newFiles = os.listdir(newSink)

#    for f in newFiles:
#        shutil.move(newSink + f, masterSink)

fileName = '../RetroPath2.0/tutorial_data/naringenin/res_B/results.csv'

expand_sink(fileName)
