from boto3.session import Session
from mypy_boto3_ec2 import EC2Client
from mypy_boto3_ec2.type_defs import VolumeTypeDef
from resources.base import LIST_FUNC, ResourceBase, TagResultType

class EC2Volume(ResourceBase):
    def __init__(self, svc: EC2Client, volume: VolumeTypeDef):
        self.svc: EC2Client = svc
        self.volume = volume

    def delete(self):
        try:
            self.svc.delete_volume(VolumeId=self.volume['VolumeId'])
        except Exception as e:
            return e
        return None

    def __str__(self):
        return self.volume['VolumeId']
    
    @property
    def tags(self) -> TagResultType:
        return self.volume.get('Tags', [])

def list_ec2_volumes(sess: Session):
    svc = sess.client("ec2")

    interator = svc.get_paginator("describe_volumes").paginate(
        Filters=[
            {
                'Name': 'status',
                'Values': [
                    'available',
                ],
            },
        ],
    )

    return (EC2Volume(svc, volume) 
            for volumes in interator 
            for volume in volumes["Volumes"]
            )

if __name__ != "__main__":
    LIST_FUNC.append(list_ec2_volumes)