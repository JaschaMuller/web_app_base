from django.contrib import admin

from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd

from geo_app.models import WaterConsumption

# Register your models here.

class WaterConsumptionAdmin(LeafletGeoAdmin):
	pass

admin.site.register(WaterConsumption, WaterConsumptionAdmin)

my_df = pd.read_pickle(r'/home/web_app_base/django_base/test_data/testData.pkl')

for index, row in my_df.iterrows():

	WaterConsumption(Id=index,
					 Suburb=row[1],
					 NoOfSingleResProp=row[2],
					 AvgMonthlyKL=row[3],
					 AvgMonthlyKLPredicted=0,
					 PredictionAccuracy=0,
					 Month=row[4],
					 Year=row[5],
					 DateTime=datetime.now(),
					 geom=Point(float(row[7].replace(',','.')),
					 			float(row[6].replace(',','.')))).save()
