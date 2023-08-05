document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('messages');
    const cursor = document.getElementById('cursor');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');

    function chatbotResponse(message) {
        const response = document.createElement('div');
        response.className = 'message bot';
        response.innerHTML = message;
        messagesContainer.appendChild(response);
        cursor.style.display = 'block';
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function userMessage(message) {
        const userMsg = document.createElement('div');
        userMsg.className = 'message user';
        userMsg.innerHTML = message;
        messagesContainer.appendChild(userMsg);
        cursor.style.display = 'none';
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        userInput.value = '';

        // Send user message to server
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_message: message,
            }),
        })
        .then(response => response.json())
        .then(data => {
            chatbotResponse(data.chatbot_response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    sendButton.addEventListener('click', function() {
        const message = userInput.value.trim();
        if (message !== '') {
            userMessage(message);
        }
    });

    userInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            const message = userInput.value.trim();
            if (message !== '') {
                userMessage(message);
            }
        }
    });

    // userMessage("Hello, Chatbot!");
});
