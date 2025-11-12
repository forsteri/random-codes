import boto3

# AssumeRoleを実施
session = boto3.Session(profile_name="admin")

# 目的の処理を実行
s3 = session.client("s3")
response = s3.list_buckets()
print(response)
