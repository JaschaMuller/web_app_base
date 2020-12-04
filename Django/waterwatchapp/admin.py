from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd

from waterwatchapp.models import WaterConsumption

# Register your models here.

class WaterConsumptionAdmin(LeafletGeoAdmin):
	pass

admin.site.register(WaterConsumption, WaterConsumptionAdmin)

df_excelReader = my_df = pd.read_csv('/home/Django/WaterWatchInput.csv', sep=';')

for index, row in df_excelReader.iterrows():

	WaterConsumption(Id=index,
					 Suburb=row[1],
					 NoOfSingleResProp=row[2],
					 AvgMonthlyKL=row[3],
					 AvgMonthlyKLPredicted=0,
					 PredictionAccuracy=0,
					 Month=row[4],
					 Year=row[5],
					 # DateTime=datetime.now(),
					 geom=Point(float(row[7].replace(',','.')),
					 			float(row[6].replace(',','.')))).save()


