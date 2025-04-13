

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# URL of the site from which the data will be pulled
url = 'https://web-scraping-project.pages.dev/'
# Local site URL
# url = 'http://127.0.0.1:5500/Python/index.html'

# Data pull function


def scrape_data():
    response = requests.get(url)

    # Verify the success of the request
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract address
        title = soup.find('h2').text if soup.find('h2') else 'No title found'

        # Text extraction
        text = soup.find('p').text if soup.find('p') else 'No text found'

        # Extract description from meta
        description = soup.find('meta', {'name': 'description'})
        description = description['content'] if description else 'No description found'

        # Extract some data from div
        data_paragraphs = soup.find_all('p', class_='info')
        data = [p.text for p in data_paragraphs]

        return {
            'title': title,
            'text': text,
            'description': description,
            'data': data
        }
    else:
        return {'error': 'Failed to retrieve data'}


@app.route('/', methods=['GET'])
def get_scraped_data():
    # Call the scrape_data function
    data = scrape_data()
    return jsonify(data)


if __name__ == '__main__':
    # Run the application on localhost
    app.run(debug=True)
