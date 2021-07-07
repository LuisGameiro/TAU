import io.appium.java_client.windows.WindowsDriver;
import org.aspectj.lang.annotation.After;
import org.openqa.selenium.Keys;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.Assert;
import org.testng.annotations.AfterClass;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.net.MalformedURLException;
import java.net.URL;

public class Notepad_test {
    private WindowsDriver notepad = null;
    private Notepad_PO np = null;

    @BeforeClass
    public void setup(){
        System.out.println("setup");
        DesiredCapabilities capabilities = new DesiredCapabilities();
        capabilities.setCapability("app","notepad.exe");
        try{
            notepad = new WindowsDriver(new URL("http://127.0.0.1:4723"),capabilities);
            np =  new Notepad_PO(notepad);
        } catch (MalformedURLException e){
            e.printStackTrace();
        }

    }
    @AfterClass
    public void teardown(){
        System.out.println("teardown");
        notepad.quit();

    }

    @Test
    public void testNotepad(){
        System.out.println("Test Notepad");
        String text = "Windriver is awesome";
        np.TextArea().sendKeys(text);
        Assert.assertEquals(np.TextArea().getText(), text);


        np.TextArea().sendKeys(Keys.ALT,Keys.F4);
        np.DialogCancel().click();
        np.TextArea().sendKeys(Keys.ALT,Keys.F4);
        np.DialogDontSave().click();
    }

}
