package service;

import java.io.FileNotFoundException;
import javax.jws.WebService;
import javax.xml.xpath.XPathExpressionException;

/**
 *
 * @Gorana Matuh
 */
@WebService(endpointInterface = "service.Translator")
public class TranslatorImpl implements Translator {

    @Override
    public String translate(String word, String original, String translateTo) throws FileNotFoundException,XPathExpressionException{
        DataSources ds = new DataSources();
        return ds.translation(word, original, translateTo);
    }

}
