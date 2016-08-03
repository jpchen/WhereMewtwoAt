#!/usr/bin/env python
"""
Demo of searching by Pokemon
"""

import os
import sys
import json
import time
import pprint
import logging
import getpass
import argparse
from s2sphere import *
from datetime import datetime
from geopy.geocoders import GoogleV3
from .models import Pokemon

# add directory of this file to PATH, so that the package will be found
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

# import Pokemon Go API lib
from pgoapi import pgoapi
from pgoapi import utilities as util


log = logging.getLogger(__name__)

def init_config():
    parser = argparse.ArgumentParser()
    config_file = "config.json"

    # If config file exists, load variables from json
    load   = {}
    if os.path.isfile(config_file):
        with open(config_file) as data:
            load.update(json.load(data))

    # Read passed in Arguments
    required = lambda x: not x in load
    parser.add_argument("-a", "--auth_service", help="Auth Service ('ptc' or 'google')",
        required=required("auth_service"))
    parser.add_argument("-u", "--username", help="Username", required=required("username"))
    parser.add_argument("-p", "--password", help="Password")
    parser.add_argument("-l", "--location", help="Location", required=required("location"))
    parser.add_argument("-d", "--debug", help="Debug Mode", action='store_true')
    parser.add_argument("-t", "--test", help="Only parse the specified location", action='store_true')
    parser.add_argument("-n", "--name", help="Pokemon name", required=required("name"))
    parser.set_defaults(DEBUG=False, TEST=False)
    config = parser.parse_args()

    # Passed in arguments shoud trump
    for key in config.__dict__:
        if key in load and config.__dict__[key] == None:
            config.__dict__[key] = str(load[key])

    if config.__dict__["password"] is None:
        log.info("Secure Password Input (if there is no password prompt, use --password <pw>):")
        config.__dict__["password"] = getpass.getpass()

    if config.auth_service not in ['ptc', 'google']:
      log.error("Invalid Auth service specified! ('ptc' or 'google')")
      return None

    return config

def main():
    # log settings
    # log format
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(module)10s] [%(levelname)5s] %(message)s')
    # log level for http request class
    logging.getLogger("requests").setLevel(logging.WARNING)
    # log level for main pgoapi class
    logging.getLogger("pgoapi").setLevel(logging.INFO)
    # log level for internal pgoapi class
    logging.getLogger("rpc_api").setLevel(logging.INFO)

    config = init_config()
    if not config:
        return

    if config.debug:
        logging.getLogger("requests").setLevel(logging.DEBUG)
        logging.getLogger("pgoapi").setLevel(logging.DEBUG)
        logging.getLogger("rpc_api").setLevel(logging.DEBUG)

    # instantiate pgoapi
    api = pgoapi.PGoApi()

    # parse position
    position = util.get_pos_by_name(config.location)
    if not position:
        log.error('Your given location could not be found by name')
        return
    elif config.test:
        return

    # Load pokemon
    pokemon_list = []
    pokemon_dict = json.load(open('examples/pogo-optimizer/data/pokemon.json'))

    # set player position on the earth
    api.set_position(*position)

    if not api.login(config.auth_service, config.username, config.password, app_simulation = True):
        return

    lat,lng,x = api.get_position()
    origin = LatLng.from_degrees(lat,lng)
    parent = CellId.from_lat_lng(LatLng.from_degrees(lat, lng)).parent(15)

    # get player profile call (single command example)
    # ----------------------
    response_dict = api.get_player()
    print('Response dictionary (get_player): \n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(response_dict)))

    # sleep due to server-side throttling
    time.sleep(0.2)

    # get player profile + inventory call (thread-safe/chaining example)
    # ----------------------
#    req = api.create_request()
#    req.get_player()
#    req.get_inventory()
#    response_dict = req.call()
#    print('Response dictionary (get_player + get_inventory): \n\r{}'.format(pprint.PrettyPrinter(indent=4).pformat(response_dict)))

if __name__ == '__main__':
    main()
