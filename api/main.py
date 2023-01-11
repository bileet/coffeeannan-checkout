from flask import Flask, Response
import requests

app = Flask(__name__)


@app.route('/prices/<plan_id>')
def index(plan_id):
    res = requests.get(
        'https://coffeeannan.chargebee.com/api/v2/item_prices?item_id[is]=' + plan_id, auth = (
            'live_zzPe8i7mUOYtEPNvJWVLdFDuRKp0S8M6:', ''
        )
    )
    resp = Response(res.text, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


app.run(host='0.0.0.0', port=81)
