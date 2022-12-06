# HOW: python HashGeneratorpy --file <file_path> --hash <md5|sha1|sha256|sha512>
# A Python script that can generate the MD5, SHA1, SHA256, and SHA512 hashes of
# a file specified by the user. The user can specify the file path and the hash
# function to use by using the '--file' and '--hash' flags, respectively.
# Author: Jorn Blaedel Garbosa


import sys
import hashlib


def generate_md5(file_path: str) -> str:
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file content and calculate the MD5 hash
        data = f.read()
        md5 = hashlib.md5(data).hexdigest()

    return md5


def generate_sha1(file_path: str) -> str:
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file content and calculate the SHA1 hash
        data = f.read()
        sha1 = hashlib.sha1(data).hexdigest()

    return sha1


def generate_sha256(file_path: str) -> str:
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file content and calculate the SHA256 hash
        data = f.read()
        sha256 = hashlib.sha256(data).hexdigest()

    return sha256


def generate_sha512(file_path: str) -> str:
    # Open the file in binary mode
    with open(file_path, 'rb') as f:
        # Read the file content and calculate the SHA512 hash
        data = f.read()
        sha512 = hashlib.sha512(data).hexdigest()

    return sha512


def main():
    # Parse the command-line arguments
    file_path = None
    hash_func = None
    for i in range(1, len(sys.argv), 2):
        flag = sys.argv[i]
        if flag == '--help':
            print(
                '\033[32m\nUsage: python HashGenerator.py --file <file_path> --hash <md5|sha1|sha256|sha512>\n')
            return
        value = sys.argv[i + 1]
        if flag == '--file':
            file_path = value
        elif flag == '--hash':
            hash_func = value
        else:
            print(f'\033[31mUnknown flag: {flag}')
            return

    # Check if the file path and hash function were specified
    if file_path is None:
        print('\033[31m\nPlease specify a file path using the --file flag.\n')
        return
    if hash_func is None:
        print('\033[31m\nPlease specify a hash function using the --hash flag.\n')
        return

    # Generate the hash of the specified file using the specified function
    if hash_func == 'md5':
        hash = generate_md5(file_path)
    elif hash_func == 'sha1':
        hash = generate_sha1(file_path)
    elif hash_func == 'sha256':
        hash = generate_sha256(file_path)
    elif hash_func == 'sha512':
        hash = generate_sha512(file_path)
    else:
        print(f'Unknown hash function: {hash_func}')
        return

    print(f'{hash_func.upper()} hash of {file_path}: {hash}')


if __name__ == '__main__':
    main()
