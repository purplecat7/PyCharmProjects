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
//Concrete Iterator
//Iterator interface 
public class ConcreteChannelIterator implements ChannelIterator {

    private List<String> channels;
    private int currentPos = 0;

    public ConcreteChannelIterator (List<String> channels) {
        this.channels = channels;
    }

    @Override
    public boolean hasNext() {
        if (currentPos + 1 < channels.size()) {
            return true;
        }
        return false;
    }

    @Override
    public void next() {
        currentPos++;
    }

    @Override
    public String currentItem() {
        return channels.get(currentPos);
    }
}
