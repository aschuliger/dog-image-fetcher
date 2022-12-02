class url_has_redirected(object):
  """An expectation for checking that the url has redirected back to the specified url

  locator - used to find the element
  returns the WebElement once it has the particular css class
  """
  def __init__(self, query):
    self.query = query

  def __call__(self, driver):
    current_url = driver.current_url  # Finding the referenced element
    print(current_url)
    print(self.query in current_url)
    if self.query in current_url:
        return True
    else:
        return False