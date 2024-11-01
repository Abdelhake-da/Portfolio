let values = document.getElementById("typing-text").attributes['value'].value;
textList = values.split(",");
const typingSpeed = 100; // Speed in milliseconds per character
const pauseBetweenTexts = 2000; // Pause between texts in milliseconds
let textIndex = 0; // To keep track of which text in the list
let charIndex = 0; // To keep track of character in current text

function typeWriter() {
    if (charIndex < textList[textIndex].length) {
        document.getElementById("typing-text").innerHTML += textList[textIndex].charAt(charIndex);
        charIndex++;
        setTimeout(typeWriter, typingSpeed);
    } else {
        setTimeout(() => {
            charIndex = 0;
            textIndex = (textIndex + 1) % textList.length; // Move to the next text, loop back at the end
            document.getElementById("typing-text").innerHTML = ""; // Clear the current text
            typeWriter(); // Start typing the next text
        }, pauseBetweenTexts);
    }
}

// Start the typing effect when page loads
window.onload = function () {
    typeWriter();
};