/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Iterator;

/**
 *
 * @author Jane
 */
public interface ChannelIterator {

    public boolean hasNext();

    public void next();

    public String currentItem();
}
