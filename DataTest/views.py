from django.shortcuts import render
from django.http import HttpResponse
import csv
import os
import os
import numpy as np
import pandas as pd
from Main.models import Blok

DIRNAME = os.path.dirname(__file__)

def DataTest_Main(self):
    html = "<h1>Data Test pagina</h1>" \
            "<html><body>Test page <br> </body></html>" \
            '<a href="./1"> Run test 1 <br></a>' \
           '<a href="./2"> Run test 2 <br></a>'

    return HttpResponse(html)

def DataTest_Jaar_Toets_Resultaat_Pogingen(self):
    Rows = []
    with open(os.path.join(DIRNAME, 'TestData', 'grades_year1.csv'), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            Rows.append(row)

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


def blok_gen():
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
    blok.to_csv(os.path.join(path, r'blok.csv'), index=False)


def list_loop(val1, year, toets, resultaat, poging):
    year_list = []
    toets_list = []
    voldoende_list = []
    poging_list = []

    data_columns = ["Jaar", "Toets", "Resultaat", "Pogingen"]

    for x in range(val1):
        year_list.append(year)
        toets_list.append(toets)
        voldoende_list.append(resultaat)
        poging_list.append(poging)
    MYarray = np.array([year_list, toets_list, voldoende_list, poging_list]).transpose()
    grades_of_the_year_df = pd.DataFrame(MYarray, columns=data_columns)
    return grades_of_the_year_df


def export_to_csv(val1, val2, val3, val4, val5, val6, val7, val8, val9=0, val10=0, val11=0, val12=0, year=0, filename='grades.csv'):
    # Het maken van de dataframe: "grades_of_the_year_df"

    data_columns = ["Jaar", "Toets", "Resultaat", "Pogingen"]
    grades_of_the_year_df = pd.DataFrame(columns=data_columns)

    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val1, year, 1, 'voldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val2, year, 1, 'onvoldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val3, year, 2, 'voldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val4, year, 2, 'onvoldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val5, year, 3, 'voldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val6, year, 3, 'onvoldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val7, year, 4, 'voldoende', 1))
    grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val8, year, 4, 'onvoldoende', 1))
    if year == 1:
        grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val9, year, 4, 'voldoende', 1))
        grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val10, year, 4, 'onvoldoende', 1))
        grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val11, year, 4, 'voldoende', 1))
        grades_of_the_year_df = grades_of_the_year_df.append(list_loop(val12, year, 4, 'onvoldoende', 1))

    grades_of_the_year_df.to_csv(filename, index=False)



