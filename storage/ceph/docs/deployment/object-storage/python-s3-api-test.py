import boto
import boto.s3.connection
access_key = 'put your access key here!'
secret_key = 'put your secret key here!'

conn = boto.connect_s3(
        aws_access_key_id = 'XEF8FOL4SOCJNLFF3IDK',
        aws_secret_access_key = 'okdD1MQbKqm2DQKcS2zMhOxPZvtZpWWrQLwsvI4U',
        host = '192.168.88.244',
        is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )


# list buckets
# for bucket in conn.get_all_buckets():
#         print("{name}\t{created}".format(
#                 name = bucket.name,
#                 created = bucket.creation_date,
#         ))


# create bucket
bucket = conn.create_bucket('test-buck')

# list objs
for key in bucket.list():
        print("{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                ))

# create obj i bucket
# key = bucket.new_key('1234567890-hello.txt')
# key.set_contents_from_string('Hello World!')

# generate link to download obj
plans_key = bucket.get_key('12345hello.txt')
plans_url = plans_key.generate_url(3600, query_auth=True, force_http=True)
print(plans_url)