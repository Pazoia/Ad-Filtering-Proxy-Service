from helper_functions import HelperFunctions

def test_python_version_checker_with_version_too_low():
  """
  Given a python version that is too low
  When we run it through the python_version_checker
  Then we get the value of False
  """

  python_version = [3, 2]

  [a, b] = python_version

  accepted_python_version = HelperFunctions.python_version_checker(a, b)

  assert accepted_python_version == False

def test_python_version_checker_with_accepted_version():
  """
  Given a python version that is an accepted version
  When we run it through the python_version_checker
  Then we get the value of True
  """

  python_version = [3, 11]

  [a, b] = python_version

  accepted_python_version = HelperFunctions.python_version_checker(a, b)

  assert accepted_python_version == True