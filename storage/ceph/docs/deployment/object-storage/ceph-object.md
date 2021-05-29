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