#Check string patrren 

import re
def isallowed(str):
    charcheck = re.compile(r'[^a-zA-Z0-9]')
    str = charcheck.search(str)
    return  bool(str)
print(isallowed("#####%&^&"))