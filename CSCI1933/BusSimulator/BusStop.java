public class BusStop {
    private Q<Passenger> eastbound;
    private Q<Passenger> westbound;
    private int stopNum;
    public String name;

    public BusStop(String name, int num){
        this.name = name;
        stopNum = num;
        eastbound = new Q<>();
        westbound = new Q<>();
    }

    public boolean addPassenger(Passenger p){
        if (p == null) return false;
        if (p.getStopOff() > stopNum){
            eastbound.add(p);
            return true;
        }
        else if (p.getStopOff() < stopNum){
            westbound.add(p);
            return true;
        }
        return false;

    }

    public Passenger removeEastbound(){
        return eastbound.remove();
    }

    public Passenger removeWestbound(){
        return westbound.remove();
    }

    public int getNumRiders(){
        return eastbound.length() + westbound.length();
    }

    public int watingEast(){
        return eastbound.length();
    }

    public int waitingWest(){
        return westbound.length();
    }
}
