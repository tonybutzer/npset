import os
import subprocess
import boto3
from boto3  import client
from botocore.exceptions import ClientError

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    stupidBytesObject = proc_stdout
    outStr = (stupidBytesObject.decode("utf-8"))
    #print(outStr)
    return(outStr)

def s3cp(fromfile, tofile):
        print ("hello from s3get copying file " + fromfile)
        infile = fromfile
        outfile = tofile
        pushcmd = "aws s3 cp %s %s" % (infile, outfile)
        print (pushcmd)
        subprocess_cmd(pushcmd)

def bo_get_bucket_list(bucket_name, prefix):

    print("my prefix",prefix)
    if '/' in prefix[-1]:
        print("prefix contains slash")
    else:
        print("prefix does not contains slash")
        prefix = prefix + '/'

    s3_conn   = client('s3')  # type: BaseClient  ## again assumes boto.cfg setup, assume AWS S3
    s3_result =  s3_conn.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter = "/")

    if 'Contents' not in s3_result:
        #print(s3_result)
        return []

    file_list = []
    for key in s3_result['Contents']:
        file_list.append(key['Key'])
    # print(f"List count = {len(file_list)}")

    while s3_result['IsTruncated']:
        continuation_key = s3_result['NextContinuationToken']
        s3_result = s3_conn.list_objects_v2(Bucket=bucket_name, Prefix=prefix, Delimiter="/", ContinuationToken=continuation_key)
        for key in s3_result['Contents']:
            file_list.append(key['Key'])
    print(f"List count = {len(file_list)}")
    return file_list
