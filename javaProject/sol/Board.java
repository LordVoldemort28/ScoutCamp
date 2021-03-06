import java.util.Arrays;
import java.util.Random;

/*
		@author - Rahul Prajapati 
		Date Modified - 04/02/2019
 */

public class Board{

    private String board[];
    final private String CROSS = "X";
    final private String ZERO = "O";
    
    public Board(){
        resetBoard();
    }
    
    /* Reset values of the board */
    public void resetBoard(){
        this.board = new String[9];
        for(int i=0; i<board.length; i++){
            board[i] = Integer.toString(i+1);
        }
    }
    
    /* Print current state of the board */
    public void printBoardState(){
        System.out.println("    |   |   ");
		System.out.println("  " + board[0] + " | " + board[1] + " | " + board[2] + " ");
		System.out.println("--------------");
		System.out.println("  " + board[3] + " | " + board[4] + " | " + board[5] + " ");
		System.out.println("--------------");
		System.out.println("  " + board[6] + " | " + board[7] + " | " + board[8] + " ");
		System.out.println("    |   |   ");
    }
    
    /*
     * Edit vaild move in the board and print after editing
     * 
     * @return {@code true} if move edited
     * */
    public boolean editBoardMove( int position, String player) {
    	
    	for( int i=0; i<board.length; i++) {
    		if(!board[ position - 1 ].equalsIgnoreCase(CROSS) &&
    				!board[ position - 1 ].equalsIgnoreCase(ZERO)  ) {
    			board[ position - 1 ] = player;
    			printBoardState();
    			return true;
    		}
    	}
    	return false;
    }

    /*
     *For each state of the board check if someone is winning or draw and end game 
     *Link used for this method - https://gist.github.com/xaviablaza-zz/3844825
     *@return {@code X} if X wins {@code O} if O wins {@code Draw} if match is draw
     */
    public String checkWinning(){
    	
    	for (int a = 0; a < 8; a++) {
			String line = null;
			switch (a) {
			case 0:
				line = board[0] + board[1] + board[2];
				break;
			case 1:
				line = board[3] + board[4] + board[5];
				break;
			case 2:
				line = board[6] + board[7] + board[8];
				break;
			case 3:
				line = board[0] + board[3] + board[6];
				break;
			case 4:
				line = board[1] + board[4] + board[7];
				break;
			case 5:
				line = board[2] + board[5] + board[8];
				break;
			case 6:
				line = board[0] + board[4] + board[8];
				break;
			case 7:
				line = board[2] + board[4] + board[6];
				break;
			}
			
			if (line.equalsIgnoreCase("XXX")) {
				return "******************* X Wins *********************";
			} else if (line.equalsIgnoreCase("OOO")) {
				return "******************* O Wins *********************";
			}
		}

		for (int a = 0; a < 9; a++) {
			if (Arrays.asList(board).contains(String.valueOf(a+1))) {
				break;
			}
			else if (a == 8) return "***************** Draw *******************";
		}

		return null;
    }
    /*
     * Get the random available move
     * 
     * @return the random move  
     */
    public int getRandomMove(){
    	Random rand = new Random();
    	int randMove = -1;
    	
    	while(true) {
    		randMove = rand.nextInt(10);
    		if(board[randMove] != CROSS || board[randMove] != CROSS ) 
    			return randMove;
    	}
    }
    

 
}