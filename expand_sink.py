import shutil
import os

sourceDirectory = 'testDirectory/'
destDirectory = '../test/'

files = os.listdir(sourceDirectory)

for f in files:
        shutil.move('testDirectory/' + f, '../test')
