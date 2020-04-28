import subprocess
def subprocess_cmd(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    stupidBytesObject = proc_stdout
    outStr = (stupidBytesObject.decode("utf-8"))
    print(outStr)
    return(outStr)

def proc_du(du_in):
    size_dict={}
    lines = du_in.split('\n')
    for line in lines:
        #print('LINE ', line)
        key = line.split('/')[-1]
        # print(key)
        gigs = line.split('\t')[0]
        if ('M' in gigs):
            gigs = gigs[0:-1]
            gigs = float(gigs)
            gigs = gigs/1000
            gigs = str(gigs) + 'G'
            print('NEW ', gigs)
        if ('G' in gigs):
            gigs = gigs[0:-1]
            gigs = float(gigs)
            # print(gigs)
            if (key == ''):
                key = 'TOTAL'
            size_dict[key]=gigs
    return size_dict