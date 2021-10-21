import jwt
import datetime
import time

key = "my-secret-key"
encoded = jwt.encode({"name": "Manan Chakma"}, key, algorithm="HS256")
print(f"Endoded: {encoded}")
decoded = jwt.decode(encoded, key, algorithms="HS256")
print(decoded)



encoded = jwt.encode({"name": "Manan Chakma", "exp": datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(seconds=5)}, key, algorithm="HS256")
print(f"Endoded: {encoded}")
decoded = jwt.decode(encoded, key, algorithms="HS256")
print(decoded)

time.sleep(10)

decoded = jwt.decode(encoded, key, algorithms="HS256")
print(decoded) # jwt.exceptions.ExpiredSignatureError: Signature has expired


# registered claim names

# exp (expiration time) claim
# nbf (not before time) claim - the nbf claim identifies the time before which the jwt must not be accepted for processing
# iss (issuer) claim
# aud (Audiance) claim
# iat (issued at) claim - the iat claim identifies the time at which the jwt was issued
# examples - https://pyjwt.readthedocs.io/en/latest/usage.html#issuer-claim-iss




