//riehl046
//bubble sort methods taken from lecture

public class ElephantHerd {
    private LinkedList<Elephant> list;

    public ElephantHerd(){
        list = new LinkedList<Elephant>();
    }

    public boolean add(Elephant ellie){
        //just passes the Elephant to the ArrayList.add method
        return list.add(ellie);

    }

    public Elephant find(String name){
        //sorts and then searches for a name that contains the string. Linear search
        int max = list.getNext();
        Node<Elephant> current = list.getStartNode().getNext();
        for (int i = 0; i < max; i++){
            if (current.getData().getName().contains(name)){
                return current.getData();
            }
            current = current.getNext();
        }
        return null;


    }

    public Elephant remove(int index){
        //see ArrayList remove
        return list.remove(index);

    }

    public void sort(){
        //Utilizes bubble sort, taken from lecture, pulls elements into list, sorts list and puts them back into ArrayList
        int max = getNext();
        Node<Elephant> current = list.getStartNode().getNext();
        Node<Elephant> compare = list.getStartNode();
        if (current.getData() == null) return;
        for (int i = 0; i < max; i++){
            current = list.getStartNode().getNext();
            compare = list.getStartNode();
            for (int j = 0; j < max - i - 1; j++){
                current = current.getNext();
                compare = compare.getNext();
                if (compare.getData().getHeight() < current.getData().getHeight()){
                    Elephant temp = compare.getData();
                    compare.setData(current.getData());
                    current.setData(temp);
                }


            }
        }

    }




    public String toString() {
        return list.toString();
    }

    public int getNext(){
        return list.getNext();
    }

    public Elephant[] getTopKLargestElephants(int k){
        if (k == 0) return null;
        int max = list.getNext();
        if (max < k) k = max;
        Elephant[] returnMe = new Elephant[k];
        sort();
        Node<Elephant> current = list.getStartNode().getNext();
        for (int i = 0; i < k; i++){
            returnMe[i] = current.getData();
            current = current.getNext();
        }
        return returnMe;
    }
}
