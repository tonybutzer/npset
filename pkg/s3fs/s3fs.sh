#! /bin/bash
REGION=us-west-2

sudo s3fs -o allow_other -o iam_role="csr-Ec2-Role" \
-o use_cache=/tmp \
-o url="https://s3-$REGION.amazonaws.com" \
-o umask=0227,uid=1000 \
-o nonempty	\
	dev-et-data /opt/et_data


# some debug options
# -o dbglevel=info -f \
# -o curldbg \
