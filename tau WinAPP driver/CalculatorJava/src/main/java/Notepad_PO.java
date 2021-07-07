import io.appium.java_client.windows.WindowsDriver;
import org.openqa.selenium.WebElement;

public class Notepad_PO {
    private WindowsDriver driver = null;
    public Notepad_PO(WindowsDriver wd){
        driver = wd;
    }

    public WebElement Minimize(){
        return driver.findElementByName("Minimize");
    }
    public WebElement Maximize(){
        return driver.findElementByName("Maximize");
    }
    public WebElement CLose(){
        return driver.findElementByName("CLose");
    }

    public WebElement MenuFile(){
        return driver.findElementByName("File");
    }

    public WebElement TextArea(){
        return driver.findElementByName("Text Editor");
    }

    public WebElement DialogSave(){
        return driver.findElementByName("Save");
    }
    public WebElement DialogDontSave(){
        return driver.findElementByName("Don't Save");
    }

    public WebElement DialogCancel(){
        return driver.findElementByName("Cancel");
    }


}
