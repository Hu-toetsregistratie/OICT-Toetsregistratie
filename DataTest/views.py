
import random

from django.http import HttpResponse, HttpResponseRedirect
import csv
import os
import numpy as np
import pandas as pd
from rest_framework import request

from Main.models import Blok, Toets
from django.contrib import messages

DIRNAME = os.path.dirname(__file__)

def DataTest_Main(self):
    html = "<h1>Data Test pagina</h1>" \
            "<html><body>Test page <br> </body></html>" \
            '<a href="./1"> Run test 1 <br></a>' \
            '<a href="./2"> Run test 2 <br></a>' \
            '<a href="./G1"> Generate data <br></a>' \
            '<a href="./G2"> Generate data 2 <br></a>'

    return HttpResponse(html)

def DataTest_Jaar_Toets_Resultaat_Pogingen(self):
    Rows = []
    for x in range(4):
        with open(os.path.join(DIRNAME, 'TestData', 'Toets_jaar{}.csv'.format(x+1)), 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # skip the headers
            for row in reader:
                _, created = Toets.objects.get_or_create(
                    toets_code=row[0],
                    toets_naam=row[1],
                    jaar=row[2],
                    blok=Blok(row[3]),
                )
    return HttpResponse(Rows)

def DataTest_blok(self):
    Rows = []
    with open(os.path.join(DIRNAME, 'TestData', 'blok.csv'), 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers
        for row in reader:
            _, created = Blok.objects.get_or_create(
                blok=row[1],
                jaar=row[0],
            )
    return HttpResponse(Rows)


##############################################
#Data generation#
##############################################


def blok_gen(self):
    path = 'TestData'
    blokken = []
    jaar = []
    for y in range(4):
        for x in range(4):
            jaar.append(y+1)
            blokken.append("Blok {}".format(x+1))

    MYarray = np.array([jaar, blokken]).transpose()
    blok_columns = ["Jaar", "Blok"]
    blok = pd.DataFrame(MYarray, columns=blok_columns)
    blok.to_csv(os.path.join(DIRNAME, 'TestData', 'blok.csv'),index=False)
    return HttpResponseRedirect("/test/")


def list_loop(val1, jaar=1,blok=1):
    toets_code_list = []
    toets_naam_list = []
    jaar_list = []
    blok_list = []

    data_columns = ["toets_code", "toets_naam", "jaar", "blok"]

    for x in range(val1):
        toets_code_list.append(random.randrange(1000000,9999999))
        toets_naam_list.append("Toets {}".format(x+1))
        jaar_list.append(jaar)
        blok_list.append(blok)
    MYarray = np.array([toets_code_list, toets_naam_list, jaar_list, blok_list]).transpose()
    grades_of_the_year_df = pd.DataFrame(MYarray, columns=data_columns)
    return grades_of_the_year_df


def run_toets_gen(self):
    export_to_csv(jaar=1, filename=1)
    export_to_csv(jaar=2, filename=2)
    export_to_csv(jaar=3, filename=3)
    export_to_csv(jaar=4, filename=4)
    return HttpResponse()

def export_to_csv(val1=4, val2=4, val3=4, val4=4, val5=4, val6=4, jaar=4, filename=''):
    # Het maken van de dataframe: "grades_of_the_year_df"

    data_columns = ["toets_code", "toets_naam", "jaar", "blok"]
    Toets_df = pd.DataFrame(columns=data_columns)

    Toets_df = Toets_df.append(list_loop(val1, jaar, (((jaar - 1) * 4)+1)))
    Toets_df = Toets_df.append(list_loop(val2, jaar, (((jaar - 1) * 4)+2)))
    if jaar == 1:
        Toets_df = Toets_df.append(list_loop(val3, jaar, (((jaar - 1) * 4)+2)))
    Toets_df = Toets_df.append(list_loop(val4, jaar, (((jaar - 1) * 4)+3)))
    Toets_df = Toets_df.append(list_loop(val5, jaar, (((jaar - 1) * 4)+4)))
    if jaar == 1:
        Toets_df = Toets_df.append(list_loop(val6, jaar, (((jaar - 1) * 4)+4)))

    Toets_df.to_csv(os.path.join(DIRNAME, 'TestData', 'Toets_jaar{}.csv'.format(filename)), index=False)





from django.shortcuts import render

# Create your views here.

