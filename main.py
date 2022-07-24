from ast import main
from flask import Flask
from flask_restful import Resource, Api
import pandas as pd


class BetriebsstellenInfo(Resource):
    def get(self, abk):
        betriebsstellen = pd.read_csv('./betriebsstellen_10.2021.csv', sep=';', index_col=False)

        try:
            data = betriebsstellen[betriebsstellen['RL100-Code'] == abk.upper()]
            data = data[['RL100-Langname', 'RL100-Kurzname', 'Typ Kurz']]
            data = data.to_dict()

            return data
        except:
            return {'data' : ''}


def main():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(BetriebsstellenInfo, '/betriebsstelle/<string:abk>')
    app.run(debug=True)


if __name__ == '__main__':
    main()