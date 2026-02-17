document.getElementById('chatbotIcon').addEventListener('click', function() {
    const chatPopup = document.getElementById('chatPopup');
    const chatbotIcon = document.getElementById('chatbotIcon');

    if (chatPopup.classList.contains('visible')) {
        chatPopup.classList.remove('visible');
        setTimeout(() => {
            chatPopup.style.display = 'none';
            chatbotIcon.innerHTML = '&#128172;'; // Message icon
            chatbotIcon.classList.remove('rotated');
        }, 300); // Wait for the opacity transition
    } else {
        chatPopup.style.display = 'flex';
        setTimeout(() => chatPopup.classList.add('visible'), 10);
        chatbotIcon.innerHTML = '&times;'; // X icon
        chatbotIcon.classList.add('rotated');
    }
});

document.getElementById('sendBtn').addEventListener('click', function() {
    const userInput = document.getElementById('userInput').value;
    if (userInput) {
        const messageDiv = document.createElement('div');
        messageDiv.textContent = userInput;
        document.getElementById('chatBody').appendChild(messageDiv);
        document.getElementById('userInput').value = '';
    }
});
