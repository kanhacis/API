// function autoRefreshPage() {
//     window.location = window.location.href;
// }
// setInterval('autoRefreshPage()', 10000); 



var isMouseActive = false;
var isKeyPressed = false;
var timeout = '';
// Event listener for mousemove
$(document).on('mousemove', function () {
    isMouseActive = true;
    clearTimeout(timeout);
    // Reset the flag after 5 seconds
    timeout = setTimeout(function () {
        isMouseActive = false;
    }, 5000);
});

// Event listener for keydown
$(document).on('keydown', function () {
    isKeyPressed = true;
    clearTimeout(timeout);

    // Reset the flag after 5 seconds
    timeout = (function () {
        isKeyPressed = false;
    }, 5000);
});

function checkForNewOrders() {
    // Check if the mouse is active or a key is pressed
    if (!isMouseActive && !isKeyPressed) {
        window.location.reload();
    }
}
setInterval(checkForNewOrders, 30000);
