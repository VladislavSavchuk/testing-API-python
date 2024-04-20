Building an API Test Automation project using basic GET, POST, PUT, DELETE methods in Python
link https://restful-booker.herokuapp.com/apidoc/index.html

Running tests and preparing a report in allure
1. Open terminal in IDE
2. Enter the command
  pytest --alluredir=test_results/ tests/test_booking.py
3. Open terminal
4. Go to the project folder
  cd <project_name>
5. Enter the command
  allure serve test_results/
  