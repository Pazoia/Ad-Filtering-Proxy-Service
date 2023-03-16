from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

class Command(BaseCommand):
  help = "It creates a random secret to be used in the .env file."
  
  def handle(self, *args, **options):

    SECRET_KEY = get_random_secret_key()
    
    print("Paste the key in your .env file, in the SECRET_KEY environment variable.")
    print(SECRET_KEY)