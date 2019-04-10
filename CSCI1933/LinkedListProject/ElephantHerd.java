//riehl046
//bubble sort methods taken from lecture

public class ElephantHerd {
    private ArrayList<Elephant> list;

    public ElephantHerd(){
        list = new ArrayList<Elephant>();
    }

    public boolean add(Elephant ellie){
        //just passes the Elephant to the ArrayList.add method
        return list.add(ellie);

    }

    public Elephant find(String name){
        //sorts and then searches for a name that contains the string. Linear search
        int max = list.getNext();
        Elephant[] all = getElephants();
        for (int count = 0; count < max; count++){
            if (all[count].name.contains(name)) return all[count];

        }
        return null;


    }

    public Elephant remove(int index){
        //see ArrayList remove
        return list.remove(index);

    }

    public void sort(){
        //Utilizes bubble sort, taken from lecture, pulls elements into list, sorts list and puts them back into ArrayList
        Elephant[] toSort = getElephants();
        toSort = makeSortedList(toSort);
        placeIntoList(toSort);
        list.setSorted(true);

    }
    public Elephant[] makeSortedList(Elephant[] toSort){
        int len = toSort.length;
        for (int count = 0; count < len; count++){
            for (int move = 0; move < len - count - 1; move++){
                if (toSort[move].height < toSort[move+1].height) {
                    Elephant temp = toSort[move];
                    toSort[move] = toSort[move+1];
                    toSort[move+1] = temp;
                }
            }
        }
        return toSort;

    }
    public void placeIntoList(Elephant[] sorted){
        //replaces the newly sorted elements into ArrayList using ArrayList.set(index)
        int len = sorted.length;
        for (int count = 0; count < len; count++){
            list.set(count,sorted[count]);
        }
    }

    public Elephant[] getElephants(){
        //pulls the non-null elements of the ArrayList to a list that can be edited.
        int max = list.getNext();
        Elephant[] returnMe = new Elephant[max];
        for (int count = 0; count < max; count++){
            returnMe[count] = list.get(count);
        }
        return returnMe;
    }

    public String toString() {
        return list.toString();
    }

    public int getNext(){
        return list.getNext();
    }

    public Elephant[] getTopKLargestElephants(int k){
        Elephant[] all = getElephants();
        Elephant[] returnMe;
        int len = k;
        int maxPos = list.getNext();
        if (maxPos == 0) return null;
        if (maxPos < k) len = maxPos;
        returnMe = new Elephant[len];
        all = makeSortedList(all);
        for (int count = 0; count < len; count++){
            returnMe[count] = all[count];
        }
        return returnMe;

    }
}
