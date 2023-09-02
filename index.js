document.addEventListener("DOMContentLoaded", function () {
    const typingText = document.getElementById("typing-text");
    const textToType = `Do you want to start learning the filed of your interset,          but still haven't found the roadmap which suits you best?       We GOT you`; // Text to be typed
    const typingSpeed = 70; // Typing speed in milliseconds
    let charIndex = 0;

    function type() {
        if (charIndex < textToType.length) {
            typingText.textContent += textToType.charAt(charIndex);
            charIndex++;
            setTimeout(type, typingSpeed);
        }
        else {
            // Typing animation is complete, now clear the content
            setTimeout(function () {
                typingText.textContent = "";
            }, 2000);
        }
    }

    // Start the typing animation when the page loads
    type();
});

//defining the function which directs the user to the main page of the quiz when the user presses the button
function directionToRoadmap() {
    window.location.assign("roadmap.htm");
}