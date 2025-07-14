import hmac
from hashlib import sha256

def generate_hmac(message:str, secret: str):
    byte_key = secret.encode("utf-8")
    byte_message = message.encode("utf-8")

    hmac_object = hmac.new(key=byte_key, msg=byte_message, digestmod=sha256)
    return hmac_object.hexdigest()
