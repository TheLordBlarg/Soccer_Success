# -*- coding: utf-8 -*-
import database_functions_helper as dfh
import database_functions_user as dfu
import unidecode
import lxml.html
import requests
import numpy
import time
import os



#"""
databases = ["sofifa_database.txt"]; i = 1
os.chdir(os.path.abspath(os.path.dirname(__file__)))
while i > 0:
    try:
        dfu.results_processor("match_list_eng-premier-league_2014-2015.txt",
                              "sofifa_database_15.txt",
                              average = 'position',
                              status = 10,
                              ignoreplayers = 7,
                              keystats = True,
                              databases = databases)
    except requests.exceptions.ConnectionError:
        print "Error!"
        time.sleep(10)
#"""