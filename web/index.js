function guessSquare() {
    var input = parseInt(window.prompt("Enter a number", "Enter here"));
    var iteration = parseInt(window.prompt("Enter the number of trial", "Enter here"));
    var c = iteration;
    var message = "Guess its square now in " + iteration +" tries";
    (function receiveAnswer() {
        var input2 = parseInt(window.prompt(message));
        if (input2 == input * input) {
            alert("Good!");
        } else {
            c--;
            if (c === 0) {
                alert("Ran out of attempts!");
            } else {
                message = "Wrong, enter again! " + c + " attempts left!";
                receiveAnswer();
            }
        }
    })();
}