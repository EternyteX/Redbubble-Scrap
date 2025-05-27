# 🖼️ Simple Redbubble Scraper

A lightweight Selenium-based tool to automatically scrape preview images from Redbubble search results.  
The tool opens the search page, grabs product thumbnails, converts them to large image URLs, and downloads each image to a local folder.

Created with ❤️ by **Ethernyte**

---

## ✨ Features

- Search Redbubble by any keyword
- Automatically scrapes the first page of results
- Downloads high-resolution preview images
- Images are renamed sequentially (e.g. `1.jpg`, `2.jpg`, ...)
- Clean CLI interface with ASCII title (via `pyfiglet`)

---

## 🧱 Requirements

- Python 3.8 or higher
- Google Chrome browser
- Matching [ChromeDriver](https://chromedriver.chromium.org/downloads)

---

## 📦 Installation

1. **Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/simple-redbubble-scraper.git
cd simple-redbubble-scraper
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

1. **Download ChromeDriver**  
   Get it from the official site:  
   [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

   Make sure the version matches your installed Google Chrome browser.  
   Example path:  
   ```
   C:\Users\YourName\Downloads\chromedriver-win64\chromedriver.exe
   ```

2. **Run the scraper**

```bash
python simple-scraper.py
```

3. **Follow the prompts** in the terminal:

- Enter the full path to your `chromedriver.exe`
- Enter a Redbubble search term (e.g. `cyber hacker sticker`)

---

## 📁 Output

Downloaded images will be stored like this:

```
simple-redbubble-scraper/
├── images/
│   ├── 1.jpg
│   ├── 2.jpg
│   └── ...
```

---

## 🧠 Notes

- This tool uses a real Chrome browser window (Selenium).
- Ensure your ChromeDriver version matches your installed Chrome.
- Avoid resizing or closing the browser while it runs.

---

## 📋 Example

```text
    ____              __    __              __      __      __
   / __ \  ___   ____/ /   / /_   __  __   / /_    / /_    / /  ___
  / /_/ / / _ \ / __  /   / __ \ / / / /  / __ \  / __ \  / /  / _ \
 / _, _/ /  __// /_/ /   / /_/ // /_/ /  / /_/ / / /_/ / / /  /  __/
/_/ |_|  \___/ \__,_/   /_.___/ \__,_/  /_.___/ /_.___/ /_/   \___/

by Ethernyte
```

---

## 📦 requirements.txt

```
requests
selenium
pyfiglet
```

---

## ☕ Credits

Built by [**Ethernyte**](https://github.com/Ethernyte)

---

## 🛠️ License

MIT License – free to use, modify, and share!
