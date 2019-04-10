public class BusSimulator {
    public static PQ agenda = new PQ();
    public static BusStop[] stops = new BusStop[10];

    public static void main(String[] args){
        //the 10 bus stops
        stops[0] = new BusStop("University Ave and 27th Street SE",0);
        stops[1] = new BusStop("Raymond Ave Station",1);
        stops[2] = new BusStop("University Ave and Fairview Ave",2);
        stops[3] = new BusStop("University Ave and Snelling Ave",3);
        stops[4] = new BusStop("University Ave and Lexington Parkway",4);
        stops[5] = new BusStop("University Ave and Dale Street", 5);
        stops[6] = new BusStop("University Ave and Marion Street",6);
        stops[7] = new BusStop("Cedar Street and 5th Street",7);
        stops[8] = new BusStop("Minnesota Street and 4th Street",8);
        stops[9] = new BusStop("Union Depot",9);
        //passenger events for each stop
        for (int i = 0; i < 10; i++){
            agenda.add(new PassengerEvent(i),0);
        }
        //bus events
        BusEvent One = new BusEvent(0);
        BusEvent Two = new BusEvent(8);
        BusEvent Three = new BusEvent(4);
        BusEvent Four = new BusEvent(6);
        agenda.add(One,0);
        //agenda.add(Two,0);
        //agenda.add(Three,0);
        //agenda.add(Four,0);

        while (agenda.getCurrentTime() <= 10000){
            agenda.remove().run();
            System.out.println(One.getCurrStop());

        }
        for (int i = 0; i < 10; i++){
            String print = "Stop " + i + " waitline: " + stops[i].getNumRiders();
            System.out.println(print);
        }
        System.out.println(agenda.getCurrentTime());
        System.out.print("Average number of people on the buses: ");
        System.out.println(Stats.queueLength/Stats.div);
        System.out.println("Number of passengers: " + Passenger.totalRiders);



    }
}
