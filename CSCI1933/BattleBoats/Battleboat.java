//written by riehl046

public class Battleboat {

    private static Cell[][] theBoard; //thank goodness that Java passes pointers :D
    private static int rowLength;
    private static int colLength;
    private int size;
    private boolean orientation; // false <-> horizontal, true <-> vertical
    private Cell[] spaces;
    private boolean sunk = false;

    // TODO: randomly set the orientation of the boat
    // TODO: set size of the boat (default to 3-cells long)
    // TODO: declare the Cell objects associated with each boat

    public Battleboat(){
        double var = Math.random() * 2;
        var = Math.floor(var);
        if (var == 1) orientation = true;
        else orientation = false;
        size = 3;
        if (orientation) spaces = allocateSpaceVert();
        else spaces = allocateSpaceHoriz();
    }



    // TODO:
    public boolean get_orientation(){
        return orientation;
    }

    // TODO:
    public int get_size(){
        return size;
    }

    // TODO:
    public Cell[] get_spaces(){
        return spaces;
    }
    public static void setRows(int len){
        rowLength = len;
    }
    public static void setCols(int len){
        colLength = len;
    }
    public boolean updateSunk(){
        int numHits = 0;
        for (int count = 0; count < 3; count++){
            if (spaces[count].get_status() == 'H') numHits += 1;
        }
        if (numHits == 3) return true;
        else return false;
    }
    public static void setTheBoard(Cell[][] board){ //gets the board pointer from the Board class
        theBoard = board;
    }
    private Cell[] allocateSpaceHoriz(){ //places the horizontal boats
        Cell[] returnMe = new Cell[3];
        int maxRow = rowLength; //technically this is minus 3, but I'll add one for random so in the end its -2
        int maxCol = colLength - 2;
        boolean done = false;
        while (done == false) {
            double randR = Math.random() * maxRow;
            double randC = Math.random() * maxCol;
            int row = (int) Math.floor(randR);
            int col = (int) Math.floor(randC);
	    System.out.println(row);
            if (theBoard[row][col].get_status() == ' ' && theBoard[row][col+1].get_status() == ' ' && theBoard[row][col+2].get_status() == ' '){
                theBoard[row][col].set_status('B');
                theBoard[row][col+1].set_status('B');
                theBoard[row][col+2].set_status('B');
                returnMe[0] = theBoard[row][col];
                returnMe[1] = theBoard[row][col+1];
                returnMe[2] = theBoard[row][col+2];
                done = true;

            }
        }
        return returnMe;
    }
    private Cell[] allocateSpaceVert(){ //places the vertical boats
        Cell[] returnMe = new Cell[3];
        int maxRow = rowLength - 2; //technically this is minus 3, but I'll add one for random so in the end its -2
        int maxCol = colLength;
        boolean done = false;
        while (done == false) {
            double randR = Math.random() * maxRow;
            double randC = Math.random() * maxCol;
            int row = (int) Math.floor(randR);
            int col = (int) Math.floor(randC);
	    System.out.println(col);
            if (theBoard[row][col].get_status() == ' ' && theBoard[row+1][col].get_status() == ' ' && theBoard[row+2][col].get_status() == ' '){
                theBoard[row][col].set_status('B');
                theBoard[row+1][col].set_status('B');
                theBoard[row+2][col].set_status('B');
                returnMe[0] = theBoard[row][col];
                returnMe[1] = theBoard[row+1][col];
                returnMe[2] = theBoard[row+2][col];
                done = true;

            }
        }
        return returnMe;
    }

}