import re
import os
fileNames = [ re.sub('\..*$', '', el) + '.txt' for el in os.listdir('.') ]
print(fileNames)
