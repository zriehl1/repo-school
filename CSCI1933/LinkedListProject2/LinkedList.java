//riehl046
public class LinkedList<T extends Comparable<T>> implements List<T>{
    private Node<T> DUMMYNODE;
    private int next;
    private Node<T> last;
    private boolean isSorted;

    public LinkedList(){
        DUMMYNODE = new Node<T>(null);
        last = DUMMYNODE;
        next = 0;
        isSorted = true;

    }

    public boolean add(T element) {
        if (element == null) return false;
        Node<T> newNode = new Node<T>(element);
        last.setNext(newNode);
        last = newNode;
        isSorted = false;
        next ++;
        return true;

    }

    public boolean add(int index, T element) {
        if (index < 0 || index > next || element == null) return false;
        if (index == next) return add(element);
        Node<T> trailer = DUMMYNODE;
        Node<T> current = DUMMYNODE.getNext();
        for (int i = 0; i < index; i++){
            trailer = current;
            current = current.getNext();
        }
        Node<T> newNode = new Node<T>(element,current);
        trailer.setNext(newNode);
        isSorted = false;
        next++;
        return true;
    }

    public void clear() {
        next = 0;
        isSorted = true;
        DUMMYNODE.setNext(null);
    }

    public boolean contains(T element){
        if (isSorted); //it doesn't really matter if its sorted since you can't jump to an index
        Node<T> current = DUMMYNODE.getNext();
        for (int i = 0; i < next; i++){
            if (current.getData().toString().equals(element) || current.getData() == element || current.getData().toString().compareTo(element.toString()) == 0) return true;
            current = current.getNext();
        }
        return false;
    }

    public int indexOf(T element){
        if (isSorted); //it doesn't really matter if its sorted, you cant jump to an index anyways
        Node<T> current = DUMMYNODE.getNext();
        for (int i = 0; i < next; i++){
            if (current.getData().toString().compareTo(element.toString()) == 0) return i;
            current = current.getNext();
        }
        return -1;
    }

    public boolean isEmpty() {
        if (next == 0) return true;
        return false;
    }

    public int lastIndexOf(T element) {
        if (isSorted); //being sorted doesn't help since you can't jump to an index
        int returnMe = -1;
        Node<T> current = DUMMYNODE.getNext();
        if (current.getData().toString().compareTo(element.toString()) == 0) return 0;
        for (int i = 0; i < next; i++){
            if (current.getData().equals(element) || current.getData() == element || current.getData().compareTo(element) == 0) returnMe = i;
            current = current.getNext();
        }
        return returnMe;
    }

    public T set(int index, T element) {
        if (index < 0 || index > next || element == null) return null;
        int count = 0;
        Node<T> current = DUMMYNODE.getNext();
        while (count < index){
            current = current.getNext();
            count++;
        }
        T data = current.getData();
        current.setData(element);
        return data;
    }

    public int size() {
        return next;
    }

    public void sort(boolean order) {
        if (next == 1 || next == 0) return;
        if (isSorted && order) return;
        if (order){
            isSorted = true;
            sortAscending();
        }
        else{
            isSorted = false;
            sortDescending();
        }

    }

    public void sortAscending(){
      Node<T> current = DUMMYNODE.getNext();
      Node<T> compare = DUMMYNODE;
      if (current.getData() == null) return;
      for (int i = 0; i < next; i++){
          current = DUMMYNODE.getNext();
          compare = DUMMYNODE;
          for (int j = 0; j < next - i - 1; j++){
              current = current.getNext();
              compare = compare.getNext();
              if (compare.getData().toString().compareTo(current.getData().toString()) > 0){
                  T temp = compare.getData();
                  compare.setData(current.getData());
                  current.setData(temp);
              }


          }
      }

    }

    public void sortDescending(){
        Node<T> current = DUMMYNODE.getNext();
        Node<T> compare = DUMMYNODE;
        if (current.getData() == null) return;
        for (int i = 0; i < next; i++){
            current = DUMMYNODE.getNext();
            compare = DUMMYNODE;
            for (int j = 0; j < next - i - 1; j++){
                current = current.getNext();
                compare = compare.getNext();
                if (compare.getData().toString().compareTo(current.getData().toString()) <= 0){
                    T temp = compare.getData();
                    compare.setData(current.getData());
                    current.setData(temp);
                }


            }
        }

    }

    public boolean remove(T element) {
        if (element == null) return false;
        Node<T> current = DUMMYNODE.getNext();
        Node<T> trailer = DUMMYNODE;
        for (int i = 0; i < next; i++){
            if (current.getData().toString().compareTo(element.toString()) == 0){
                trailer.setNext(current.getNext());
                next--;
                return true;
            }
            trailer = current;
            current = current.getNext();
        }

        return false;
    }

    public T remove(int index) {
        if (index < 0 || index > next) return null;
        Node<T> current = DUMMYNODE.getNext();
        Node<T> trailer = DUMMYNODE;
        int count = 0;
        while (count < index){
            trailer = current;
            current = current.getNext();
            count++;
        }
        T data = current.getData();
        trailer.setNext(current.getNext());
        next--;
        return data;
    }

    public T get(int index) {
        if (index < 0 || index > next) return null;
        int count = 0;
        Node<T> current = DUMMYNODE.getNext();
        while (count < index){
            current = current.getNext();
            count++;
        }
        return current.getData();
    }

    public String toString() {
        if (next == 0) return "No Entries Yet";
        String returnMe = "";
        Node<T> current = DUMMYNODE.getNext();
        for (int i = 0; i < next; i++){
            returnMe += current.getData().toString() + "\n";
            current = current.getNext();

        }
        return returnMe;
    }

    public int getNext() {
        return next;
    }

    public Node getStartNode(){
        return DUMMYNODE;
    }
}
