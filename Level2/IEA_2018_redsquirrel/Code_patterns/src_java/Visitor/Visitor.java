/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Visitor;

/**
 *
 * @author Jane
 */
public interface Visitor {
    public void visit(Book book);
    //visit other concrete items
    //public void visit(CD cd);
    //public void visit(DVD dvd); 
}
