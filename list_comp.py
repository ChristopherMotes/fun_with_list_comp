import re
import os
fileNames = [ re.sub('\..*$', '', el) + '.txt' for el in os.listdir('.') if not re.match("^\.", el) ]
print(fileNames)
