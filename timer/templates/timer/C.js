document.getElementById('startBtn').addEventListener('click', function() {
    const timeInput = document.getElementById('time').value;
    let time = parseInt(timeInput);

    const timerDisplay = document.getElementById('timerDisplay');
    timerDisplay.classList.add('active');

    // Set the date we're counting down to
    const countDownDate = new Date().getTime() + time * 1000;

    const interval = setInterval(function() {
        // Get the current time
        const now = new Date().getTime();

        // Calculate the remaining time
        const distance = countDownDate - now;

        // Time calculations for days, hours, minutes, and seconds
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        // Display the result in the element with id="timerDisplay"
        timerDisplay.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;

        // If the countdown is finished, display "EXPIRED"
        if (distance < 0) {
            clearInterval(interval);
            timerDisplay.innerHTML = "EXPIRED";
            timerDisplay.classList.remove('active');
            alert("⏰ Time's up! Great job!");
        }
    }, 1000);
});
