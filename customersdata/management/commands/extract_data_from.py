from django.core.management.base import BaseCommand

from customersdata.data_handlers.file_data import HandleFileData
from customersdata.data_handlers.database_data import HandleDatabaseData

class Command(BaseCommand):
  help = "Extracts data from files, passing it to be managed by data handlers"

  def add_arguments(self, parser) -> None:
    parser.add_argument("filename", nargs="+", type=str)

  def handle(self, *args, **options):
    
    file = options["filename"][0]

    data_extracted_from_file = HandleFileData.extract_file_data(file)
    HandleDatabaseData.save_data_to_db(data_extracted_from_file)

    print(f"The data from file {file} has been extracted successfully.")
