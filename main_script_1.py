# Yt 2
# Block certain urls or websites

import os
from time import *
from datetime import *

# Path to host file on system
host_path = os.path.join('C:\\', 'Windows', 'System32', 'drivers', 'etc')

# Keep adding this line to the host file
localhost = "127.0.0.1"

# List of urls to block
urls = input("Enter a list of Urls seperated by a comma: ")
# Returns a list of urls seperated by a comma
urls = urls.split()
# urls = ['www.facebook.com', 'betnaija.com']

# Continue adding this line to the host file

while True:
    # Returns a boolean
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 8, 30) < datetime.now() < datetime(datetime.now().year, datetime.now().month, datetime.now().day, 18, 30):
        # Accessing the file
        with open(host_path, ) as file:
            # Reading the file
            content = file.read()

            for url in urls:
                if url in content:
                    pass
                else:
                    file.write(localhost + " " + url + "\n")

    else:
        with open(host_path, "r+") as file:
            content = file.readlines()
            file.seek(0)

            for line in content:
                if not any(url in line for url in urls):
                    file.write(line)

                file.truncate()
            sleep(5)


