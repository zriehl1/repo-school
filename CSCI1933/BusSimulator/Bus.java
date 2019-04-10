public class Bus {
    private Q<Passenger>[] storage = new Q[10];
    private int capacity;

    public Bus(){
        setUp();
        capacity = 40;
    }
    public Bus(int size){
        setUp();
        capacity = size;
    }
    private void setUp(){
        for (int i = 0; i < 10; i++){
            storage[i] = new Q<>();
        }
    }
    public boolean add(Passenger p){
        if (isFull()) return false;
        int stop = p.getStopOff();
        storage[stop].add(p);
        return true;

    }

    public Passenger[] remove(int stop){
        if (stop > 10 || stop < 0) return null;
        int len = storage[stop].length();
        Passenger[] ret = new Passenger[len];
        for (int i = 0; i < len; i++){
            ret[i] = storage[stop].remove();
        }
        return ret;

    }

    public boolean isFull(){
        int people = getNumRiders();
        if (people == capacity) return true;
        return false;
    }
    public int getCapacity(){
        return capacity;
    }
    public int getNumRiders(){
        int ret = 0;
        for (int i = 0; i < 10; i++){
            ret += storage[i].length();
        }
        return ret;
    }
}
