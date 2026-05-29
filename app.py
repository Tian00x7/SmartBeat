from flask import Flask, render_template, request, jsonify
from database import songs
from math_engine import process_recommendations
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/recommend', methods=['POST'])
def recommend():
    data = request.json
    selected_genres = data.get('genres', [])
    mood = data.get('mood', 'Netral')
    activity = data.get('activity', 'Bekerja')
    
    # Map activity to target features based on reference logic
    # berolahraga → energy > 0.65 AND tempo > 0.65 (target ~0.8, 0.8)
    # bekerja     → energy 0.40–0.80 AND acousticness < 0.50 (target ~0.6, 0.5)
    # belajar     → energy < 0.45 AND acousticness > 0.50 (target ~0.2, 0.3)
    # bersantai   → valence > 0.40 AND energy < 0.75 (target ~0.4, 0.5)
    
    if activity == 'Olahraga':
        energy = 0.85
        danceability = 0.80
    elif activity == 'Bekerja':
        energy = 0.60
        danceability = 0.50
    elif activity == 'Belajar':
        energy = 0.20
        danceability = 0.30
    else: # Santai
        energy = 0.35
        danceability = 0.45
    
    results = process_recommendations(songs, selected_genres, mood, energy, danceability, activity)
    return jsonify(results)

@app.route('/api/antigravity', methods=['POST'])
def antigravity():
    data = request.json
    message = data.get('message', '').lower()
    
    # 1. Mood Detection
    keywords_sad = {"galau", "sedih", "patah hati", "lonely", "sad", "melancholy"}
    keywords_happy = {"senang", "happy", "hype", "semangat", "upbeat", "party", "energik", "bahagia"}
    keywords_calm = {"santai", "relax", "calm", "fokus", "study", "chill", "kerja", "belajar", "tidur"}
    
    target_mood = "Netral"
    activity_pref = "Bekerja"
    energy_pref = 0.5
    dance_pref = 0.5
    
    if any(word in message for word in keywords_sad):
        target_mood = "Sedih"
        activity_pref = "Santai"
        energy_pref = 0.3
        dance_pref = 0.3
    elif any(word in message for word in keywords_happy):
        target_mood = "Bahagia"
        activity_pref = "Olahraga"
        energy_pref = 0.8
        dance_pref = 0.8
    elif any(word in message for word in keywords_calm):
        target_mood = "Netral"
        activity_pref = "Belajar" if "belajar" in message else "Bekerja"
        energy_pref = 0.3
        dance_pref = 0.4
        
    # 2. Genre Detection
    all_genres = ["pop", "rock", "hip-hop", "jazz", "electronic", "classical", "r&b", "edm"]
    selected_genres = [g for g in all_genres if g in message]
    
    # Fix casing for exact matching in db
    genre_mapping = {
        "pop": "Pop", "rock": "Rock", "hip-hop": "Hip-Hop", "jazz": "Jazz", 
        "electronic": "Electronic", "classical": "Classical", "r&b": "R&B", "edm": "EDM"
    }
    selected_genres_capitalized = [genre_mapping[g] for g in selected_genres]
    
    # Get recommendations based on detected intent
    rec_results = process_recommendations(songs, selected_genres_capitalized, target_mood, energy_pref, dance_pref, activity_pref)
    top_songs = rec_results['top_songs'][:3] # Top 3 for chat
    
    # 3. Generate conversational response
    templates = []
    if target_mood == "Sedih":
        templates = [
            "Hmm, lagi butuh yang chill atau nemenin galau ya 🌧️ Coba dengerin ini:",
            "Ini playlist santai buat nemenin vibe kamu sekarang ☕:",
            "Paham banget rasanya. Nih, lagu-lagu yang cocok buat momen ini:"
        ]
    elif target_mood == "Bahagia":
        templates = [
            "Wih, lagi semangat nih! 🔥 Yuk tambah hype dengan lagu-lagu ini:",
            "Let's go! Ini rekomendasi upbeat spesial buat kamu 🎉:",
            "Gas! Dengerin ini biar makin semangat:"
        ]
    else:
        templates = [
            "Menarik! 🎵 Ini beberapa pilihan keren yang mungkin kamu suka:",
            "Here you go! Coba cek rekomendasi ini:",
            "Sip, ini beberapa lagu yang pas banget buat kamu dengerin sekarang:"
        ]
        
    # Add context if genre was detected
    response_text = random.choice(templates)
    if selected_genres:
        g_str = ", ".join(selected_genres_capitalized)
        response_text = f"Ooh, lagi cari vibe {g_str} ya? 🎧 " + response_text
        
    formatted_songs = []
    for s in top_songs:
        song_data = s['song']
        formatted_songs.append({
            "title": song_data["title"],
            "artist": song_data["artist"],
            "genre": song_data["genre"],
            "similarity": s["similarity"],
            "youtube_id": song_data["youtube_id"],
            "youtube_url": f"https://www.youtube.com/watch?v={song_data['youtube_id']}"
        })
        
    return jsonify({
        "reply": response_text,
        "songs": formatted_songs
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)
