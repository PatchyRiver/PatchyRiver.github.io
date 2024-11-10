import requests
import os
import time

print(2)

def download_images():
    base_url = 'https://api.hn/api.php?zd=pc&fl=fengjing'
    output_directory = 'head'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    for i in range(85,100):
        response = requests.get(base_url)
        if response.status_code == 200:
            with open(os.path.join(output_directory, f'image_{i}.jpg'), 'wb') as f:
                f.write(response.content)
            print(f"Downloaded image {i + 1}")
        else:
            print(f"Failed to download image {i + 1}")
        time.sleep(5)
        

download_images()