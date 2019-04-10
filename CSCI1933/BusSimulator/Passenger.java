public class Passenger {
    public static int totalRiders = 0;
    private double timeOn;
    private double timeOff;
    private int stopOn;
    private int stopOff;
    private double stopTime; //the time they arrived at the stop

    public Passenger(double t, int s){
        stopTime = t;
        stopOn = s;
        stopOff = getOff(s);
        totalRiders++;
    }

    private int getOff(int s){
        while (true){
            int randStop = (int) (Math.random() * 10);
            if (randStop != stopOn) return randStop;
        }

    }

    public String toString() {
        return "Stop On: " + stopOn + "\n" + "Stop Off: " + stopOff + "\n";
    }

    public double getTimeOn(){
        return timeOn;
    }
    public double getTimeOff(){
        return timeOff;
    }
    public double getStopTime(){
        return stopTime;
    }
    public int getStopOn(){
        return stopOn;
    }
    public int getStopOff(){
        return stopOff;
    }
}
