document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.getElementById('chat-toggle-btn');
    const closeBtn = document.getElementById('chat-close-btn');
    const widget = document.getElementById('chat-widget');
    const sendBtn = document.getElementById('chat-send-btn');
    const input = document.getElementById('chat-input');
    const messagesContainer = document.getElementById('chat-messages');

    // Toggle Chat
    function toggleChat() {
        widget.classList.toggle('hidden');
    }

    toggleBtn.addEventListener('click', toggleChat);
    closeBtn.addEventListener('click', toggleChat);

    // Send Message
    async function sendMessage() {
        const text = input.value.trim();
        if (!text) return;

        // Add User Message
        addMessage(text, 'user');
        input.value = '';

        // Add Loading Indicator
        const loadingId = addMessage('Thinking...', 'bot', true);

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });

            const data = await response.json();

            // Remove Loading & Add Bot Response
            removeMessage(loadingId);
            addMessage(data.reply || "Error: No reply received.", 'bot');

        } catch (error) {
            removeMessage(loadingId);
            addMessage("Error connecting to the server.", 'bot');
            console.error('Chat Error:', error);
        }
    }

    sendBtn.addEventListener('click', sendMessage);
    input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    // Helper: Add Message to UI
    function addMessage(text, sender, isLoading = false) {
        const div = document.createElement('div');
        div.classList.add('message', sender);
        div.textContent = text;
        if (isLoading) div.id = 'loading-msg';

        messagesContainer.appendChild(div);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        return div.id;
    }

    function removeMessage(id) {
        const el = document.getElementById(id);
        if (el) el.remove();
    }
});
