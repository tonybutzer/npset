#Put this in the /rcp45 and /rcp58 folders
import os

fl = os.listdir('.')
tasmax_list = []
tasmin_list = []
pr_list = []
missed = []

try:
    os.mkdir('./tasmax')
except:
    pass
try:
    os.mkdir('./tasmin')
except:
    pass
try:
    os.mkdir('./pr')
except:
    pass

for f in fl:
    if f.split('.')[-1] != 'nc': continue
    if 'tasmax' in f: tasmax_list.append(f)
    elif 'tasmin' in f: tasmin_list.append(f)
    elif '_pr_' in f: pr_list.append(f)
    else: missed.append(f)
    
print('Files that will not be sorted : ', missed)


first_command = "mv ./{f1} ./{d}/{f2}"
d_count = 0
for d in ['tasmax','tasmin','pr']:
    if d_count == 0 : this_list = tasmax_list
    elif d_count == 1: this_list = tasmin_list
    else: this_list = pr_list
    for f in this_list:
        this = first_command.format(f1 = f, f2 = f, d = d)
        os.system(this)
        print(this)
    d_count += 1
    

    
    
    

