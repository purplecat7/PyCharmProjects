/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Visitor;

/**
 *
 * @author Jane
 */
public interface Visitable {
    public void accept(Visitor visitor);
}
