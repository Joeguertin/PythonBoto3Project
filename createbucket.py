import boto3
import random
import logging
import os

from botocore.exceptions import ClientError

s3 = boto3.resource('s3')

##input bucket name

bucktname = input("What is your buckets name?")
newBucket = s3.Bucket(bucktname)


## check the name to see if it already exists
def check_bucket():
    if newBucket.creation_date:
        print("Bucket name exists, pick new bucket name.")
        exit()
    else:
        print("Bucket  *", bucktname, "*  created")
        s3.create_bucket(Bucket=bucktname)
        print("successfully created",bucktname)

check_bucket()



##upload ballons.jpg and assign it a random ending to name
def upload():

    rand = random.randbytes(5)
    s3key = 'balloons' + '-' + str(rand)
    try:
        data = open('balloons.jpg', 'rb')
        s3.Bucket(bucktname).put_object(Key=s3key, Body=data)
    except ClientError as e:
        logging.error(e)
        return False
    return True

upload()



