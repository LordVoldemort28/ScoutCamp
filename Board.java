public class Board{

    private String board[];
    final private String EMPTY_MOVE = " ";

    public Board(){
        resetBoard();
    }

    public void resetBoard(){
        this.board = new String[9];
        for(int i=0; i<board.length; i++){
            board[i] = EMPTY_MOVE;
        }
    }

    public void printBoardState(){
        System.out.println("|---|---|---|");
		System.out.println("| " + board[0] + " | " + board[1] + " | " + board[2] + " |");
		System.out.println("|-----------|");
		System.out.println("| " + board[3] + " | " + board[4] + " | " + board[5] + " |");
		System.out.println("|-----------|");
		System.out.println("| " + board[6] + " | " + board[7] + " | " + board[8] + " |");
		System.out.println("|---|---|---|");
    }

 
}