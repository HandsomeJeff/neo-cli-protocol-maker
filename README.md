# neo-cli-protocol-maker

One click (if you do it right) to update `protocol.json`

## Requirements:
### Python packages
2. BeautifulSoup4 (bs4)
3. selenium
4. requests

### Additional things
1. Firefox or Chrome browser
2. [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) if using Chrome
3. [geckodriver](https://github.com/mozilla/geckodriver/releases) if using Firefox. If there is any issue, I recommend reading [this](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path)

## Getting Started
### 1. Download the package

### 2. Run the Package
Run the script `python make_protocol.py`

You should see a new `protocol.json` file in the same directory as the script. Now, copy and replace the `protocol.json` in your neo-cli directory with this file.

### 3. That's it!
You can run neo-cli normally. It should automatically connect to live nodes.
