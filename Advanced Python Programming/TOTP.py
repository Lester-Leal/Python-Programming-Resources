# Emulates behavior of an authenticator app like Google Authenticator
# Sample usage:
# '''
# Provider [...Facebook, Google]: Facebook
# Secret Key: I3LQHRSPGB72JUSD5FAPJVDL75D5I4IL
# TOTP:  618282
# '''

# Author: Jorn Blaedel Garbosa

import hashlib
import hmac
import struct
import time
import base64


def generate_totp(secret_key, digits=6, time_interval=30):
    # Get the current Unix time
    current_time = int(time.time())

    # Calculate the number of time intervals that have elapsed since the Unix epoch
    time_steps = current_time // time_interval

    # Convert the time steps to a byte string
    time_steps_bytes = struct.pack(">Q", time_steps)

    # Compute the HMAC-SHA1 hash using the secret key and time steps
    hmac_sha1 = hmac.new(base64.b32decode(secret_key),
                         time_steps_bytes, hashlib.sha1).digest()

    # Get the offset value from the last 4 bits of the hash
    offset = hmac_sha1[-1] & 0x0F

    # Get the 4 bytes at the specified offset
    truncated_hash = hmac_sha1[offset:offset + 4]

    # Convert the truncated hash to an integer
    totp = struct.unpack(">L", truncated_hash)[0] & 0x7FFFFFFF

    # Normalize the TOTP to the desired length
    totp %= 10**digits

    # Convert the TOTP to a string
    totp_str = str(totp).zfill(digits)

    return totp_str


str(input("Provider [...Facebook, Google]: "))

secret_key = str(input("Secret Key: "))

print("TOTP: ", generate_totp(secret_key=secret_key))
