import boto3

session = boto3.Session(aws_access_key_id='AKIA4Z23VOJKQKSGF56I', aws_secret_access_key='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')
print(session)

s3 = session.resource('s3')
result = s3.Bucket('seu2022').upload_file('PCI.pdf', 'PCI_New_2.pdf')


#data = open('data.txt', 'rb')
#s3.Bucket('seu2022').put_object(Key='data.txt', Body=data)

