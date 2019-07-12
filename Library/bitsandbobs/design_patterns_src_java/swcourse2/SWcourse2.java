/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package swcourse2;

import Singleton.Singleton;
import Iterator.ConcreteTV;
import Factory.AbstractLoggerCreator;
import Factory.XMLLoggerCreator;


/**
 *
 * @author Jane
 */
public class SWcourse2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here

        Singleton singleton = Singleton.getInstance();

        //for the purposes of this example, create an XMLLoggerCreator directly,
        //but this would normally be passed to constructor for use.
        AbstractLoggerCreator creator = new XMLLoggerCreator();

        FactoryClient client = new FactoryClient();
        client.someMethodThatLogs(creator);

    }
}
