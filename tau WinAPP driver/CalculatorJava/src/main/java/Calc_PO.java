import io.appium.java_client.windows.WindowsDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.RemoteWebDriver;
public class Calc_PO {
    private WindowsDriver driver = null;

    public Calc_PO(WindowsDriver wd){
        driver = wd;

    }

    public WebElement One(){
        return driver.findElementByName("One");

    }
    public WebElement Two(){
        return driver.findElementByName("Two");

    }
    public WebElement Three(){
        return driver.findElementByName("Three");

    }
    public WebElement Four(){
        return  driver.findElementByName("Four");

    }
    public WebElement Five(){
        return driver.findElementByName("Five");

    }
    public WebElement Six(){
        return driver.findElementByName("Six");

    }
    public WebElement Seven(){
        return driver.findElementByName("Seven");

    }
    public WebElement Eight(){
        return driver.findElementByName("Eight");

    }
    public WebElement Nine(){
        return driver.findElementByName("Nine");

    }
    public WebElement Zero(){
        return driver.findElementByName("Zero");

    }
    public WebElement Equals(){
        return driver.findElementByName("Equals");

    }
    public WebElement Plus(){
        return driver.findElementByName("Plus");

    }

    public String GetResultDisplayed(){
        return driver.findElementByAccessibilityId("CalculatorResults").getText().replace("Display is","").trim();

    }

}
