import random

import names
from django.http import HttpResponse, HttpResponseRedirect
import csv
import os
import numpy as np
import pandas as pd
from rest_framework import request
from PIL import Image


from Main.models import Blok, Toets, Student, Cijfer
from django.contrib import messages

DIRNAME = os.path.dirname(__file__)
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from django.template import RequestContext, Template, Context
from django.conf import settings


def DataTest_Main(self):
    html =  "<h1>Data Test pagina</h1>" \
            "<html><body>Test page <br> </body></html>" \
            '<a href="./1"> Run Toets (blok moet gedaan zijn) <br></a>' \
            '<a href="./2"> Run Blok <br></a>' \
            '<a href="./3"> Run student <br></a>' \
            '<a href="./4"> Run cijfers <br></a>' \
            '<a href="./G1"> Generate Blok <br></a>' \
            '<a href="./G2"> Generate Toets <br></a>' \
            '<a href="./G3"> Generate Student <br></a>' \
            '<a href="./G4"> Generate cijfers <br></a>' \
            '<a href="./G5"> Generate grafiek <br></a>'

    return HttpResponse(html)

def save_graph(filename, dataset, graph_title):
    grafiek = sns.countplot(data=dataset,
                            x="toets_code",
                            hue="voldoende",
                            hue_order=[0, 1],
                            palette="viridis").set_title(graph_title)

    # het positioneren van de legenda
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

    # locatie van de output
    filepath = 'TestData/'
    # instantieren van de figure
    fig = grafiek.get_figure()
    # het opslaan van de grafiek
    fig.savefig(os.path.join(DIRNAME, filepath, filename), bbox_inches='tight')
    # Zorgen dat de legenda en grafiek wordt gereset
    plt.clf()
    plt.close()

    image_data = open(os.path.join(DIRNAME, filepath, filename), "rb").read()
    return HttpResponse(image_data)


def graph_gen(self):
    df_grades_all = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'grades_all.csv'), index_col=False)

    df_grades_all.Jaar.astype('str')

    df_grades_y1 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'Cijfers1.csv'))
    df_grades_y2 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'Cijfers2.csv'))
    df_grades_y3 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'Cijfers3.csv'))
    df_grades_y4 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'Cijfers4.csv'))

    save_graph(filename='grafiek_jaar1.png', dataset=df_grades_y1, graph_title='Resultaten van Jaar 1')
    save_graph(filename='grafiek_jaar2.png', dataset=df_grades_y2, graph_title='Resultaten van Jaar 2')
    save_graph(filename='grafiek_jaar3.png', dataset=df_grades_y3, graph_title='Resultaten van Jaar 3')
    save_graph(filename='grafiek_jaar4.png', dataset=df_grades_y4, graph_title='Resultaten van Jaar 4')

    image_data1 = Image.open(os.path.join(DIRNAME, "TestData", "grafiek_jaar1.png"))
    image_data2 = Image.open(os.path.join(DIRNAME, "TestData", "grafiek_jaar2.png"))
    image_data3 = Image.open(os.path.join(DIRNAME, "TestData", "grafiek_jaar3.png"))
    image_data4 = Image.open(os.path.join(DIRNAME, "TestData", "grafiek_jaar4.png"))

    image_data1_size = image_data1.size

    main_image = Image.new('RGB', (2 * image_data1_size[0], 2 * image_data1_size[1]), (250, 250, 250))

    main_image.paste(image_data1, (0, 0))
    main_image.paste(image_data2, (image_data1_size[0], 0))
    main_image.paste(image_data3, (0, image_data1_size[1]))
    main_image.paste(image_data4, (image_data1_size[0], image_data1_size[1]))
    main_image.save(os.path.join(DIRNAME, "TestData", "full_graph.png"))

    image_data_main = open(os.path.join(DIRNAME, "TestData", "full_graph.png"), "rb").read()

    return HttpResponse(image_data_main, content_type="image/png")


def stat_gen(self):
    df_success_all = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'success_rates_y1.csv'), index_col=False)

    df_success_y1 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'success_rates_y1.csv'))
    df_success_y2 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'success_rates_y2.csv'))
    df_success_y3 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'success_rates_y2.csv'))
    df_success_y4 = pd.read_csv(os.path.join(DIRNAME, 'TestData', 'success_rates_y4.csv'))

    html_df = df_success_y1.to_html(index=False) + df_success_y2.to_html(index=False) + df_success_y3.to_html(index=False) + df_success_y4.to_html(index=False)

    return HttpResponse(html_df)


