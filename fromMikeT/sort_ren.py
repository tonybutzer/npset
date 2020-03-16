
# Only run this in the individual param folders, e.g. tasmax, tasmin, pr
import os
import numpy as np

def fixlen(s):
    s = str(s)
    if len(s) == 1: s = '0' + s
    return s

fl = os.listdir('.')
fl = [x for x in fl if x.split('.')[-1] == 'nc']
#print(fl)

# Years might not always be in same position in filename.

test_filename = fl[0]
print('!***',test_filename)
index = 0
parts = test_filename.split('_')
for item in parts:
    #print(item)
    try:
        x = int(item)
    except:
        index +=1
        continue
    if 1900 < x < 3000:
        final_index = index
        break
    else:
        index +=1

print('First year index = ',final_index)

final_files = []
the_years = []
for f in fl:
    try:
        this_year = int(f.split('_')[final_index])
    except:
        continue
    final_files.append(f)
    the_years.append(this_year)
    
final_files = np.array(final_files)
the_years = np.array(the_years)
print(the_years)

indices = np.argsort(the_years)
final_files = final_files[indices]

i = 1
for f in final_files:
    new_name = fixlen(i) + '_' + f
    os.rename(f,new_name)
    print(f,new_name)
    i+=1
    

        
    





