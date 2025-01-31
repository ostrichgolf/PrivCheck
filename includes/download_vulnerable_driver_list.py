import csv
import sys
from urllib.request import urlopen, Request

if len(sys.argv) > 1:
    OUTPUT_PATH = sys.argv[1]
else:
    OUTPUT_PATH = "."

CSV_FILE = OUTPUT_PATH + "/drivers.csv"
HASH_OUTPUT_FILE = OUTPUT_PATH + "/vulndrivers.h"

# Download CSV with all vulnerable hashes
driverreq = Request("https://www.loldrivers.io/api/drivers.csv")
try:
    with urlopen(driverreq) as response:
        if response.getcode() == 200:
            with open(CSV_FILE, "wb") as file:
                file.write(response.read())
        else:
            print(f"Request failed with status code: {response.getcode()}")
except Exception as e:
    print(f"An error occured: {e}")


# Extract relevant hashes
hashes = set()

with open(CSV_FILE, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Check if 'Category' matches
        category = row.get("Category", "").strip().lower()
        if category in ["vulnerable driver", "vulnerable drivers"]:
            # Collect SHA1, SHA256 and MD5 hashes if present
            sha1_hash = row.get("KnownVulnerableSamples_SHA1", "").strip().upper()
            sha256_hash = row.get("KnownVulnerableSamples_SHA256", "").strip().upper()
            md5_hash = row.get("KnownVulnerableSamples_MD5", "").strip().upper()

            # Add hashes to the set (to ensure uniqueness)
            if sha1_hash:
                hashes.update(sha1_hash.split(','))
            if sha256_hash:
                hashes.update(sha256_hash.split(','))
            if md5_hash:
                hashes.update(md5_hash.split(','))


# Format as C array in header file
with open(HASH_OUTPUT_FILE, 'w') as file:
    file.write("#include <windows.h>\n")
    file.write("#ifndef VULNDRIVERS_H\n")
    file.write("#define VULNDRIVERS_H\n\n")
    file.write("const char* VulnerableHashes[] = {\n")

    for hash_value in sorted(hashes):
        hash_value = hash_value.strip()
        if hash_value:  # Ignore empty values
            file.write(f'    "{hash_value}",\n')

    file.write("    NULL // End of array\n")
    file.write("};\n\n")
    file.write("#endif // VULNDRIVERS_H\n")
    file.close()

print(f"Hashes extracted and saved to {HASH_OUTPUT_FILE}")