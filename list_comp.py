import re
import os
print( *[ 
                'mv ' + el + ' ' + re.sub('\..*$', '', el) + '.txt' 
                for el in os.listdir('.') 
                if not re.match("^\.", el) 
            ], sep='\n'
)