#Fonctions pour effectuer des requettes dans la base

import mysql.connector
from mysql.connector import Error

import pandas as pd
import geopandas
import matplotlib.pyplot as plt


def getStudent(conn):
	try:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM STUDENT")

		row = cursor.fetchall()

		for r0w0 in row :
			print(r0w0)

	except Error as e:
		print(e)

	finally:
		cursor.close()
		return row

def getInternships(conn):
	try:
		cursor = conn.cursor()
		cursor.execute("SELECT * FROM INTERNSHIP")

		row = cursor.fetchall()

		for r0w0 in row :
			print(r0w0)


	except Error as e:
		print(e)

	finally:
		cursor.close()
		return row


def addStudent(conn, Fname, Lname, GradY):
	try:
		cursor = conn.cursor()
		cursor.execute("INSERT INTO STUDENT(lname, fname, gradyear_id) VALUES ( '"+ Fname +"', '"+ Lname +"', '"+ GradY+"' )")
	except Error as e:
		print(e)
		return -1

	finally:
		cursor.close()
		return 0 

def addInternship(conn, Fname, Lname, GradY, cityN, date_start, date_end):
	try:
		cursor = conn.cursor()
		cursor.execute("SELECT student_id FROM STUDENT WHERE Fname = '"+Fname+"' AND Lname = '"+Lname+"' AND gradyear_id = "+GradY )
		id_S = cursor.fetchone()
		if (id_S == None):
			print("ETUDIANT INCONNU")
			return 1
		cursor.execute("SELECT city_id FROM CITY WHERE city_name = '"+cityN+"'" )
		id_C = cursor.fetchone()
		if (id_C == None):
			print("VILLE INCONNUE")
			return 2
		print("INSERT INTO INTERNSHIP(student_id, city_id, date_start, date_end) VALUES, (decap_id(id_S) ,decap_id(id_C),date_start, date_end)")
		cursor.execute("INSERT INTO INTERNSHIP(student_id, city_id, date_start, date_end) VALUES" , (decap_id(id_S) ,decap_id(id_C) ,date_start, date_end))
	except Error as e:
		print(e)
		return -1

	finally:
		cursor.close()
		return 0

def decap_id(id_cap):
	return id_cap[1:len(id_cap)-1]


## Test stages plot sur la worldmap
def drawCitiesOnMap(conn):
        try:
                cursor = conn.cursor()
                cursor.execute( "SELECT longitude, latitude FROM CITY" )
                cities = cursor.fetchall()
                if (cities == None):
                        print("AUCUNE VILLE")
                        return 1
        except Error as e:
                print(e)
                return -1

        finally:
                cursor.close()

        longitude, latitude = [], []
        for i in range(len(cities)):
                longitude.append( float(cities[i][0]) )
                latitude.append( float(cities[i][1]) )
        
        coord = pd.DataFrame({'Longitude' : longitude, 'Latitude' : latitude})
        gdf = geopandas.GeoDataFrame(coord, geometry = geopandas.points_from_xy(coord.Longitude, coord.Latitude))

        world = geopandas.read_file(geopandas.datasets.get_path('naturalearth_lowres'))
        ax = world.plot(color='white', edgecolor='black')

        gdf.plot(ax=ax, color='red')
        plt.show()

        return 0

