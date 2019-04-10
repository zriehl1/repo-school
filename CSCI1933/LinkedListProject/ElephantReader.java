import java.io.PrintWriter;
import java.io.File;
import java.util.Scanner;

//riehl046
//basically taken straight from Lab

public class ElephantReader {
    public static boolean readElephants(ElephantHerd input, String filename){
        //assumes the Elephant file is in CSV form, with no headers or any non-data lines
        Scanner fileIn;
        try{
            fileIn =  new Scanner(new File(filename));
        }
        catch (Exception e){
            System.out.println("Failed to find File");
            return false;
        }
        while (fileIn.hasNextLine()){
            String data = fileIn.nextLine();
            String[] split = data.split(" ");
            String name = split[0];
            String sAge = split[1];
            String sHeight = split[2];
            double dAge =  Double.parseDouble(sAge);
            int age = (int) dAge;
            double height = Double.parseDouble(sHeight);
            input.add(new Elephant(name,age,height));

        }
        return true;


    }
    public static boolean writeElephants(ElephantHerd input, String filename){
        PrintWriter out;
        try{
            out = new PrintWriter(new File(filename));
        }
        catch (Exception e){
            System.out.println("File not Found");
            return false;
        }
        int max = input.getNext();
        // I could just call the .toString() method here, but it prints all on one line, it still works as though
        //they were on separate lines, but this looks cleaner.
        for (int count = 0; count < max; count++){
            out.println(input.getElephants()[count].toString());
        }
        out.close();
        return true;

    }
    //This worked successfuly for me
    public static void main(String[] args){
        ElephantHerd test = new ElephantHerd();
        if (readElephants(test,"src/test.txt")) {
            test.sort();
            writeElephants(test,"src/testOut.txt");
        }
        System.out.println(test.toString());
    }
}
