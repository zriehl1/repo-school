//riehl046 taken from LAB10


// Example 27a
// Priority Queue and Simulation
// Segment class used in priority queue (PQ.java)
// Uses queue class Q.java

public class Segment {

    private double time;
    private Q q;
    private Segment next;

    // constructor

    public Segment(double t) {
        time = t;
        q = new Q();
        next = null;
    }

    // methods

    public double getTime() {
        return time;
    }

    public Q getEvents() {
        return q;
    }

    public Segment getNext() {
        return next;
    }

    public void setNext(Segment nextSegment) {
        next = nextSegment;
    }

}  // Segment class