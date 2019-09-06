
package service;

import java.io.FileNotFoundException;
import javax.jws.WebMethod;
import javax.jws.WebService;
import javax.xml.xpath.XPathExpressionException;

/**
 *
 * @Gorana Matuh
 */

@WebService
public interface Translator {
    
    @WebMethod
    String translate (String word, String original, String translateTo) throws FileNotFoundException,XPathExpressionException;
    
}