def DataTest_Jaar_Toets_Resultaat_Pogingen(self):
    Rows = []
    for x in range(4):
        with open(os.path.join(DIRNAME, 'TestData', 'Toets_jaar{}.csv'.format(x + 1)), 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # skip the headers
            for row in reader:
                _, created = Toets.objects.get_or_create(
                    toets_code=row[0],
                    toets_naam=row[1],
                    jaar=row[2],
                    blok=Blok(row[3]),
                    volgorde=row[4]
                )
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

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
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

def DataTest_student(self):
    Rows = []
    for x in range(4):
        with open(os.path.join(DIRNAME, 'TestData', 'Students{}.csv'.format(x + 1)), 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # skip the headers
            for row in reader:
                _, created = Student.objects.get_or_create(
                    voornaam=row[0],
                    achternaam=row[1],
                    student_nummer=row[2],
                )
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

def DataTest_cijfer(self):
    Rows = []
    for x in range(4):
        with open(os.path.join(DIRNAME, 'TestData', 'Cijfers{}.csv'.format(x + 1)), 'r') as file:
            reader = csv.reader(file)
            next(reader, None)  # skip the headers
            for row in reader:
                _, created = Cijfer.objects.get_or_create(
                    voldoende=row[0],
                    blok_id=row[1],
                    student_id=row[2],
                    toets_code_id=row[3],
                    toets_naam_id=row[3]
                )
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")




##############################################
# Data generation#
##############################################


def blok_gen(self):
    path = 'TestData'
    blokken = []
    jaar = []
    for y in range(4):
        for x in range(4):
            jaar.append(y + 1)
            blokken.append("Blok {}".format(x + 1))

    MYarray = np.array([jaar, blokken]).transpose()
    blok_columns = ["Jaar", "Blok"]
    blok = pd.DataFrame(MYarray, columns=blok_columns)
    blok.to_csv(os.path.join(DIRNAME, 'TestData', 'blok.csv'), index=False)
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")


##########################################################

def run_student_gen(self):
    StudentGen(filename=1)
    StudentGen(filename=2)
    StudentGen(filename=3)
    StudentGen(filename=4)
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

def StudentGen(val1=10, val2=10, val3=10, val4=10, filename=''):
    data_columns = ["voornaam", "achternaam", "student_nummer"]
    Student_df = pd.DataFrame(columns=data_columns)

    Student_df = Student_df.append(Student_loop(val1, "male"))
    Student_df = Student_df.append(Student_loop(val2, "female"))
    Student_df = Student_df.append(Student_loop(val3, "male"))
    Student_df = Student_df.append(Student_loop(val4, "female"))

    Student_df.to_csv(os.path.join(DIRNAME, 'TestData', 'Students{}.csv'.format(filename)), index=False)


def Student_loop(val1, gender):
    student_voornaam_list = []
    student_achternaam_list = []
    student_nummer_list = []

    data_columns = ["voornaam", "achternaam", "student_nummer"]

    for x in range(val1):
        student_nummer_list.append(random.randrange(1000000, 9999999))
        student_voornaam_list.append(names.get_first_name(gender='{}'.format(gender)))
        student_achternaam_list.append(names.get_last_name())

    MYStudentarray = np.array([student_voornaam_list, student_achternaam_list, student_nummer_list]).transpose()
    Student_df = pd.DataFrame(MYStudentarray, columns=data_columns)
    return Student_df


################################################################

def run_toets_gen(self):
    export_to_csv(jaar=1, filename=1)
    export_to_csv(jaar=2, filename=2)
    export_to_csv(jaar=3, filename=3)
    export_to_csv(jaar=4, filename=4)
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

def export_to_csv(val1=1, val2=1, val3=1, val4=1, val5=1, val6=1, jaar=4, filename=''):
    # Het maken van de dataframe: "grades_of_the_year_df"

    data_columns = ["toets_code", "toets_naam", "jaar", "blok"]
    Toets_df = pd.DataFrame(columns=data_columns)

    Toets_df = Toets_df.append(list_loop(val1, jaar, (((jaar - 1) * 4) + 1), 1))
    Toets_df = Toets_df.append(list_loop(val2, jaar, (((jaar - 1) * 4) + 2), 2))
    if jaar == 1:
        Toets_df = Toets_df.append(list_loop(val3, jaar, (((jaar - 1) * 4) + 2), 3))
        Toets_df = Toets_df.append(list_loop(val4, jaar, (((jaar - 1) * 4) + 3), 4))
        Toets_df = Toets_df.append(list_loop(val5, jaar, (((jaar - 1) * 4) + 4), 5))
        Toets_df = Toets_df.append(list_loop(val6, jaar, (((jaar - 1) * 4) + 4), 6))
    else:
        Toets_df = Toets_df.append(list_loop(val4, jaar, (((jaar - 1) * 4) + 3), 3))
        Toets_df = Toets_df.append(list_loop(val5, jaar, (((jaar - 1) * 4) + 4), 4))

    Toets_df.to_csv(os.path.join(DIRNAME, 'TestData', 'Toets_jaar{}.csv'.format(filename)), index=False)


def list_loop(val1, jaar=1, blok=1, nummer = 1):
    toets_code_list = []
    toets_naam_list = []
    jaar_list = []
    blok_list = []
    volgorde_list = []

    data_columns = ["toets_code", "toets_naam", "jaar", "blok", "volgorde"]

    for x in range(val1):
        toets_code_list.append(random.randrange(1000000, 9999999))
        if jaar == 1:
            toets_naam_list.append("Toets {}".format(((jaar - 1) * 4) + nummer))
            volgorde_list.append(((jaar - 1) * 4) + nummer)
        else:
            toets_naam_list.append("Toets {}".format(((jaar - 1) * 4) + nummer + 2))
            volgorde_list.append(((jaar - 1) * 4) + nummer + 2)

        jaar_list.append(jaar)
        blok_list.append(blok)

    MYarray = np.array([toets_code_list, toets_naam_list, jaar_list, blok_list, volgorde_list]).transpose()
    grades_of_the_year_df = pd.DataFrame(MYarray, columns=data_columns)
    return grades_of_the_year_df

#########################################################


def run_cijfer_gen(self):
    CijferGen(filename=1, year=1)
    CijferGen(filename=2, year=2)
    CijferGen(filename=3, year=3)
    CijferGen(filename=4, year=4)
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

def CijferGen(val1=160, val2=160, val3=160, val4=160, filename='', year = 1):
    data_columns = ["voldoende", "blok", "student", "toets_code", "toets_naam"]
    Cijfer_df = pd.DataFrame(columns=data_columns)


    if year ==1:
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val1, year, 1))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val2, year, 2))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val2, year, 2, 1))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val3, year, 3, 1))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val4, year, 4, 1))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val2, year, 4, 2))
    else:
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val1, year, 1, 2))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val2, year, 2, 2))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val3, year, 3, 2))
        Cijfer_df = Cijfer_df.append(Cijfer_loop(val4, year, 4, 2))


    Cijfer_df.to_csv(os.path.join(DIRNAME, 'TestData', 'Cijfers{}.csv'.format(filename)), index=False)


