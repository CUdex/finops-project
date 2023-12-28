import boto3
from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.type_defs import VolumeTypeDef
from resources.base import LIST_FUNC

class EC2Volume:
    def __init__(self, sess: EC2Client, volume: VolumeTypeDef):
        self.sess: EC2Client = sess
        self.volume = volume

    def delete(self):
        try:
            self.sess.delete_volume(VolumeId=self.volume['VolumeId'])
        except Exception as e:
            return e
        return None

    def __str__(self):
        return self.volume['VolumeId']

def list_ec2_volumes(region: str = "ap-northeast-2"):
    sess = boto3.client(
        "ec2",
        region_name = region
    )

    interator = sess.get_paginator("describe_volumes").paginate(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ],
            },
        ],
    )

    return (EC2Volume(sess, volume) for volumes in interator for volume in volumes["Volumes"])

if __name__ != "__main__":
    LIST_FUNC.append(list_ec2_volumes)