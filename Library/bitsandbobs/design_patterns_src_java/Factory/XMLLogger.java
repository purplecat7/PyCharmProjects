/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Factory;

/**
 *
 * @author Jane
 */
//concrete implementation of the Logger (Product)
public class XMLLogger implements Logger {

    public void log(String message) {
        //log to xml
        System.err.println("logging");
    }
}