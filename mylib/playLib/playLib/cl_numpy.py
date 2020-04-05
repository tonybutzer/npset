import numpy as np
from s3fs.core import S3FileSystem


def np_load_cloud(bucket_file):

    s3 = S3FileSystem()

    ARY = np.load(s3.open(bucket_file))
    ARY[(ARY < 0)] = 0

    ARY = np.flip(ARY, axis=0)

    return ARY


