import unittest
from appium import webdriver
from notepad import notepad_PO
from selenium.webdriver.common.keys import Keys

class notepad_test(unittest.TestCase):
    notepadSession = None

    def setUp(self):
        print("setup")
        desired_cap = {}
        desired_cap["app"] = "notepad.exe"
        self.notepadSession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_cap
        )

    def tearDown(self):
        self.notepadSession.quit()

    
    def test_notepad(self):
        text = "awesome!!!"
        np = notepad_PO.notepad_PO(self.notepadSession)
        np.textArea().send_keys(text)

        np.textArea().send_keys(Keys.ALT,Keys.F4)
        np.dialogCancel().click()
        np.textArea().send_keys(Keys.ALT,Keys.F4)
        np.dialogDontSave().click()


