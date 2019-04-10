// riehl046
//bubble sorting methods taken from lecture


public class ArrayList<T extends Comparable<T>> implements List<T> {
    private T[] arrayList;
    private int next = 0;
    private boolean isSorted = true;

    public ArrayList(){
        arrayList = (T[]) new Comparable[2];
    }

    public boolean add(T element) {
        //adds the element to the end of the list
        //if the element is null, or crashes the program, returns false
        if (element == null) return false;
        if (next == arrayList.length){
            increaseSize();
        }
        try {
            arrayList[next] = element;
            next++;
            isSorted = false;
            return true;
        }
        catch (Exception e) {
            return false;
        }
    }

    public boolean contains(T element) {
        //makes sure that the list contains something; if its sorted, it uses the same method as the find element
        //else it goes through linearly and compares pretty much everything for a match
        if (next == 0) return false;
        if (isSorted){
             int index = sortedSearch(element);
             if (index == -1) return false;
             return true;
        }
        else{
            for (int count = 0; count < next; count++){
                if (arrayList[count] == element || arrayList[count].equals(element) || arrayList[count].toString().compareTo(element.toString()) == 0) return true;
            }
        }



        return false;
    }
    public int lastFindSorted(T element){
        //determines whether the element is "larger" or "smaller" than the value at the midpoint
        //if its larger, it searches backwards from the top and returns the first element that matches if any
        //else it searches backwards from the midpoint
        int midpoint = Math.floorDiv(next,2);
        int startSearch;
        int finishSearch;
        if (arrayList[midpoint].toString().compareTo(element.toString()) >= 0){
            startSearch = next - 1;
            finishSearch = midpoint - 1;
        }
        else{
            startSearch = midpoint - 1;
            finishSearch = 0;
        }
        for (int count = startSearch; count > finishSearch; count--){
            if (arrayList[count].toString().compareTo(element.toString()) == 0) return count;
        }
        return -1;

    }

    public int sortedSearch(T element){
        //does exactly the same thing as lastFindSorted, except it goes through the list from left to right, as opposed to right to left
        int midpoint = Math.floorDiv(next,2);
        int startSearch;
        int finishSearch;
        if (arrayList[midpoint].toString().compareTo(element.toString()) <= 0){
            startSearch = 0;
            finishSearch = midpoint + 1;
        }
        else{
            startSearch = midpoint;
            finishSearch = next;
        }
        for (int count = startSearch; count < finishSearch; count++){
            if (arrayList[count].toString().compareTo(element.toString()) == 0) return count;
        }
        return -1;
    }

    public boolean add(int index, T element) {
        //attampts to add the element at the given index, shifting all the ones to the right over one
        //fails if you input the index of the last element (this is what the directions said? to change this you can delete the equals sign from index >= size)
        //or if the index is out of bounds (bigger or smaller than the array)
        T last;
        if (element == null) return false;
        int size = next;
        if (index < 0 || index >= size) return false;
        //else if (index == 0) return add(element);
        else{
            if (next == arrayList.length) increaseSize();
            last = arrayList[next-1];
            for (int count = size; count > index; count--){
                arrayList[count] = arrayList[count-1];

            }
            arrayList[next] = last;
            arrayList[index] = element;
            isSorted = false;
            next++;
            return true;

        }


    }

    public boolean isEmpty() {
        //if the next value is 0, by default there are no elements within
        if (next == 0) return true;
        return false;
    }

    public boolean remove(T element) {
        //searches linearly through the list, finds the first occurrence of an element and removes it, shifting all others to the left
        for (int count = 0; count < next; count++){
            //System.out.println(arrayList[count].toString() + "-->" + element.toString());
            if (arrayList[count].compareTo(element) == 0){
                for (int move = count; move < next - 1; move++){
                    arrayList[move] = arrayList[move+1];
                }
                arrayList[next-1] = null;
                next--;
                return true;
            }
        }
        return false;
    }

    public int indexOf(T element) {
        //finds the first occurrence of the element, linearly if unsorted or using the midpoint function if it is sorted
        if (next == 0) return -1;
        if (isSorted) return sortedSearch(element);
        for (int count = 0; count < next; count++){
            if (arrayList[count].toString().compareTo(element.toString()) == 0) return count;
        }
        return -1;
    }

    public int lastIndexOf(T element) {
        //same as indexOf, except if it is sorted calls lastFindSorted
        if (next == 0) return -1;
        if (isSorted) return lastFindSorted(element);
        for (int count = next -1; count > 0; count--){
            if (arrayList[count].toString().compareTo(element.toString()) == 0) return count;
        }
        return -1;
    }

    public int size() {
        return next;
    }

    public T get(int index) {
        try {
            return arrayList[index];
        }
        catch (Exception e){
            return null;
        }
    }

    public T remove(int index) {
        //removes value at the index, shifts all elements to the left and decrements next
        T returnMe;
        if (index >= next || index < 0) return null;
        returnMe = arrayList[index];
        for (int count = index; count < next - 1; count++){
            arrayList[count] = arrayList[count + 1];
        }
        arrayList[next-1] = null;
        next--;
        return returnMe;
    }

    public T set(int index, T element) {
        //replaces the value at the index if possible, and returns the old value
        T returnMe;
        if (index >= next || index < 0) return null;
        returnMe = arrayList[index];
        arrayList[index] = element;
        return returnMe;
    }

    public void clear() {
        // "clears" the array by making an entirely new one
        arrayList = (T[]) new Comparable[2];
        next = 0;
        isSorted = true;

    }

    public void sort(boolean order) {
        //passes to the appropriate sort function and sets isSorted
        if (order) sortAscending();
        else sortDecending();
        isSorted = true;

    }
    public void sortAscending(){
        //bubble sort taken from lecture
        for (int count = 0; count < next; count++){
            for (int move = 0; move < next - count - 1; move++){
                if (arrayList[move].toString().compareTo(arrayList[move+1].toString()) > 0){
                    T temp = arrayList[move];
                    arrayList[move] = arrayList[move+1];
                    arrayList[move+1] = temp;
                }

            }

        }
        isSorted = true;

    }

    public void sortDecending(){
        //bubble sort, but B A C K W A R D S
        for (int count = 0; count < next; count++){
            for (int move = 0; move < next - count - 1; move++){
                if (arrayList[move].toString().compareTo(arrayList[move+1].toString()) < 0){
                    T temp = arrayList[move];
                    arrayList[move] = arrayList[move+1];
                    arrayList[move+1] = temp;
                }

            }

        }
        isSorted = true;

    }

    public String toString() {
        //adds the string of every non-null element
        if (next == 0) return "Empty List";
        String returnMe = "";
        for (int count = 0; count < next; count++){
            returnMe += arrayList[count].toString() + "\n";
        }
        return returnMe;
    }

    public void increaseSize(){
        //doubles the length of the array, and transfers the values before returning new Array
        int len = arrayList.length;
        T[] newList = (T[]) new Comparable[len*2];
        for (int count = 0; count < len; count++){
            newList[count] = arrayList[count];
        }
        arrayList = newList;
    }

    //these bottom three are my cheaty getter methods

    public void setSorted(boolean val){
        isSorted = val;
    }
    public int getNext(){
        return next;
    }
    public T[] getArrayList(){
        return arrayList;
    }

}
