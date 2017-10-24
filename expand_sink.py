import sys
import pandas as pd

# add generated contents to existing sink materials
# @pre:    newSink: newly-generated directory
#                   from which to move contents
#       masterSink: destination folder containing
#                   all sink materials

def expand_sink(newSink, masterSink) :

    # open new sink csv and extract InChi columns
    dataFrame = pd.read_csv(newSink)
    inchiSubstrates = dataFrame['Substrate InChI']
    inchiProducts = dataFrame['Product InChI']

    # combine InChis into one column
    inchisSeries = inchiSubstrates.append(inchiProducts)

    # convert to dataframe for appending to master sink
    inchis = inchisSeries.to_frame()

    # append to master sink
    inchis.insert(0, '', '')
    with open('masterSink.csv', 'a') as f:
        inchis.to_csv(f, index=False)


#fileName = '../RetroPath2.0/tutorial_data/naringenin/res_B/results.csv'
#oldSink = './masterSink.csv'
if (len(sys.argv) > 3) :
    print("Error: Too many arguments:\n")
    print("Please provide only a newSink and a masterSink")
    sys.exit(1)

newSink = sys.argv[1]
masterSink = sys.argv[2]
expand_sink(newSink, masterSink)
