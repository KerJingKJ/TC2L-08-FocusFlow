// script.js
function changeWallpaper(wallpaper) {
    // Remove default background (image or video)
    document.body.classList.remove('default-bg');
    
    const defaultVideo = document.querySelector('.default-video');
    if (defaultVideo) {
        defaultVideo.style.display = "none";
    }

    // Hide all videos
    const videos = document.querySelectorAll('.background-video');
    videos.forEach(video => video.classList.remove('show'));

    // Show the selected video
    const selectedVideo = document.getElementById(wallpaper + '-video');
    selectedVideo.classList.add('show');
}
