/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Factory;

/**
 *
 * @author Jane
 */
//ConcreteCreator
public class XMLLoggerCreator extends AbstractLoggerCreator {

    @Override
    public Logger createLogger() {
        XMLLogger logger = new XMLLogger();
        return logger;
    }
}