import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs


def download_image(url, output_dir):
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.basename(urlparse(url).path)
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")


def get_image_urls(base_url):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
        }
        response = requests.get(base_url, headers=headers)
        response.raise_for_status()  # Raise an error if the response status code is not 200

        print("Response status code:", response.status_code)  # Debugging statement

        soup = BeautifulSoup(response.content, 'html.parser')
        image_elements = soup.find_all('img')

        print("Number of image elements found:", len(image_elements))  # Debugging statement

        image_urls = []
        for img in image_elements:
            img_url = img.get('src')
            if img_url and "gettyimages" in img_url:
                image_urls.append(img_url)

        print("Number of image URLs found:", len(image_urls))  # Debugging statement

        return image_urls
    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return []
    except Exception as e:
        print(f"Error occurred: {e}")
        return []


def main():
    base_url = "https://www.gettyimages.in/photos/aamir-khan-actor"
    output_dir = "images"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_urls = get_image_urls(base_url)
    for url in image_urls:
        download_image(url, output_dir)


if __name__ == "__main__":
    main()
