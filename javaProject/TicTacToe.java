/**
Author: Rahul Prajapati
Date Modified: 03/24/2019
Class: TicTacToe.java
 */

import java.util.*;
public class TicTacToe{


	public static Scanner sc = new Scanner(System.in);
	final static private String CROSS = "X";
	final static private String ZERO = "O";

	/*Main method*/
	public static void main(String args[]){

		//Print welcome message
		printWelcomeMessage();
		
		int gameChoice =  getGameOption();
		letsBeginMessage(gameChoice);
		
		playGame(gameChoice);
		

	}//End main method

	/*
	* Get a vaild input from user to place move in the board
	* @args board - current state of the board and 
	*		player - player which playing current move
	* @returns {@code true}if move is sucessfully played
	*/
	public static boolean playerMove(Board board, String player) {
		int position = -1;
		boolean flag = false;
		while(true){

			try {
				System.out.println(player + " --> Select the available position: ");
				position = Integer.parseInt(sc.nextLine());

				if(position <= 9 && position >= 0 )
					break;
				else 
					System.out.println("Invalid position!!!!");
			}catch(Exception e ) {
				System.out.println("Invalid position!!!!");
			}
		}
			
			if(board.editBoardMove(position, player) == true) 
				return true;
			else 
				return false;
		}
	
		/*
		*	Start game by intializing the board and check for winning in each move and give attempt
		*   to player to place their move
		* 	@return null
		*/
		public static String playGame(int gameOption) {

			String player1 = CROSS;
			String player2 = ZERO;

			//Initialize Board
			Board board  = new Board();
			board.printBoardState();

			while( board.checkWinning() == null ) {

				boolean player1Done = false, player2Done  = false;

				while(player1Done != true){
					player1Done = playerMove(board, player1);	
				}

				if(board.checkWinning() != null)
					break;


				while(player2Done != true){
					if(gameOption == 2) {
						board.editBoardMove(board.getRandomMove(), player2);
						player2Done = true;
					}
					else if(gameOption == 1)
						player2Done = playerMove(board, player2);
				}

			}//Complete one game

			System.out.println("Results: " + board.checkWinning());
			return null;
		}

		/* Print lets being message and let know player their move sign */
		public static void letsBeginMessage(int gameChoice){

			System.out.println("\n" + 
					"██╗     ███████╗████████╗███████╗    ██████╗ ███████╗ ██████╗ ██╗███╗   ██╗\n" + 
					"██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔════╝██╔════╝ ██║████╗  ██║\n" + 
					"██║     █████╗     ██║   ███████╗    ██████╔╝█████╗  ██║  ███╗██║██╔██╗ ██║\n" + 
					"██║     ██╔══╝     ██║   ╚════██║    ██╔══██╗██╔══╝  ██║   ██║██║██║╚██╗██║\n" + 
					"███████╗███████╗   ██║   ███████║    ██████╔╝███████╗╚██████╔╝██║██║ ╚████║\n" + 
					"╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝╚═╝  ╚═══╝\n" + 
					"                                                                           \n" + 
					"");
			if(gameChoice == 1) {
				System.out.println("\t\t\tPlayer 1 - X");
				System.out.println("\t\t\tPlayer 2 - O");
			}
			else {
				System.out.println("\t\t\tPlayer - X");
				System.out.println("\t\t\tComputer - O");
			}

		}//End letsBeingMessage()

		/* Print welcome message and game option */
		public static void printWelcomeMessage() {
			System.out.println("\n" + 
					" █     █░▓█████  ██▓     ▄████▄   ▒█████   ███▄ ▄███▓▓█████ \n" + 
					"▓█░ █ ░█░▓█   ▀ ▓██▒    ▒██▀ ▀█  ▒██▒  ██▒▓██▒▀█▀ ██▒▓█   ▀ \n" + 
					"▒█░ █ ░█ ▒███   ▒██░    ▒▓█    ▄ ▒██░  ██▒▓██    ▓██░▒███   \n" + 
					"░█░ █ ░█ ▒▓█  ▄ ▒██░    ▒▓▓▄ ▄██▒▒██   ██░▒██    ▒██ ▒▓█  ▄ \n" + 
					"░░██▒██▓ ░▒████▒░██████▒▒ ▓███▀ ░░ ████▓▒░▒██▒   ░██▒░▒████▒\n" + 
					"░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░▓  ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░░ ▒░ ░\n" + 
					"  ▒ ░ ░   ░ ░  ░░ ░ ▒  ░  ░  ▒     ░ ▒ ▒░ ░  ░      ░ ░ ░  ░\n" + 
					"  ░   ░     ░     ░ ░   ░        ░ ░ ░ ▒  ░      ░      ░   \n" + 
					"    ░       ░  ░    ░  ░░ ░          ░ ░         ░      ░  ░\n" + 
					"                        ░                                   \n" + 
					"");

		}//End printWelcomeMessage()

		/*
		 * Get game option 
		 * 1 vs 1 or 1 v/s Computer
		 * 
		 * @return option selected by the player 
		 * **/
		public static int getGameOption() {
			System.out.println("\t\t1. Player v/s Player ");
			System.out.println("\t\t2. Player v/s Computer ");

			
			int gameChoice = 0;

			while(true){
				try {

					System.out.println("\tChoose one of the game choice( 1 or 2 ):  "); 
					gameChoice = Integer.parseInt(sc.nextLine());

					if(gameChoice == 1 || gameChoice == 2)
						break;
					else
						System.out.println("Please select vaild option!!!");
				}catch(Exception e) {
					System.out.println("Please select vaild option!!!");
				}//End of vaild catch

			}

			return gameChoice;
		}//End getGameOption()

	}//End of Class
