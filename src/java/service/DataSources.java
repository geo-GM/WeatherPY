package service;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import javax.xml.xpath.XPath;
import javax.xml.xpath.XPathConstants;
import javax.xml.xpath.XPathExpression;
import javax.xml.xpath.XPathExpressionException;
import javax.xml.xpath.XPathFactory;
import org.xml.sax.InputSource;

/**
 *
 * @Gorana Matuh
 */
class DataSources {

    public String translation(String word, String original, String translateTo) throws XPathExpressionException, FileNotFoundException {

        XPathFactory xpf = XPathFactory.newInstance();
        XPath xp = xpf.newXPath();
        XPathExpression expr = xp.compile("//word [english = '" + word + "']/german");

        File xmlDocument = new File(DataSources.class.getResource("/resources/wordbook.xml").getFile());;
        InputSource inputSource = new InputSource(new FileInputStream(xmlDocument));
        String translated = (String) expr.evaluate(inputSource, XPathConstants.STRING);

        if (translated.isEmpty()| original.isEmpty() | translateTo.isEmpty()) {
            String notExist = "Word does not exist, try another word";
            return notExist;
        } else {
            return translated;
        }
    }

}
