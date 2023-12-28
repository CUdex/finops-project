import boto3

# AWS 접속을 위한 클라이언트 생성
ec2 = boto3.client('ec2', region_name='ap-northeast-2')

# EC2 볼륨 생성
volume = ec2.create_volume(
    AvailabilityZone='ap-northeast-2a',  # 서울 리전의 특정 가용 영역
    Size=30,  # 볼륨 크기 (GB 단위)
    VolumeType='gp2'  # 볼륨 타입 (예: gp2, io1 등)
)

print(volume)
