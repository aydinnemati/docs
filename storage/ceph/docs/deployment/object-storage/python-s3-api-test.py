import boto
import boto.s3.connection
access_key = 'CORG59IYDX6CRTBUX83V'
secret_key = 'bp5AqTgytGeTKr6tkUXoGFrp5oNZu20RxX1NUO99'

conn = boto.connect_s3(
        aws_access_key_id = 'GOFWEDL1YNMLENR0FJWB',
        aws_secret_access_key = 'nBfT0X9maPaMADtaR8vnFTmllAz6TEKCBHBqw0Dg',
        host = '10.0.23.7',
        is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )
print("=====================")
print(conn)
print("=====================")
# list buckets
# for bucket in conn.get_all_buckets():
#         print("{name}\t{created}".format(
#                 name = bucket.name,
#                 created = bucket.creation_date,
#         ))


# create bucket
bucket = conn.create_bucket('test-bsdasduck')

# # list objs
for key in bucket.list():
        print("{name}\t{size}\t{modified}".format(
                name = key.name,
                size = key.size,
                modified = key.last_modified,
                ))

# # create obj i bucket
# # key = bucket.new_key('1234567890-hello.txt')
# # key.set_contents_from_string('Hello World!')

# # generate link to download obj
# plans_key = bucket.get_key('12345hello.txt')
# plans_url = plans_key.generate_url(3600, query_auth=True, force_http=True)
# print(plans_url)