class browsers_are_closed(object):
  """An expectation for checking that the url has redirected back to the specified url

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __call__(self, driver):
    number_of_browsers = len(driver.window_handles)  # Finding the referenced element
    print(number_of_browsers)
    if number_of_browsers == 1:
        return True
    else:
        return False