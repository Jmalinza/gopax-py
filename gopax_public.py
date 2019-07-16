# -*- coding: utf-8 -*-

#COMMMENTS ARE COOL

import requests
import json
import logging
import time 

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


class gopax:
    def __init__(self, timeout=20):
        self.host = "https://api.gopax.co.kr/"
        self.timeout = timeout

    def assets(self):
        return self.request_get("assets")

    def trading_pairs(self):
        return self.request_get("trading-pairs")

    def ticker(self, trading_pair="BTC-KRW"):
        return self.request_get("trading-pairs/" +trading_pair+ "/ticker")

    def book(self, trading_pair="BTC-KRW", level="1"):
        params = {
            'level': level
        }
        return self.request_get("trading-pairs/" +trading_pair+ "/book", params=params)

    def recent_trades(self, trading_pair="BTC-KRW", limit="50"):
        params = {
            'limit': limit
        }
        return self.request_get("trading-pairs/" +trading_pair+ "/trades", params=params)

    def stats(self, trading_pair="BTC-KRW"):
        return self.request_get("trading-pairs/" +trading_pair+ "/stats")

    def all_stats(self):
        return self.request_get("trading-pairs/stats")

    #not working, returns empty json
    def history(self, trading_pair="BTC-KRW", start=round((time.time() )), end=round(((time.time()-86400))),interval="5"):
        params ={
            'start': str(start),
            'end': str(end),
            'interval': interval
        }
        return self.request_get("trading-pairs/" +trading_pair+ "/candles", params=params)


    def request_get(self, path, headers=None, params=None):
        response = requests.get(urljoin(self.host, path), headers=headers, params=params, timeout=self.timeout)
        try:
            return response.json()
        except json.decoder.JSONDecodeError as e:
            logging.error("exception: {}, response_text: {}".format(e, response.text))
            return response.text
