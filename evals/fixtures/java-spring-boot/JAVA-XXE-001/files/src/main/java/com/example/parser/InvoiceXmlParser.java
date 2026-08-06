package com.example.parser;

import org.w3c.dom.Document;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import java.io.InputStream;

public class InvoiceXmlParser {

    // Vulnerable: DocumentBuilderFactory is used with its default settings,
    // which leaves external entity resolution and external DTD loading
    // enabled. A crafted invoice upload containing a DOCTYPE with an
    // external entity (e.g. one that reads file:///etc/passwd or a
    // cloud-metadata URL and reflects it back into a parsed field) is
    // resolved by this parser - a classic XXE vulnerability that can leak
    // local files or make the server issue attacker-chosen requests.
    public Document parseInvoice(InputStream xmlInput) throws Exception {
        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        return builder.parse(xmlInput);
    }
}
