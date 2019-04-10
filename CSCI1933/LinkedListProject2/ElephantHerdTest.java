//riehl046
import org.junit.Test;

import static org.junit.Assert.*;

public class ElephantHerdTest {
    Elephant one = new Elephant("zach",12,15);
    Elephant two = new Elephant("fred",15,14);
    Elephant three = new Elephant("george",14,1);
    Elephant four = new Elephant("Avery",5,7);

    @Test
    public void add() {
        System.out.println("ADD TEST");
        ElephantHerd test1 = new ElephantHerd();
        test1.add(one);
        test1.add(two);
        System.out.println(test1.toString());
        String string = one.toString() + '\n' + two.toString() + '\n';
        assertTrue(test1.toString().equals(string));
    }

    @Test
    public void find() {
        System.out.println("FIND TEST");
        ElephantHerd test2 = new ElephantHerd();
        test2.add(one);
        test2.add(two);
        test2.add(three);
        test2.add(four);
        Elephant found = test2.find("george");
        System.out.println(found.toString() + '\n');
        assertTrue(found == three);
    }

    @Test
    public void remove() {
        System.out.println("REMOVE TEST");
        ElephantHerd test3 = new ElephantHerd();
        test3.add(one);
        test3.add(two);
        test3.add(three);
        test3.add(four);
        test3.remove(1);
        String string = one.toString() + '\n' + three.toString() + '\n' + four.toString() + '\n';
        System.out.println(test3.toString());
        assertTrue(test3.toString().equals(string));
    }

    @Test
    public void sort() {
        System.out.println("SORT TEST");
        ElephantHerd test4 = new ElephantHerd();
        test4.add(one);
        test4.add(two);
        test4.add(three);
        test4.add(four);
        test4.sort();
        String string = one.toString() + '\n' + two.toString() + '\n' + four.toString() + '\n' + three.toString() + '\n';
        System.out.println(test4.toString());
        assertTrue(test4.toString().equals(string));

    }


    @Test
    public void getTopKLargestElephants() {
        System.out.println("LARGEST TEST");
        ElephantHerd test5 = new ElephantHerd();
        test5.add(one);
        test5.add(two);
        test5.add(three);
        test5.add(four);
        Elephant[] test6 = test5.getTopKLargestElephants(2);
        for (int i = 0; i < 2; i++){
            System.out.println(test6[i].toString());
        }
        assertTrue(test6[0].toString().equals(one.toString()));
        assertTrue(test6[1].toString().equals(two.toString()));
    }
}