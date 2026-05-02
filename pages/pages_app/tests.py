from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self): # Test that the home page returns a 200 status code -> 200 means the page is found and working correctly
        response = self.client.get("/") # Send a GET request to the home page URL
        self.assertEqual(response.status_code, 200) # Assert that the response status code is 200 (OK)

    def test_about_page_status_code(self):
        response = self.client.get("/about/") # Send a GET request to the about page URL
        self.assertEqual(response.status_code, 200) # Assert that the response status code is 200 (OK)