let countdown; // to control pause or stop
let paused = false; // means the timer isn't pause
let secondsLeft; // track how many secs left or remainder

function startTimer() { // minta input
    const subject = document.getElementById('subject').value; // get study subject
    let seconds = parseInt(document.getElementById('time').value); // gets num of secs

    if (isNaN(seconds) || seconds <= 0) { // only accepts +ve num from user
        alert('Please enter a valid number of seconds.');
        return;
    }

    document.getElementById('timer').textContent = formatTime(seconds); //formatting
    secondsLeft = seconds;

    countdown = setInterval(() => { // nak start countdownn
        if (!paused && secondsLeft > 0) { // cek kalau bukan pause kena decrease 1
            secondsLeft--;
            document.getElementById('timer').textContent = formatTime(secondsLeft); // cek display
        } else if (secondsLeft <= 0) { // bila dh 0 timer stop 
            clearInterval(countdown); 
            document.getElementById('timer').textContent = "Blast off!";
        }
    }, 1000); // buat loop every 1000 miliseccond = 1 sec 
}

function formatTime(seconds) { // convert
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`; // format

}

function pauseTimer() { // pause countfown
    paused = true;
}

function resumeTimer() { // resume countdown
    paused = false;
}

function stopTimer() { // stop countdown
    clearInterval(countdown);
    document.getElementById('timer').textContent = "Stopped";
}