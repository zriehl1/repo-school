//riehl046

import org.junit.Test;
import sun.awt.image.ImageWatched;

import static org.junit.Assert.*;

public class LinkedListTest {
    Elephant one = new Elephant("Zach",2,2);
    Elephant two = new Elephant("Albert",5,5);
    Elephant three = new Elephant("Jeff",3,3);
    Elephant four = new Elephant("Kody",4,4);
    Elephant five = new Elephant("Fred",9,9);

    @org.junit.Test
    public void add() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        String string = one.toString() + "\n" + two.toString() + "\n";
        assertTrue(test.toString().equals(string));

    }

    @org.junit.Test
    public void add1() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(1,three);
        String string = one.toString() + "\n" + three.toString() + "\n" + two.toString() + "\n";
        assertTrue(test.toString().equals(string));
    }

    @org.junit.Test
    public void clear() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        test.clear();
        String string = "No Entries Yet";
        assertTrue(test.toString().equals(string));
        assertTrue(test.getNext() == 0);
    }

    @org.junit.Test
    public void contains() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.contains(three));
        assertTrue(test.contains(five));
        assertTrue(test.contains(one));
    }

    @org.junit.Test
    public void indexOf() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.indexOf(two) == 1);
        assertTrue(test.indexOf(five) == 4);
    }

    @org.junit.Test
    public void isEmpty() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        assertTrue(test.isEmpty() == false);
        test.clear();
        assertTrue(test.isEmpty());
    }

    @org.junit.Test
    public void lastIndexOf() {
        LinkedList test = new LinkedList();
        test.add(five);
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        assertTrue(test.lastIndexOf(one) == 4);
        assertTrue(test.lastIndexOf(three) == 3);
        assertTrue(test.lastIndexOf(five) == 0);
    }

    @org.junit.Test
    public void set() {
        LinkedList test = new LinkedList();
        LinkedList test2 = new LinkedList();
        test2.add(one);
        test2.add(five);
        test2.add(three);
        test2.add(four);
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        assertTrue(test.set(1,five) == two);
        assertTrue(test.toString().equals(test2.toString()));

    }

    @org.junit.Test
    public void size() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        assertTrue(test.size() == 4);
    }

    @org.junit.Test
    public void sort() {
        LinkedList test = new LinkedList();
        LinkedList asce1 = new LinkedList();
        LinkedList asce2 = new LinkedList();
        asce1.add(two);
        asce1.add(five);
        asce1.add(three);
        asce1.add(four);
        asce1.add(one);
        asce2.add(one);
        asce2.add(four);
        asce2.add(three);
        asce2.add(five);
        asce2.add(two);

        test.add(one);
        test.add(two);
        test.add(four);
        test.add(three);
        test.add(five);
        test.sort(true);
        System.out.println(test.toString());
        assertTrue(test.toString().equals(asce1.toString()));
        test.sort(false);
        System.out.println(test.toString());
        assertTrue(test.toString().equals(asce2.toString()));
    }

    @org.junit.Test
    public void remove() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.remove(one));
        assertTrue(test.remove(three));
        assertTrue(test.remove(five));
    }

    @org.junit.Test
    public void remove1() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.remove(1) == two);
        assertTrue(test.remove(0) == one);
        assertTrue(test.remove(2) == five);
    }

    @org.junit.Test
    public void get() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.get(0) == one);
        assertTrue(test.get(4) == five);
        assertTrue(test.get(2) == three);

    }

    @org.junit.Test
    public void testString() {
        LinkedList test = new LinkedList();
        test.add(one);
        test.add(two);
        String string = one.toString() + "\n" + two.toString() + "\n";
        assertTrue(test.toString().equals(string));
    }

}