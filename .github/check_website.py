import hashlib
import requests

def get_webpage_hash(url):
    response = requests.get(url)
    content = response.text
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

url = "https://docs.sqd.dev/subsquid-network/participate/worker/"
hash_file = ".github/checksum"

if __name__ == "__main__":
    try:
        with open(hash_file, "r") as f:
            old_hash = f.read()
    except FileNotFoundError:
        old_hash = ""

    new_hash = get_webpage_hash(url)

    if new_hash != old_hash:
        print("Website has changed!")
        with open(hash_file, "w") as f:
            f.write(new_hash)
    else:
        print("No changes detected.")
