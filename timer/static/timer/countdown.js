// // variables

// let workTittle = document.getElementById('work');
// let breakTittle = document.getElementById('break');

// let workTime = 25;
// let breakTime = 5;

// let seconds = "00"

// // display
// window.onload = () => {
//     document.getElementById('minutes').innerHTML = workTime;
//     document.getElementById('seconds').innerHTML = seconds;

//     workTittle.classList.add('active');
// }

// // start timer
// function start() {
//     // change button
//     document.getElementById('start').style.display = "none";
//     document.getElementById('reset').style.display = "block";

//     // change the time
//     seconds = 59;

//     let workMinutes = workTime - 1;
//     let breakMinutes = breakTime - 1;

//     breakCount = 0;

//     // countdown
//     let timerFunction = () => {
//         //change the display
//         document.getElementById('minutes').innerHTML = workMinutes;
//         document.getElementById('seconds').innerHTML = seconds;

//         // start
//         seconds = seconds - 1;

//         if(seconds === 0) {
//             workMinutes = workMinutes - 1;
//             if(workMinutes === -1 ){
//                 if(breakCount % 2 === 0) {
//                     // start break
//                     workMinutes = breakMinutes;
//                     breakCount++

//                     // change the painel
//                     workTittle.classList.remove('active');
//                     breakTittle.classList.add('active');
//                 }else {
//                     // continue work
//                     workMinutes = workTime;
//                     breakCount++

//                     // change the painel
//                     breakTittle.classList.remove('active');
//                     workTittle.classList.add('active');
//                 }
//             }
//             seconds = 59;
//         }
//     }
//     // start countdown
//     setInterval(timerFunction, 1000); // 1000 = 1s

// }

//Variables
let workTitle = document.getElementById('work');
let breakTitle = document.getElementById('break');

let workTime = 25; // Work time in minutes
let breakTime = 5; // Break time in minutes

let seconds = 0; // Initial seconds
let minutes = workTime; // Initial minutes

let timer; // To hold the timer interval

// Function to format time as "MM:SS"
function formatTime(mins, secs) {
    return `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
}

// Display initial time
window.onload = () => {
    document.getElementById('minutes').innerHTML = workTime;
    document.getElementById('seconds').innerHTML = seconds < 10 ? `0${seconds}` : seconds;

    workTitle.classList.add('active');
}

// Start timer
function start() {
    // Change button visibility
    document.getElementById('start').style.display = "none";
    document.getElementById('reset').style.display = "block";

    // Initialize timer variables
    seconds = 59;
    minutes = workTime - 1;
    let breakCount = 0;

    // Clear any existing timer
    if (timer) {
        clearInterval(timer);
    }

    // Countdown function
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

// Reset timer
function reset() {
    // Clear any existing timer
    if (timer) {
        clearInterval(timer);
    }

    // Reset display and button visibility
    document.getElementById('start').style.display = "block";
    document.getElementById('reset').style.display = "none";
    document.getElementById('minutes').innerHTML = workTime;
    document.getElementById('seconds').innerHTML = "00";
    workTitle.classList.add('active');
    breakTitle.classList.remove('active');
}

// Attach reset function to the reset button
document.getElementById('reset').addEventListener('click', reset);
