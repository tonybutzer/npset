import os

fl = os.listdir('.')
rcp45_list = []
rcp85_list = []
missed = []

try:
    os.mkdir('./rcp85')
except:
    pass
try:
    os.mkdir('./rcp45')
except:
    pass

for f in fl:
    if f.split('.')[-1] != 'nc': continue
    if 'rcp45' in f: rcp45_list.append(f)
    elif 'rcp85' in f: rcp85_list.append(f)
    else: missed.append(f)
    
print('Files that will not be sorted : ', missed)


first_command = "mv ./{f1} ./{d}/{f2}"
d_count = 0
for d in ['rcp45','rcp85']:
    if d_count == 0 : this_list = rcp45_list
    else: this_list = rcp85_list
    for f in this_list:
        this = first_command.format(f1 = f, f2 = f, d = d)
        os.system(this)
        print(this)
    d_count += 1
    

    
    
    

