import json

class HandleFileData:
  def extract_file_data(file):
    with open(file) as f:
      data = json.load(f)
      return data