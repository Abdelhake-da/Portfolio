(function () {
    const typingElement = document.getElementById("typing-text");
    if (!typingElement) return;

    const rawValue = typingElement.getAttribute("value") || "";
    const textList = rawValue.split(",").map(t => t.trim()).filter(t => t.length > 0);

    if (textList.length === 0) return;

    const typingSpeed = 100; // Speed in milliseconds per character
    const pauseBetweenTexts = 2000; // Pause between texts in milliseconds
    let textIndex = 0; // To keep track of which text in the list
    let charIndex = 0; // To keep track of character in current text

    function typeWriter() {
        if (charIndex < textList[textIndex].length) {
            typingElement.textContent += textList[textIndex].charAt(charIndex);
            charIndex++;
            setTimeout(typeWriter, typingSpeed);
        } else {
            setTimeout(() => {
                charIndex = 0;
                textIndex = (textIndex + 1) % textList.length; // Move to the next text, loop back at the end
                typingElement.textContent = ""; // Clear the current text
                typeWriter(); // Start typing the next text
            }, pauseBetweenTexts);
        }
    }

    typeWriter();
})();