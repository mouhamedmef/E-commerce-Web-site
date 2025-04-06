from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

DUMMYJSON_API_PRODUCTS_URL = "https://dummyjson.com/products"

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/Beauty')
def beauty():
    return render_template('beauty.html')


@app.route('/dummyjson/products', methods=['GET'])
def get_dummyjson_products():
    """
    Fetches a list of products from the DummyJSON API.
    """
    try:
        response = requests.get(DUMMYJSON_API_PRODUCTS_URL)
        response.raise_for_status()
        products_data = response.json()
        return jsonify(products_data['products'])  # The products are nested under 'products' key
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching products: {e}'}), 500

@app.route('/dummyjson/products/<int:product_id>', methods=['GET'])
def get_dummyjson_product(product_id):
    """
    Fetches details of a specific product by ID from the DummyJSON API.
    """
    try:
        response = requests.get(f"{DUMMYJSON_API_PRODUCTS_URL}/{product_id}")
        response.raise_for_status()
        product_data = response.json()
        return jsonify(product_data)
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error fetching product: {e}'}), 500
    except ValueError:
        return jsonify({'error': 'Invalid product ID'}), 400

if __name__ == '__main__':
    app.run(debug=True)