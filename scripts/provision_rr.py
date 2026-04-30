import os
import urllib.request
import zipfile
import shutil

RR_URL = "https://github.com/GuntherRademacher/rr/releases/download/v1.63/rr-1.63-java8.zip"
RR_ZIP = "rr.zip"
RR_WAR = "rr.war"

def provision_rr():
    if os.path.exists(RR_WAR):
        print(f"{RR_WAR} already exists.")
        return

    print(f"Downloading {RR_URL}...")
    urllib.request.urlretrieve(RR_URL, RR_ZIP)

    print(f"Extracting {RR_ZIP}...")
    with zipfile.ZipFile(RR_ZIP, 'r') as zip_ref:
        zip_ref.extractall(".")

    if os.path.exists(RR_ZIP):
        os.remove(RR_ZIP)

    if os.path.exists(RR_WAR):
        print("Successfully provisioned rr.war.")
    else:
        print("Failed to provision rr.war.")
        exit(1)

if __name__ == "__main__":
    provision_rr()
