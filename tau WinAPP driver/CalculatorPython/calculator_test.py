import unittest
from appium import webdriver


class calculator_test(unittest.TestCase):
    calcResult = None
    calcSession = None

    def setUp(self):
        print("setup")
        desired_capabiliti = {}
        desired_capabiliti["app"] = "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.calcSession = webdriver.Remote(
            command_executor="http://127.0.0.1:4723",
            desired_capabilities=desired_capabiliti
        )

    def tearDown(self):
        print("teardown")
        self.calcSession.quit()

    def test_addition(self):
        print("addition")
        self.calcSession.find_element_by_name("Two").click()
        self.calcSession.find_element_by_name("Seven").click()
        self.calcSession.find_element_by_name("Plus").click()
        self.calcSession.find_element_by_name("Nine").click()
        self.calcSession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResult(), "36")

    def test_subtraction(self):
        print("subtraction")
        self.calcSession.find_element_by_name("Two").click()
        self.calcSession.find_element_by_name("Seven").click()
        self.calcSession.find_element_by_name("Minus").click()
        self.calcSession.find_element_by_name("Seven").click()
        self.calcSession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResult(), "20")

    def test_multiplication(self):
        print("multiplication")
        self.calcSession.find_element_by_name("Two").click()
        self.calcSession.find_element_by_name("Two").click()
        self.calcSession.find_element_by_name("Multiply by").click()
        self.calcSession.find_element_by_name("One").click()
        self.calcSession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResult(), "22")

    def test_division(self):
        print("division")
        self.calcSession.find_element_by_name("Two").click()
        self.calcSession.find_element_by_name("Seven").click()
        self.calcSession.find_element_by_name("Divide by").click()
        self.calcSession.find_element_by_name("Nine").click()
        self.calcSession.find_element_by_name("Equals").click()
        self.assertEqual(self.getDisplayResult(), "3")

    def getDisplayResult(self):
        calcresult = self.calcSession.find_element_by_accessibility_id(
            "CalculatorResults")
        return calcresult.text.strip("Display is").strip(" ")

    def test_SelectAnotherCalculator(self):
        print("select Anptehr calculator")
        self.ChooseCalculator("Scientific Calculator")

    def ChooseCalculator(self, locator):
        self.calcSession.find_element_by_accessibility_id("TogglePaneButton").click()
        calcType = self.calcSession.find_elements_by_class_name("ListViewItem")
        print(locator)

        for typeC in calcType:
            if typeC.get_attribute("AutomationID") == locator:
                typeC.click()
                break
    
    def test_SelectAnotherCalculatorXpath(self):
        print("select Anptehr calculator")
        self.ChooseCalculatorXpath("Scientific Calculator")

    def ChooseCalculatorXpath(self, locator):
        self.calcSession.find_element_by_accessibility_id("TogglePaneButton").click()
        calcType = self.calcSession.find_elements_by_xpath("//ListItem")
        print(locator)
        
        for typeC in calcType:
            if typeC.get_attribute("AutomationID") == locator:
                typeC.click()
                break

