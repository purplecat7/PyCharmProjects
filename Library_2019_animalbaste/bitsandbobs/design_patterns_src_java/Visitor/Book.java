/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package Visitor;

/**
 *
 * @author Jane
 */
//concrete element
public class Book implements Visitable {

    private double price;
    private double weight;

    /**
     * accept the visitor
     *
     * @param visitor
     */
    @Override
    public void accept(Visitor visitor) {
        visitor.visit(this);
    }

    public double getPrice() {
        return price;
    }

    public double getWeight() {
        return weight;
    }
}
