let countdown; 
let paused = false;
let secondsLeft;

function startTimer() {
    const subject = document.getElementById('subject').value;
    let seconds = parseInt(document.getElementById('time').value);

    if (isNaN(seconds) || seconds <= 0) {
        alert('Please enter a valid number of seconds.');
        return;
    }

    document.getElementById('timer').textContent = formatTime(seconds);
    secondsLeft = seconds;

    countdown = setInterval(() => {
        if (!paused && secondsLeft > 0) {
            secondsLeft--;
            document.getElementById('timer').textContent = formatTime(secondsLeft);
        } else if (secondsLeft <= 0) {
            clearInterval(countdown);
            document.getElementById('timer').textContent = "Blast off!";
        }
    }, 1000);
}

function formatTime(seconds) {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
}

function pauseTimer() {
    paused = true;
}

function resumeTimer() {
    paused = false;
}

function stopTimer() {
    clearInterval(countdown);
    document.getElementById('timer').textContent = "Stopped";
}
