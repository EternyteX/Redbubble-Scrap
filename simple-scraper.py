import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from urllib.parse import quote_plus
from art import tprint


class SimpleRedbubbleScraper:
    def __init__(self, driver_path):
        options = Options()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        service = ChromiumService(driver_path)
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.implicitly_wait(10)

    def open_search_results(self, search_term: str):
        encoded_term = quote_plus(search_term)
        url = f"https://www.redbubble.com/shop?query={encoded_term}&ref=search_box"
        self.driver.get(url)
        self.driver.maximize_window()

    def scrape_first_page_image_urls(self):
        time.sleep(3)
        image_urls = []
        imgs = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/shop/'] img")
        for img in imgs:
            src = img.get_attribute("src")
            if src and src.endswith(".jpg"):
                image_urls.append(src)
        if not image_urls:
            imgs = self.driver.find_elements(By.TAG_NAME, "img")
            for img in imgs:
                src = img.get_attribute("src")
                if src and src.endswith(".jpg"):
                    image_urls.append(src)
        return image_urls

    def get_large_image_url(self, url):
        if "st,small" in url:
            return url.replace("st,small", "st,large")
        elif "st," in url:
            parts = url.split("/")
            last_part = parts[-1]
            if last_part.startswith("st,"):
                segments = last_part.split(",")
                if len(segments) > 1:
                    segments[1] = "large"
                    parts[-1] = ",".join(segments)
                    return "/".join(parts)
        return url

    def download_image(self, url, folder="images"):
        os.makedirs(folder, exist_ok=True)
        filename = url.split("/")[-1].split("?")[0]
        path = os.path.join(folder, filename)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/114.0.0.0 Safari/537.36",
            "Referer": "https://www.redbubble.com/"
        }
        try:
            r = requests.get(url, headers=headers, stream=True, timeout=10)
            if r.status_code == 200:
                with open(path, "wb") as f:
                    for chunk in r.iter_content(1024):
                        f.write(chunk)
                print(f"Saved: {path}")
                return filename
            else:
                print(f"Failed to download: {url} - Status {r.status_code}")
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        return None

    def close(self):
        self.driver.quit()


def main():
    tprint("Redbubble", font="slant")
    print("by EternyteX\n")

    driver_path = input("Enter full path to chromedriver: ").strip()
    if not os.path.isfile(driver_path):
        print("Invalid driver path.")
        return

    search_term = input("Enter search term: ").strip()
    folder = "images"
    os.makedirs(folder, exist_ok=True)

    scraper = SimpleRedbubbleScraper(driver_path)
    print(f"\nSearching for: {search_term}\n")
    scraper.open_search_results(search_term)

    urls = scraper.scrape_first_page_image_urls()
    print(f"Found {len(urls)} images.\n")

    counter = 1
    for thumb_url in urls[:500]:
        large_url = scraper.get_large_image_url(thumb_url)
        print(f"Downloading: {large_url}")
        original_filename = scraper.download_image(large_url, folder=folder)
        if original_filename:
            original_path = os.path.join(folder, original_filename)
            new_path = os.path.join(folder, f"{counter}.jpg")
            if os.path.exists(original_path):
                os.rename(original_path, new_path)
                print(f"Renamed to: {new_path}\n")
                counter += 1

    input("Press Enter to close the browser...")
    scraper.close()


if __name__ == "__main__":
    main()
