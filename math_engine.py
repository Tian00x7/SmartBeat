import math
import numpy as np

def apply_set_theory(selected_genres, songs):
    """
    Groups songs by genre using set operations (union).
    """
    if not selected_genres:
        return songs, {"formula": "A ∪ B = {}", "sets": {}}
    
    
    genre_sets = {}
    for song in songs:
        for genre in song["genre"]:
            if genre not in genre_sets:
                genre_sets[genre] = set()
            genre_sets[genre].add(song["id"])
            
    
    result_set = set()
    sets_info = {}
    for g in selected_genres:
        g_set = genre_sets.get(g, set())
        result_set = result_set.union(g_set)
        sets_info[g] = len(g_set)
        
    filtered_songs = [s for s in songs if s["id"] in result_set]
    
    formula = " ∪ ".join(selected_genres)
    
    return filtered_songs, {
        "formula": f"Union of: {formula}",
        "sets": sets_info,
        "total_union": len(result_set)
    }

def cosine_similarity(vec_a, vec_b):
    """
    Calculates cosine similarity between two vectors.
    """
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)
    
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)

def get_feature_vector(song):
    f = song["features"]
    return [f["energy"], f["danceability"], f["valence"], f["tempo_normalized"], f["acousticness"]]

def evaluate_boolean_logic(song, target_mood):
    """
    Evaluates complex boolean rules:
    is_popular = (play_count > 1B)
    is_recent = (year >= 2020)
    matches_mood = (valence matches target mood)
    """
    play_count_threshold = 1000000000
    is_popular = song["play_count"] > play_count_threshold
    is_recent = song["year"] >= 2020
    
    valence = song["features"]["valence"]
    if target_mood == "Bahagia":
        matches_mood = valence > 0.6
    elif target_mood == "Sedih":
        matches_mood = valence < 0.4
    else: # Netral
        matches_mood = 0.4 <= valence <= 0.6
        
    
    expr1 = is_popular and matches_mood
    expr2 = is_recent and matches_mood and not is_popular
    final_result = expr1 or expr2
    
    return {
        "is_popular": is_popular,
        "is_recent": is_recent,
        "matches_mood": matches_mood,
        "result": final_result
    }

def process_recommendations(songs, selected_genres, target_mood, pref_energy, pref_danceability, activity_pref):
    """
    Orchestrates math concepts for the recommendation pipeline.
    """
    
    filtered_songs, set_info = apply_set_theory(selected_genres, songs)
    if not filtered_songs:
        filtered_songs = songs # Fallback if no genre selected
        
    
    if target_mood == "Bahagia":
        pref_valence = 0.8
    elif target_mood == "Sedih":
        pref_valence = 0.2
    else:
        pref_valence = 0.5
        
    
    P = [pref_energy, pref_danceability, pref_valence, 0.6, 0.3]
    
    
    results = []
    for i, song in enumerate(filtered_songs):
        vec_song = get_feature_vector(song)
        # Cosine similarity for display
        sim = cosine_similarity(P, vec_song)
        
        # 3. BOOLEAN LOGIC
        bool_eval = evaluate_boolean_logic(song, target_mood)
        
        # Activity matching boost
        activity_match = activity_pref.lower() in [a.lower() for a in song.get("activity", [])]
        if activity_match:
            sim += 0.15 # Boost similarity if activity matches explicitly
            
        # Cap similarity at 1.0 (or 100%)
        sim = min(1.0, sim)
        
        results.append({
            "song": song,
            "similarity": round(sim * 100, 1),
            "similarity_raw": sim,
            "vector": vec_song,
            "boolean": bool_eval
        })
        
    # Sort by similarity
    results.sort(key=lambda x: x["similarity_raw"], reverse=True)
    top_results = results[:5]
    
    return {
        "top_songs": top_results
    }
