import boto3
from boto3  import client
from botocore.exceptions import ClientError

def s3cp(from_file, bucket, prefix_no_slash):
    #bucket='dev-rhassan'
    #prefix_no_slash='tony'
    objecta='{}/{}'.format(prefix_no_slash,from_file)
    s3 = boto3.client('s3')
    with open(from_file, "rb") as f:
        s3.upload_fileobj(f, bucket, objecta)

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
