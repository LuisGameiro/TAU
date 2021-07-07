import io.appium.java_client.windows.WindowsDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.*;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.List;

public class Calculator {
    private WindowsDriver calcsession = null;
    private WebElement calcresult = null;

    @BeforeClass
    public void setup() throws MalformedURLException {
        System.out.println("setup");
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("app","Microsoft.WindowsCalculator_8wekyb3d8bbwe!App");
        calcsession = new WindowsDriver(new URL("http://127.0.0.1:4723"),capabilities);
    }
    @AfterClass
    public void teardown(){
        System.out.println("teardown");
        calcsession.quit();
    }
    @BeforeMethod
    public void clear(){
        System.out.println("clear");
        if (calcsession.findElementByName("Clear") != null) {
            calcsession.findElementByName("Clear").click();
        }
        else{
            calcsession.findElementByName("Clear entry").click();
        }

    }

    @Test
    public void addition(){
        System.out.println("addition test start");
        calcsession.findElementByName("One").click();
        calcsession.findElementByName("Two").click();
        calcsession.findElementByName("Plus").click();
        calcsession.findElementByName("Nine").click();
        calcsession.findElementByName("Equals").click();

        Assert.assertEquals(GetResultDisplayed(), "21");
    }
    @Test
    public void subtraction(){
        System.out.println("subtraction test start");
        calcsession.findElementByName("One").click();
        calcsession.findElementByName("Two").click();
        calcsession.findElementByName("Minus").click();
        calcsession.findElementByName("Nine").click();
        calcsession.findElementByName("Equals").click();

        Assert.assertEquals(GetResultDisplayed(), "3");
    }
    @Test
    public void multiplication(){
        System.out.println("multiplication test start");
        calcsession.findElementByName("One").click();
        calcsession.findElementByName("Two").click();
        calcsession.findElementByName("Multiply by").click();
        calcsession.findElementByName("Two").click();
        calcsession.findElementByName("Equals").click();

        Assert.assertEquals(GetResultDisplayed(), "24");
    }
    @Test
    public void division(){
        System.out.println("division test start");
        calcsession.findElementByName("Two").click();
        calcsession.findElementByName("Seven").click();
        calcsession.findElementByName("Divide by").click();
        calcsession.findElementByName("Nine").click();
        calcsession.findElementByName("Equals").click();

        Assert.assertEquals(GetResultDisplayed(), "3");
    }

    @Test
    public void SelectAnotherCalculator(){
        System.out.println("Selecting Another Calculator");
        ChooseCalculator("Scientific Calculator");
    }

    @Test
    public void SelectAnotherCalculatorXpath(){
        System.out.println("Selecting Another Calculator");
        ChooseCalculatorXpath("Scientific Calculator");
    }

    public String GetResultDisplayed(){
        calcresult = calcsession.findElementByAccessibilityId("CalculatorResults");
        return calcresult.getText().replace("Display is","").trim();

    }

    public void ChooseCalculator(String locator){
        calcsession.findElementByAccessibilityId("TogglePaneButton").click();

        List <WebElement> calcType = calcsession.findElementsByClassName("listViewItem");

        System.out.println(calcType.size());

        for (int i = 0; i<calcType.size(); i++){
            if (calcType.get(i).getAttribute("Name").equals("locator")){
                calcType.get(i).click();
                break;
            }
        }
    }
    public void ChooseCalculatorXpath(String locator){
        calcsession.findElementByAccessibilityId("TogglePaneButton").click();

        calcsession.findElementByXPath("//ListItem[contains(@Name,\"" + locator + "\")]").click();

        System.out.println("somehting");
    }
}
