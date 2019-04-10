import org.junit.Test;

import static org.junit.Assert.*;
//riehl046

public class ArrayListTest {
    Elephant one = new Elephant("Avery",14,14);
    Elephant two = new Elephant("Bob",15,16);
    Elephant three = new Elephant("Carl",5,7);
    Elephant four = new Elephant("Derek",9,2);
    Elephant five = new Elephant("Zach",19,6.33);

    @Test
    public void addElement() {
        ArrayList test = new ArrayList();
        test.add(one);
        String string = one.toString() + '\n';
        assertTrue(string.equals( test.toString()));
    }

    @Test
    public void contains() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        assertTrue(test.contains(one));
    }

    @Test
    public void addIndex() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(2,five);
        String string = one.toString() + '\n' + two.toString() + '\n' + five.toString() + '\n' + three.toString() + '\n' + four.toString() + '\n';
        assertTrue(test.toString().equals(string));
    }

    @Test
    public void isEmpty() {
        ArrayList test = new ArrayList();
        assertTrue(test.toString().equals("Empty List"));
    }

    @Test
    public void removeElement() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.remove(two);
        String string = one.toString() + '\n' + three.toString() + '\n';
        assertTrue(test.toString().equals(string));
    }

    @Test
    public void indexOf() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        int index = test.indexOf(two);
        assertTrue(index == 1);

    }

    @Test
    public void lastIndexOf() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        int index = test.lastIndexOf(one);
        assertTrue(index == 3);
    }

    @Test
    public void size() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        assertTrue(test.size() == 4);

    }

    @Test
    public void get() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        String string = two.toString();
        assertTrue(test.get(1).toString().equals(string));
    }

    @Test
    public void removeIndex() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        test.remove(1);
        String string = one.toString() + '\n' + three.toString() + '\n' + one.toString() + '\n';
        assertTrue(test.toString().equals(string));
    }

    @Test
    public void set() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(one);
        test.set(1,five);
        String string = one.toString() + '\n' + five.toString() + '\n' + three.toString() + '\n' + one.toString() + '\n';
        assertTrue(test.toString().equals(string));

    }

    @Test
    public void clear() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(2,five);
        test.clear();
        assertTrue(test.toString().equals("Empty List"));
    }

    @Test
    public void sort() {
        ArrayList test = new ArrayList();
        test.add(one);
        test.add(two);
        test.add(three);
        test.add(four);
        test.add(five);
        ArrayList upSort = new ArrayList();
        upSort.add(one);
        upSort.add(two);
        upSort.add(three);
        upSort.add(four);
        upSort.add(five);
        ArrayList downSort = new ArrayList();
        downSort.add(five);
        downSort.add(four);
        downSort.add(three);
        downSort.add(two);
        downSort.add(one);

        test.sort(false);
        assertTrue(test.toString().equals(downSort.toString()));
        test.sort(true);
        assertTrue(test.toString().equals(upSort.toString()));


    }
}