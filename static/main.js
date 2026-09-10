document.addEventListener("DOMContentLoaded", () => {
    const container = document.querySelector(".emoji-bg");
    if (!container) return;

    const totalEmojis = 70; // number of floating emojis
    const emojis = ["🐶","🐱","🐾"]; // emoji pool

    const containerWidth = container.offsetWidth;
    const containerHeight = container.offsetHeight;

    for (let i = 0; i < totalEmojis; i++) {
        const emoji = document.createElement("span");
        emoji.className = "emoji";

        // pick a random emoji from the array
        emoji.innerText = emojis[Math.floor(Math.random() * emojis.length)];

        // random size
        const size = 1 + Math.random() * 2.5; // 1rem to 3.5rem
        emoji.style.fontSize = size + "rem";

        // starting position within container, accounting for size
        const pxSize = size * 16; // approximate px
        emoji.style.left = Math.random() * (containerWidth - pxSize) + "px";
        emoji.style.top = Math.random() * (containerHeight - pxSize) + "px";

        // random drift distance
        const moveX = (Math.random() * 150 - 75) + "px"; // smaller drift for smoothness
        const moveY = (Math.random() * 150 - 75) + "px";
        emoji.style.setProperty("--move-x", moveX);
        emoji.style.setProperty("--move-y", moveY);

        // random duration for drifting
        emoji.style.setProperty("--duration", (3 + Math.random() * 4) + "s");

        // no animation delay
        emoji.style.animationDelay = "0s";

        // append emoji
        container.appendChild(emoji);
    }
});
