document.addEventListener('DOMContentLoaded', () => {
    // Form Submission
    const form = document.getElementById('recommendation-form');
    let radarChartInstance = null;
    let barChartInstance = null;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Gather data
        const genres = Array.from(document.querySelectorAll('#genre-checkboxes input:checked')).map(cb => cb.value);
        const mood = document.getElementById('mood').value;
        const activity = document.getElementById('activity').value;

        try {
            const response = await fetch('/api/recommend', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ genres, mood, activity })
            });
            const data = await response.json();
            
            document.getElementById('results-container').classList.remove('hidden');
            renderRecommendations(data.top_songs);
            renderCharts(data.top_songs);
        } catch (error) {
            console.error('Error fetching recommendations:', error);
        }
    });

    function renderRecommendations(songs) {
        const container = document.getElementById('recommendations-list');
        container.innerHTML = '';

        songs.forEach(item => {
            const song = item.song;
            
            // Card
            const card = document.createElement('div');
            card.className = 'song-card';
            card.innerHTML = `
                <h3>🎵 ${song.title}</h3>
                <div class="song-artist">${song.artist}</div>
                <div class="song-stats">
                    <strong>Genres:</strong> ${song.genre.join(', ')}<br>
                    <strong>Aktivitas:</strong> ${(song.activity || []).join(', ')}<br>
                    <strong>Kesesuaian:</strong> ${item.similarity}%
                </div>
                <a href="https://www.youtube.com/watch?v=${song.youtube_id}" target="_blank" rel="noopener noreferrer" class="play-btn">
                    ▶ Putar di YouTube
                </a>
            `;
            container.appendChild(card);
        });
    }

    function renderCharts(songs) {
        const labels = songs.map(s => s.song.title.substring(0, 15) + '...');
        
        // Radar Chart
        const ctxRadar = document.getElementById('radarChart').getContext('2d');
        if (radarChartInstance) radarChartInstance.destroy();
        
        const datasets = songs.map((s, idx) => {
            const colors = [
                'rgba(233, 69, 96, 0.5)',
                'rgba(106, 27, 154, 0.5)',
                'rgba(76, 175, 80, 0.5)',
                'rgba(255, 152, 0, 0.5)',
                'rgba(3, 169, 244, 0.5)'
            ];
            const borderColors = [
                '#e94560', '#6a1b9a', '#4caf50', '#ff9800', '#03a9f4'
            ];
            return {
                label: s.song.title,
                data: s.vector,
                backgroundColor: colors[idx % colors.length],
                borderColor: borderColors[idx % borderColors.length],
                borderWidth: 1
            };
        });

        radarChartInstance = new Chart(ctxRadar, {
            type: 'radar',
            data: {
                labels: ['Energy', 'Danceability', 'Valence', 'Tempo', 'Acousticness'],
                datasets: datasets
            },
            options: {
                scales: {
                    r: {
                        angleLines: { color: 'rgba(255,255,255,0.1)' },
                        grid: { color: 'rgba(255,255,255,0.1)' },
                        pointLabels: { color: '#a0a0b0' },
                        ticks: { display: false }
                    }
                },
                plugins: {
                    legend: { labels: { color: '#fff' } }
                }
            }
        });

        // Bar Chart
        const ctxBar = document.getElementById('barChart').getContext('2d');
        if (barChartInstance) barChartInstance.destroy();

        barChartInstance = new Chart(ctxBar, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Skor Kesesuaian (%)',
                    data: songs.map(s => s.similarity),
                    backgroundColor: '#e94560'
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        grid: { color: 'rgba(255,255,255,0.1)' },
                        ticks: { color: '#a0a0b0' }
                    },
                    x: {
                        grid: { display: false },
                        ticks: { color: '#a0a0b0' }
                    }
                },
                plugins: {
                    legend: { labels: { color: '#fff' } }
                }
            }
        });
    }

    // SmartBeat Chat UI Logic
    const chatBubble = document.getElementById('ag-chat-bubble');
    const chatWindow = document.getElementById('ag-chat-window');
    const closeBtn = document.getElementById('ag-close-btn');
    const sendBtn = document.getElementById('ag-send-btn');
    const chatInput = document.getElementById('ag-input');
    const messagesContainer = document.getElementById('ag-messages');

    chatBubble.addEventListener('click', () => {
        chatBubble.classList.add('hidden');
        chatWindow.classList.remove('hidden');
        chatInput.focus();
    });

    closeBtn.addEventListener('click', () => {
        chatWindow.classList.add('hidden');
        chatBubble.classList.remove('hidden');
    });

    chatInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') handleSend();
    });

    sendBtn.addEventListener('click', handleSend);

    async function handleSend() {
        const text = chatInput.value.trim();
        if (!text) return;
        
        // Add user message
        appendMessage('user', text);
        chatInput.value = '';

        // Add typing indicator
        const typingId = appendTypingIndicator();

        try {
            const response = await fetch('/api/antigravity', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            const data = await response.json();
            
            // Remove typing indicator
            document.getElementById(typingId).remove();
            
            // Wait a small amount for realistic effect
            setTimeout(() => {
                appendSystemMessageWithCards(data.reply, data.songs);
            }, 500);

        } catch (error) {
            console.error('Chat error:', error);
            document.getElementById(typingId).remove();
            appendMessage('system', 'Maaf, lagi ada gangguan di sistem aku nih 😅');
        }
    }

    function appendMessage(sender, text) {
        const row = document.createElement('div');
        row.className = `ag-msg-row ag-${sender}`;
        
        const bubble = document.createElement('div');
        bubble.className = 'ag-bubble-msg';
        bubble.textContent = text;
        
        row.appendChild(bubble);
        messagesContainer.appendChild(row);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function appendSystemMessageWithCards(text, songs) {
        const row = document.createElement('div');
        row.className = 'ag-msg-row ag-system';
        
        const bubble = document.createElement('div');
        bubble.className = 'ag-bubble-msg';
        bubble.textContent = text;
        
        if (songs && songs.length > 0) {
            songs.forEach(song => {
                const card = document.createElement('div');
                card.className = 'ag-mini-card';
                card.innerHTML = `
                    <h4>🎵 ${song.title} - ${song.artist}</h4>
                    <p>⭐ Sim: ${song.similarity}% | ${song.genre.join(', ')}</p>
                    <a href="${song.youtube_url}" target="_blank" rel="noopener noreferrer" class="play-btn" style="padding:0.3rem 0.6rem; font-size:0.75rem;">
                        ▶ Putar di YouTube
                    </a>
                `;
                bubble.appendChild(card);
            });
        }
        
        row.appendChild(bubble);
        messagesContainer.appendChild(row);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    function appendTypingIndicator() {
        const id = 'typing-' + Date.now();
        const row = document.createElement('div');
        row.id = id;
        row.className = 'ag-msg-row ag-system';
        
        const bubble = document.createElement('div');
        bubble.className = 'ag-bubble-msg typing-indicator';
        bubble.innerHTML = `
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        `;
        
        row.appendChild(bubble);
        messagesContainer.appendChild(row);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
        
        return id;
    }
});
