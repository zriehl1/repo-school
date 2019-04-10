public class Test {
    public static void main(String[] args){
        Passenger test = new Passenger(2,2);
        Passenger test2 = new Passenger(2,2);
        test2 = null;
        System.out.println(Passenger.totalRiders);
    }
}
