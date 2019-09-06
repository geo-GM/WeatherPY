
package service;

import java.io.FileNotFoundException;
import java.io.IOException;
import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.parsers.ParserConfigurationException;
import javax.xml.xpath.XPathExpressionException;
import org.xml.sax.SAXException;

/**
 *
 * @Gorana Matuh
 */

@WebService
public interface Translator {
    
    @WebMethod
    String translate (String word, String original, String translateTo) throws FileNotFoundException,XPathExpressionException;
    
}
