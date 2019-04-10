//written by riehl046

public class Board {
    private int num_rows;
    private int num_columns;
    private int num_boats;
    private Battleboat[] boats;
    private Cell[][] board;
    private boolean debugMode;


    // TODO: Initialize the board as a 2-D Cell array
    // TODO: Initialize boats as a Battleboat array
    // TODO: Place Battleboats appropriately on board and add them to the board's boats

    public Board(int m , int n, boolean debugMode){
        Battleboat.setRows(m);
        Battleboat.setCols(n);
        num_rows = m;
        num_columns = n;
        num_boats = getBoatNumber(m,n);
        this.debugMode = debugMode;
        board = new Cell[m][n];
        fillBoard(board);
        Battleboat.setTheBoard(board);
        boats = boatSetUp();

    }
    private void fillBoard(Cell[][] gameBoard){ // makes the entire board blank
        int row = gameBoard.length;
        int col = gameBoard[0].length;
        for (int r = 0; r < row; r++){
            for (int c = 0; c < col; c++){
                gameBoard[r][c] = new Cell(r,c,' ');
            }
        }
    }

    private int getBoatNumber(int row, int col){ //sets the correct number of boats
        int product = row * col;
        int returnMe;
        if (product == 9) returnMe = 1;
        else if (product > 9 && product < 26) returnMe = 2;
        else if (product > 25 && product < 50) returnMe = 3;
        else if (product > 49 && product < 81) returnMe = 4;
        else returnMe = 6;

        return returnMe;
    }
    //Obscures a character if the game is not being played in debug mode
    private char debug(boolean debugMode, char c){
        if(debugMode){
            return c;
        }
        else{
            switch(c){
                case 'H':
                    c = 'H';
                    break;
                case 'M':
                    c = 'M';
                    break;
                default:
                    c = ' ';
                    break;
            }
            return c;
        }
    }

    //Prints a Board object in a way that makes sense to the player
    public String toString(){

        String boardString = "\t";
        for (int j = 0; j < num_columns-1; j++){
            boardString += j + " |" + "\t";
        }

        boardString += num_columns-1;

        for(int i = 0; i < num_rows; i++){
            boardString+= "\n" + i + "\t";
            for (int j = 0; j < num_columns; j++){
                boardString += debug(debugMode, board[i][j].get_status()) + "\t";
            }
        }

        boardString += "\n";
        return boardString;
    }

    // TODO: Return a int based on the guess for the cell/its status
    // TODO: Change the statuses of the cell if applicable
    public int guess(int r, int c){
        if (r >= num_rows || c >= num_columns || r < 0 || c < 0){
            return 0;
            //"Penalty: Out of Bounds";
        }
        else if (board[r][c].get_status() == ' ') {
            board[r][c].set_status('M');
            return 1;
            //"Miss";
        }
        else if(board[r][c].get_status() == 'B'){
            board[r][c].set_status('H');
            return 2;
            //"Hit";
        }
        else {
            return 3;
            //"Penalty: Redundant Guess";
        }
    }

    //TODO: write a function that calculates the number of unsunk boats
    public int unsunkBoats(){
        int notSunk = num_boats;
        for (int count =0; count < num_boats; count++){
            if (boats[count].updateSunk()){
                notSunk -= 1;

            }
        }
        return notSunk;
    }
    public int getNum_rows(){
        return num_rows;
    }
    public int getNum_columns(){
        return num_columns;
    }
    private Battleboat[] boatSetUp(){ //makes correct number of battleboats for the arena
        Battleboat[] returnMe = new Battleboat[num_boats];
        for (int count = 0; count < num_boats; count++){
            returnMe[count] = new Battleboat();
        }
        return returnMe;

    }
}
