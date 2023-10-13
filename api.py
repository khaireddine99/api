from flask import Flask, jsonify
from scraper import scrape

app = Flask(__name__)

# Create a route to scrape the data and return it in JSON format
@app.route('/scrape', methods=['GET'])
def scrape_data():
    try:
        scraped_data = scrape()  # Call the scrape function to get the data

        return jsonify(scraped_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)