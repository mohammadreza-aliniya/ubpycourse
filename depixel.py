import os
import sys
for count in sys.argv[1:]:
    os.system("potrace -b svg -b pdf"+str(count))
    print("proccess finished")
