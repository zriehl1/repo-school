import org.junit.Test;

import static org.junit.Assert.*;
//riehl046

public class ElephantHerdTest {
    Elephant one = new Elephant("Zach",100,100);
    Elephant two = new Elephant("Fred",80,80);
    Elephant three = new Elephant("Bruce",30,6.3);
    Elephant four = new Elephant("King Alex III",-40,60);
    Elephant five = new Elephant("Alfred",65,6.1);

    @Test
    public void add() {
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        test.add(two);
        String string = one.toString() + '\n' + two.toString() + '\n';
        assertTrue(test.toString().equals(string));
    }

    @Test
    public void find() {
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        assertTrue(test.find("Alex").equals(four));

    }

    @Test
    public void remove() {
        ElephantHerd compareTo = new ElephantHerd();
        compareTo.add(one);
        compareTo.add(three);
        compareTo.add(four);
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.remove(1);
        assertTrue(test.toString().equals(compareTo.toString()));
    }

    @Test
    public void sort() {
        ElephantHerd compareTo = new ElephantHerd();
        compareTo.add(one);
        compareTo.add(two);
        compareTo.add(four);
        compareTo.add(three);
        compareTo.add(five);
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        test.sort();
        assertTrue(compareTo.toString().equals(test.toString()));

    }

    @Test
    public void toStringTwo() {
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        String sting = one.toString() + '\n';
        assertTrue(test.toString().equals(sting));
    }

    @Test
    public void getTopKLargestElephants() {
        Elephant[] compareTo = {one,two,four};
        ElephantHerd test = new ElephantHerd();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        Elephant[] result = test.getTopKLargestElephants(3);
        for (int i = 0; i < 3; i++){
            assertTrue(compareTo[i].toString().equals(result[i].toString()));
        }

    }
}