def Cijfer_loop(val1, jaar = 1, blok = 1, toetsOffset = 0):
    cijfer_voldoende_list = []
    cijfer_blok_list = []
    cijfer_student_list = []
    cijfer_toets_code_list = []
    cijfer_toets_naam_list = []

    data_columns = ["voldoende", "blok", "student", "toets_code", 'toets_naam']


    for x in range(val1):

        if random.randrange(0, 10) != 1:
            cijfer_voldoende_list.append(True)
        else:
            cijfer_voldoende_list.append(False)

        cijfer_toets_code_list.append(((jaar - 1) * 4) + blok + toetsOffset)
        cijfer_toets_naam_list.append(((jaar - 1) * 4) + blok + toetsOffset)
        cijfer_blok_list.append(blok)
        cijfer_student_list.append(x + 1)

    MYCijferarray = np.array([cijfer_voldoende_list, cijfer_blok_list, cijfer_student_list,cijfer_toets_code_list, cijfer_toets_naam_list ]).transpose()
    Cijfer_df = pd.DataFrame(MYCijferarray, columns=data_columns)
    return Cijfer_df



def Run_all_gen_test(self):
    blok_gen(self)
    run_toets_gen(self)
    run_cijfer_gen(self)
    run_student_gen(self)
    DataTest_student(self)
    DataTest_blok(self)
    DataTest_Jaar_Toets_Resultaat_Pogingen(self)
    DataTest_cijfer(self)
    return HttpResponseRedirect("http://62.251.126.253:63343/dev.html")

