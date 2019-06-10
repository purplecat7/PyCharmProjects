/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package swcourse2;
import Factory.AbstractLoggerCreator;
import Factory.Logger;

/**
 *
 * @author Jane
 */
public class FactoryClient {

    public void someMethodThatLogs(AbstractLoggerCreator logCreator) {
        Logger logger = logCreator.createLogger();
        logger.log("message");

    }
}
