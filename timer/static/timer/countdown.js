
let workTitle = document.getElementById('work');
let breakTitle = document.getElementById('break');

let workTime = 25; 
let breakTime = 5; 

let seconds = 0; 
let minutes = workTime;

let timer; 


function formatTime(mins, secs) {
    return `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
}
window.onload = () => {
    document.getElementById('minutes').innerHTML = formatTime(workTime, seconds).split(':')[0];
    document.getElementById('seconds').innerHTML = formatTime(workTime, seconds).split(':')[1];
    workTitle.classList.add('active');
}

function start() {
    document.getElementById('start').style.display = "none";
    document.getElementById('reset').style.display = "block";
    seconds = 59;
    minutes = workTime - 1;
    let breakCount = 0;
    if (timer) {
        clearInterval(timer);
    }

    const timerFunction = () => {
        // Update display
        document.getElementById('minutes').innerHTML = formatTime(minutes, seconds).split(':')[0];
        document.getElementById('seconds').innerHTML = formatTime(minutes, seconds).split(':')[1];

        // Decrement seconds
        seconds--;

        if (seconds < 0) {
            seconds = 59;
            minutes--;

            if (minutes < 0) {
                if (breakCount % 2 === 0) {
                    // Start break
                    minutes = breakTime;
                    breakCount++;
                    workTitle.classList.remove('active');
                    breakTitle.classList.add('active');
                } else {
                    // Continue work
                    minutes = workTime;
                    breakCount++;
                    breakTitle.classList.remove('active');
                    workTitle.classList.add('active');
                }
            }
        }
    };

    // Start the countdown
    timer = setInterval(timerFunction, 1000); // 1000ms = 1s
}
function reset() {
    if (timer) {
        clearInterval(timer);
    }

    document.getElementById('start').style.display = "block";
    document.getElementById('reset').style.display = "none";
    document.getElementById('minutes').innerHTML = workTime;
    document.getElementById('seconds').innerHTML = "00";
    workTitle.classList.add('active');
    breakTitle.classList.remove('active');
}
document.getElementById('reset').addEventListener('click', reset);
