//written by riehl046

public class Cell {
    private int row;
    private int col;
    private char status; // ' ': Empty, 'B': Boat, 'H': Hit; 'M': Miss

    // TODO:
    public char get_status(){
        return status;

    }

    // TODO:
    public void set_status(char c){
        status = c;
    }

    // TODO:
    public Cell(int row, int col, char status){
        this.row = row;
        this.col = col;
        this.status = status;


    }

}