# Website Downloader 🌐📥

A Python script to download an entire website, including HTML, CSS, JavaScript, and images. This tool is useful for archiving web pages or for offline browsing.

## Features ✨

- Download HTML, CSS, JavaScript, and image files from a specified website.
- Save the website structure locally, preserving relative links to assets.
- Display a simple animated message during the download process.

## Requirements 📋

- Python 3.x
- `requests` library
- `beautifulsoup4` library

Install the required libraries using pip:

```bash
pip install requests beautifulsoup4
```

## How to Use 🚀

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/website-downloader.git
    cd website-downloader
    ```

2. **Run the script**:

    ```bash
    python website_downloader.py
    ```

3. **Enter the URL of the website** when prompted. The script will download the website and save it to a folder named after the website's hostname.

## Example 🖥️

```bash
Enter the URL of the website to download: https://example.com
```

The website will be downloaded into a folder named `example.com_download`.

## How It Works 🔍

- The script first creates a local directory to store the downloaded files.
- It downloads the main HTML file and saves it as `index.html`.
- It parses the HTML to find links to CSS, JavaScript, and image files.
- Each asset is downloaded and saved in the same directory.
- The script updates the HTML file to use local paths for the downloaded assets.
- An animated "Downloading..." message is displayed during the process.

## Notes 📝

- This script is intended for educational purposes and personal use.
- Be mindful of the website’s `robots.txt` file and usage policies before downloading content.

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing 🤝

Feel free to submit issues or pull requests if you have suggestions or improvements. 

## Contact 📧

If you have any questions, please reach out to [your-email@example.com](mailto:your-email@example.com).

---

Happy coding! 🚀
