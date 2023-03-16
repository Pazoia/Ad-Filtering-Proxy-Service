from unittest.mock import patch

from customersdata.data_handlers.file_data import HandleFileData

@patch("customersdata.data_handlers.file_data.json.load")
@patch("customersdata.data_handlers.file_data.open")
def test_extract_file_data_returns_data(mock_open, mock_json_load):
  mock_json_load.return_value = dict({"data": "Some data"})
  
  assert HandleFileData.extract_file_data("fake_file") == {"data": "Some data"}
  mock_open.assert_called_once_with("fake_file")
