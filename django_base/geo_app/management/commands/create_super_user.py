#import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'waterwatch.settings')
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
	def handle(self, *args, **options):
		try:
			User.objects.get(username="sjm", is_superuser=True).delete()
		except:
			pass
		User.objects.create_superuser('sjm', 'email', '123')