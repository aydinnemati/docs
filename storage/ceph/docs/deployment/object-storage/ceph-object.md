# using s3 api with curl
see [redhat.com](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/4/html/developer_guide/ceph-object-gateway-and-the-s3-api) 
# using swift api with curl
see [redhat.com](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/4/html/developer_guide/ceph-object-gateway-and-the-swift-api)

# Object Gateway Guide for Red Hat Enterprise Linux
see [redhat.com](https://access.redhat.com/documentation/en-us/red_hat_ceph_storage/3/html-single/object_gateway_guide_for_red_hat_enterprise_linux/index)

# Ceph Object Gateway
see [python](./python-s3-api-test.py)





# auth  
- see [amazon](https://docs.aws.amazon.com/AmazonS3/latest/userguide/RESTAuthentication.html#ConstructingTheAuthenticationHeader)

```bash
Authorization = "AWS" + " " + AWSAccessKeyId + ":" + Signature;

Signature = Base64( HMAC-SHA1( UTF-8-Encoding-Of(YourSecretAccessKey), UTF-8-Encoding-Of( StringToSign ) ) );

StringToSign = HTTP-Verb + "\n" +
	Content-MD5 + "\n" +
	Content-Type + "\n" +
	Date + "\n" +
	CanonicalizedAmzHeaders +
	CanonicalizedResource;

CanonicalizedResource = [ "/" + Bucket ] +
	<HTTP-Request-URI, from the protocol name up to the query string> +
	[ subresource, if present. For example "?acl", "?location", or "?logging"];

CanonicalizedAmzHeaders = <described below>
```
# Authentication

- Authenticating a request requires including an access key and a Hash-based Message Authentication Code (HMAC) in the request before it is sent to the RGW server. RGW uses an S3-compatible authentication approach.
```
HTTP/1.1
PUT /buckets/bucket/object.mpeg
Host: cname.domain.com
Date: Mon, 2 Jan 2012 00:01:01 +0000
Content-Encoding: mpeg
Content-Length: 9999999

Authorization: AWS {access-key}:{hash-of-header-and-secret}
```

- In the foregoing example, replace {access-key} with the value for your access key ID followed by a colon (:). Replace {hash-of-header-and-secret} with a hash of the header string and the secret corresponding to the access key ID.

- To generate the hash of the header string and secret, you must:

1. Get the value of the header string.

2. Normalize the request header string into canonical form.

3. Generate an HMAC using a SHA-1 hashing algorithm. See RFC 2104 and HMAC for details.

4. Encode the hmac result as base-64.

- To normalize the header into canonical form:

1. Get all fields beginning with x-amz-.

2. Ensure that the fields are all lowercase.

3. Sort the fields lexicographically.

4. Combine multiple instances of the same field name into a single field and separate the field values with a comma.

5. Replace white space and line breaks in field values with a single space.

6. Remove white space before and after colons.

8. Append a new line after each field.

9. Merge the fields back into the header.

Replace the {hash-of-header-and-secret} with the base-64 encoded HMAC string.