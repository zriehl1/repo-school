public class PassengerEvent implements IEvent {
    private int stop;
    private boolean downtown = false;

    public PassengerEvent(int stop){
        this.stop = stop;
    }
    public PassengerEvent(int stop, boolean downtown){
        this.stop = stop;
        this.downtown = downtown;
    }


    public void run(){
        double time = BusSimulator.agenda.getCurrentTime();
        BusSimulator.stops[stop].addPassenger(new Passenger(time,stop));
        BusSimulator.agenda.add(this, getNextTime());
    }

    private double getNextTime(){
        double time = 120;
        return time;
    }
    public int getStop(){
        return stop;
    }
}
