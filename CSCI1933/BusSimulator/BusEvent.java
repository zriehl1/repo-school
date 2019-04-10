public class BusEvent implements IEvent {
    private int currStop;
    private Bus bus;
    private boolean direction = true; //false is west (neg), true is east (pos)
    private int totalWait;

    public BusEvent(int stop){
        currStop = stop;
        bus = new Bus();
        totalWait = 0;
    }

    public BusEvent(int stop, Bus bus, boolean direction){
        currStop = stop;
        this.bus = bus;
        this.direction = direction;
        totalWait = 0;
    }

    public int getCurrStop(){
        return currStop;
    }
    public void run(){
        if (currStop == 9) direction = false;
        else if (currStop == 0) direction = true;
        //remove passengers at stop
        Passenger[] removed = bus.remove(currStop);
        double time = (double) (removed.length * 2);
        if (time != 0){
            totalWait += time;
            BusSimulator.agenda.add(this,time);
            return;
        }

        //add new passengers and continue
        double loadTime = loadNew();
        if (loadTime != 0){
            BusSimulator.agenda.add(this,loadTime*3);
            totalWait += loadTime;
            return;
        }
        // makes sure the stop takes at least 15 seconds
        if (totalWait < 15){
            totalWait = 15;
            BusSimulator.agenda.add(this,15 - totalWait);
            return;
        }
        //stats gather
        Stats.queueLength += bus.getNumRiders();
        Stats.div += 1;

        //moves on to next stop
        int nextStop = getNextStop();
        //System.out.println(nextStop);
        BusSimulator.agenda.add(new BusEvent(nextStop,bus,direction),180);
    }
    private int getNextStop(){
        if (currStop == 9){
            direction = false;
            return 8;
        }
        if (currStop == 0){
            direction = true;
            return 1;
        }
        if (direction){
            return currStop + 1;
        }
        else return currStop - 1;
    }

    private int loadNew(){
        int ret = 0;
        if (direction){
            while (bus.getNumRiders() < 40 && BusSimulator.stops[currStop].watingEast() > 0){
                ret++;
                bus.add(BusSimulator.stops[currStop].removeEastbound());
            }
        }
        else{
            while (bus.getNumRiders() < 40 && BusSimulator.stops[currStop].waitingWest() > 0){
                ret++;
                bus.add(BusSimulator.stops[currStop].removeWestbound());
            }
        }
        return ret;

    }
}
