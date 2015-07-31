// Tic Tac Toe
var tictactoe = (function() {
  var currentTurn = 'X';
  var gameboard = ["", "", "", "", "", "", "", "", ""];
  var numberOfMoves = 0;

	// Function for updating the gameboard.
  var updateInternalGrid = function(index, value){
		gameboard[index] = value;
	}

  var isValidMove = function(index){
		var item = gameboard[index];
		if (item == "X" || item == "O"){
			return false;
		}else{
			return true;
		}
	}

  var play = function( $square ) {
    // Get the selected div tag.
    var index = +$square.attr( 'tag' );
    
    // Check if that move is possible.
    if (isValidMove(index) ){
    	// Update UI.
    	$square.html (currentTurn);

        numberOfMoves++;
		// Update internal grid for tracking.
    	updateInternalGrid(index, currentTurn);
	    
	    // Check if user won.
	    if (checkIfWon()){
            alert("You won");
            resetGame();
            // Record that computer lost.
            $.ajax({
                    type: "POST",
                    url: "/add_loss",
                    data: {winner: 'AL'},
                    success: function(data) {
                    },
                    error: function(data) {
                        // Please catch me
                    },
                    complete: function(data) {
                       // reset the game.
                    }
                });
	    }

	    // Computer turn.
	    if (currentTurn == "X")
	    {
		    var index_chosen = computer_turn();
		    var sqaure = document.getElementById('grid' + index_chosen);
			sqaure.innerHTML = "O";
			// Check if computer won.
	    	if (checkIfWon()){
	    	    alert ("Computer wins");
                $.ajax({
                    type: "POST",
                    url: "/add_win",
                    data: {winner: 'AL'},
                    success: function(data) {
                    },
                    error: function(data) {
                        // Please catch me
                    },
                    complete: function(data) {
                       // reset the game.

                    }
                });

	            resetGame();
	    	    numberOfMoves++;
	    	}
	    }
    }

    if (numberOfMoves == 9){
        alert('Draw');
        $.ajax({
                type: "POST",
                url: "/add_draw_game",
                data: {},
                success: function(data) {

                },
                error: function(data) {
                    // Please catch me
                },
                complete: function(data) {

                }
            });
        resetGame();
    }
  };


  var resetGame = function(){
    // Reset variables.
    currentTurn = 'X';
	gameboard = ["", "", "", "", "", "", "", "", ""];
	numberOfMoves = 0;
	// Turn divs empty.
	$(".square").each(function(i, square) {
	    $(square).empty();
	});

  };

  // Will check depending on the last turn played.
  var checkIfWon = function(){
  	// 9 possible ways of winning for each. 
  	winningCombination = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
  												[0, 3, 6], [1, 4, 7], [2, 5, 8],
  												[0, 4, 8], [2, 4, 6]
  												];

  	// Check if one of these combinations has occured as x's or o's 
  	for (var i = 0; i < winningCombination.length; i++) {
    		if (gameboard[winningCombination[i][0]] == 'X' && gameboard[winningCombination[i][1]] == "X" && gameboard[winningCombination[i][2]] == "X"){
    			return true;
    		}
    		if (gameboard[winningCombination[i][0]] == 'O' && gameboard[winningCombination[i][1]] == "O" && gameboard[winningCombination[i][2]] == "O"){
    			return true;
    		}
    	
		}
		
		return false;
  };

  // This is the function for computer turn.
  var computer_turn = function(){
       // Get first Unused slot.
       // I know its simple AI.
       var index;
       for (var i = 0; i < gameboard.length; i++){
            // Check if slot is empty
            if (gameboard[i] == ""){
                gameboard[i] = "O";
                index = i;
                break;
            }
       }

       return index;
  }

  return { play: play };

})();

$( document ).ready( function() {
	
	//  Attach an event handler function for one or more events to the selected elements. 
	// In this case board and its children.
  $( '#board' ).on( 'click', '.square', function() {
    tictactoe.play( $(this) );
  });

  $("#reset-button").on('click', function() {
    tictactoe.resetGame();
  });
});
