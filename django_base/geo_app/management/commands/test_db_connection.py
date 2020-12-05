from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError

class Command(BaseCommand):
	def handle(self, *args, **options):
		db_conn = connections['default']
		try:
		    c = db_conn.cursor()
		except OperationalError:
		    connected = False
		    print('-->DB connection Failed<--')
		else:
		    connected = True
		    print('-->DB connection Suceeded<--')
