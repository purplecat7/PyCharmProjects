/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Iterator;

import java.util.List;

/**
 *
 * @author Jane
 */
//Concrete Aggregator
public class ConcreteTV {

    private ChannelIterator iterator;
    private List<String> channels;

    public ConcreteTV() {
        iterator = new ConcreteChannelIterator(channels);
    }

    public ChannelIterator getIterator() {
        return iterator;
    }
}
