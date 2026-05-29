# ============================================================
# MusicMath Recommender — Complete Song Database (60 Lagu)
# Field tambahan: "activity" = kegiatan yang cocok
# Nilai activity: "bekerja", "bersantai", "belajar", "berolahraga"
# ============================================================

songs = [

  # ============================================================
  # BATCH 1 — LAGU AWAL (ID 1–30)
  # ============================================================

  # === POP ===
  {
    "id": 1,
    "title": "Blinding Lights",
    "artist": "The Weeknd",
    "genre": ["Pop", "Synth-pop"],
    "year": 2019,
    "play_count": 4500000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.73,
      "danceability": 0.51,
      "valence": 0.33,
      "tempo_normalized": 0.87,
      "acousticness": 0.00
    },
    "youtube_id": "4NRXx6U8ABQ",
    "spotify_id": "0VjIjW4GlUZAMYd2vXMi3b"
  },
  {
    "id": 2,
    "title": "As It Was",
    "artist": "Harry Styles",
    "genre": ["Pop", "Indie Pop"],
    "year": 2022,
    "play_count": 2800000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.73,
      "danceability": 0.52,
      "valence": 0.66,
      "tempo_normalized": 0.79,
      "acousticness": 0.04
    },
    "youtube_id": "H5v3kku4y6Q",
    "spotify_id": "4Dvkj6JhhA12EX05fT7y2e"
  },
  {
    "id": 3,
    "title": "Anti-Hero",
    "artist": "Taylor Swift",
    "genre": ["Pop", "Indie Pop"],
    "year": 2022,
    "play_count": 3100000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.59,
      "danceability": 0.64,
      "valence": 0.53,
      "tempo_normalized": 0.68,
      "acousticness": 0.08
    },
    "youtube_id": "b1kbLwvqugk",
    "spotify_id": "0V3wPSX9ygBnCm8psDIegu"
  },
  {
    "id": 4,
    "title": "Stay",
    "artist": "The Kid LAROI & Justin Bieber",
    "genre": ["Pop", "Hip-Hop"],
    "year": 2021,
    "play_count": 2700000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.68,
      "danceability": 0.79,
      "valence": 0.50,
      "tempo_normalized": 0.77,
      "acousticness": 0.02
    },
    "youtube_id": "kTJczUoc26U",
    "spotify_id": "5HCyHkniMN6OMUD4KPTfWu"
  },
  {
    "id": 5,
    "title": "Levitating",
    "artist": "Dua Lipa",
    "genre": ["Pop", "Disco"],
    "year": 2020,
    "play_count": 2500000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.78,
      "danceability": 0.82,
      "valence": 0.91,
      "tempo_normalized": 0.75,
      "acousticness": 0.00
    },
    "youtube_id": "TUVcZfQe-Kw",
    "spotify_id": "463CkQjx2Zk1yXoBuierM9"
  },

  # === ROCK ===
  {
    "id": 6,
    "title": "Bohemian Rhapsody",
    "artist": "Queen",
    "genre": ["Rock", "Progressive Rock"],
    "year": 1975,
    "play_count": 2100000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.41,
      "danceability": 0.39,
      "valence": 0.49,
      "tempo_normalized": 0.59,
      "acousticness": 0.15
    },
    "youtube_id": "fJ9rUzIMcZQ",
    "spotify_id": "7tFiyTwD0nx5a1eklYtX2J"
  },
  {
    "id": 7,
    "title": "Hotel California",
    "artist": "Eagles",
    "genre": ["Rock", "Soft Rock"],
    "year": 1977,
    "play_count": 1500000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.44,
      "danceability": 0.36,
      "valence": 0.32,
      "tempo_normalized": 0.56,
      "acousticness": 0.21
    },
    "youtube_id": "BciS5krYL80",
    "spotify_id": "40riOy7x9W7GXjyGp4pjAv"
  },
  {
    "id": 8,
    "title": "Smells Like Teen Spirit",
    "artist": "Nirvana",
    "genre": ["Rock", "Grunge"],
    "year": 1991,
    "play_count": 1300000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.88,
      "danceability": 0.49,
      "valence": 0.43,
      "tempo_normalized": 0.76,
      "acousticness": 0.00
    },
    "youtube_id": "hTWKbfoikeg",
    "spotify_id": "5ghIJDpPoe3CfHMGu71E6T"
  },
  {
    "id": 9,
    "title": "Wonderwall",
    "artist": "Oasis",
    "genre": ["Rock", "Britpop"],
    "year": 1995,
    "play_count": 900000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.45,
      "danceability": 0.40,
      "valence": 0.35,
      "tempo_normalized": 0.58,
      "acousticness": 0.58
    },
    "youtube_id": "bx1Bh8ZvH84",
    "spotify_id": "2ld7fJkJlkRLmXFg8AJnvX"
  },
  {
    "id": 10,
    "title": "Mr. Brightside",
    "artist": "The Killers",
    "genre": ["Rock", "Indie Rock"],
    "year": 2003,
    "play_count": 1100000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.92,
      "danceability": 0.36,
      "valence": 0.24,
      "tempo_normalized": 0.83,
      "acousticness": 0.00
    },
    "youtube_id": "gGdGFtwCNBE",
    "spotify_id": "003vvx7Niy0yvhvHt4a14B"
  },

  # === HIP-HOP / RAP ===
  {
    "id": 11,
    "title": "God's Plan",
    "artist": "Drake",
    "genre": ["Hip-Hop", "Rap"],
    "year": 2018,
    "play_count": 2000000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.45,
      "danceability": 0.75,
      "valence": 0.36,
      "tempo_normalized": 0.66,
      "acousticness": 0.07
    },
    "youtube_id": "xpVfcZ0ZcFM",
    "spotify_id": "6DCZcSspjsKoFjzjrWoCdn"
  },
  {
    "id": 12,
    "title": "HUMBLE.",
    "artist": "Kendrick Lamar",
    "genre": ["Hip-Hop", "Rap"],
    "year": 2017,
    "play_count": 1600000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.62,
      "danceability": 0.90,
      "valence": 0.42,
      "tempo_normalized": 0.73,
      "acousticness": 0.00
    },
    "youtube_id": "tvTRZJ-4EyI",
    "spotify_id": "7KXjTSCq5nL1LoYtL7XAwS"
  },
  {
    "id": 13,
    "title": "Rockstar",
    "artist": "Post Malone ft. 21 Savage",
    "genre": ["Hip-Hop", "Trap"],
    "year": 2017,
    "play_count": 1800000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.55,
      "danceability": 0.79,
      "valence": 0.19,
      "tempo_normalized": 0.64,
      "acousticness": 0.03
    },
    "youtube_id": "UceaB4D0jpo",
    "spotify_id": "1Qrg8KqiBpW07V7PNxwwwL"
  },
  {
    "id": 14,
    "title": "Sicko Mode",
    "artist": "Travis Scott",
    "genre": ["Hip-Hop", "Trap"],
    "year": 2018,
    "play_count": 1700000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.74,
      "danceability": 0.82,
      "valence": 0.21,
      "tempo_normalized": 0.78,
      "acousticness": 0.04
    },
    "youtube_id": "6ONRf7h3Mdk",
    "spotify_id": "2xLMifQCjDGFmkHkpNLD9h"
  },
  {
    "id": 15,
    "title": "Old Town Road",
    "artist": "Lil Nas X",
    "genre": ["Hip-Hop", "Country"],
    "year": 2019,
    "play_count": 2300000000,
    "activity": ["bersantai", "berolahraga"],
    "features": {
      "energy": 0.64,
      "danceability": 0.84,
      "valence": 0.69,
      "tempo_normalized": 0.74,
      "acousticness": 0.11
    },
    "youtube_id": "w2Ov5jzm3j8",
    "spotify_id": "2YpeDb67231RjR0MgVLzsG"
  },

  # === JAZZ ===
  {
    "id": 16,
    "title": "So What",
    "artist": "Miles Davis",
    "genre": ["Jazz", "Modal Jazz"],
    "year": 1959,
    "play_count": 80000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.25,
      "danceability": 0.41,
      "valence": 0.46,
      "tempo_normalized": 0.44,
      "acousticness": 0.97
    },
    "youtube_id": "ylXk1LBvIqU",
    "spotify_id": "7II3PTAiCrTq3HMJG9heGf"
  },
  {
    "id": 17,
    "title": "Take Five",
    "artist": "Dave Brubeck",
    "genre": ["Jazz", "Cool Jazz"],
    "year": 1959,
    "play_count": 95000000,
    "activity": ["belajar", "bekerja"],
    "features": {
      "energy": 0.20,
      "danceability": 0.48,
      "valence": 0.57,
      "tempo_normalized": 0.36,
      "acousticness": 0.98
    },
    "youtube_id": "vmDDOFXSgAs",
    "spotify_id": "1YQWosTIljIvxAgHWTp7KP"
  },
  {
    "id": 18,
    "title": "Fly Me to the Moon",
    "artist": "Frank Sinatra",
    "genre": ["Jazz", "Vocal Jazz"],
    "year": 1964,
    "play_count": 210000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.28,
      "danceability": 0.52,
      "valence": 0.81,
      "tempo_normalized": 0.47,
      "acousticness": 0.94
    },
    "youtube_id": "ZEcqHA7dbwM",
    "spotify_id": "5b2fk5BbQdFY2OTRAQWM3l"
  },
  {
    "id": 19,
    "title": "What a Wonderful World",
    "artist": "Louis Armstrong",
    "genre": ["Jazz", "Pop"],
    "year": 1967,
    "play_count": 180000000,
    "activity": ["bersantai", "belajar"],
    "features": {
      "energy": 0.15,
      "danceability": 0.33,
      "valence": 0.87,
      "tempo_normalized": 0.25,
      "acousticness": 0.96
    },
    "youtube_id": "A3yCcXgbKrE",
    "spotify_id": "29U7stRjqHU6rMiS8BfaI9"
  },
  {
    "id": 20,
    "title": "Autumn Leaves",
    "artist": "Chet Baker",
    "genre": ["Jazz", "Cool Jazz"],
    "year": 1955,
    "play_count": 65000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.17,
      "danceability": 0.35,
      "valence": 0.23,
      "tempo_normalized": 0.32,
      "acousticness": 0.97
    },
    "youtube_id": "r-Z8KuwI7Gc",
    "spotify_id": "4O7fZFRTomFKiMPsNF6Qib"
  },

  # === ELECTRONIC / EDM ===
  {
    "id": 21,
    "title": "Levels",
    "artist": "Avicii",
    "genre": ["Electronic", "Progressive House"],
    "year": 2011,
    "play_count": 1200000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.88,
      "danceability": 0.71,
      "valence": 0.88,
      "tempo_normalized": 0.82,
      "acousticness": 0.00
    },
    "youtube_id": "_ovdm2yX4MA",
    "spotify_id": "4eHbdreAnSOrDDsFfc4Fpm"
  },
  {
    "id": 22,
    "title": "One More Time",
    "artist": "Daft Punk",
    "genre": ["Electronic", "House"],
    "year": 2000,
    "play_count": 950000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.87,
      "danceability": 0.78,
      "valence": 0.95,
      "tempo_normalized": 0.79,
      "acousticness": 0.00
    },
    "youtube_id": "FGBhQbmPwH8",
    "spotify_id": "0DiWol3AO6WpXZgdaF3L0W"
  },
  {
    "id": 23,
    "title": "Titanium",
    "artist": "David Guetta ft. Sia",
    "genre": ["Electronic", "Pop"],
    "year": 2011,
    "play_count": 1400000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.78,
      "danceability": 0.60,
      "valence": 0.46,
      "tempo_normalized": 0.80,
      "acousticness": 0.01
    },
    "youtube_id": "JRfuAukYTKg",
    "spotify_id": "0u5T0lf9Mz52vB6GXQR7cP"
  },
  {
    "id": 24,
    "title": "Animals",
    "artist": "Martin Garrix",
    "genre": ["Electronic", "Big Room House"],
    "year": 2013,
    "play_count": 1100000000,
    "activity": ["berolahraga"],
    "features": {
      "energy": 0.97,
      "danceability": 0.65,
      "valence": 0.60,
      "tempo_normalized": 0.89,
      "acousticness": 0.00
    },
    "youtube_id": "gCYcHz2k5x0",
    "spotify_id": "4mAXAkNNbqj7LGXB7KQVJA"
  },
  {
    "id": 25,
    "title": "Clarity",
    "artist": "Zedd ft. Foxes",
    "genre": ["Electronic", "Electro House"],
    "year": 2012,
    "play_count": 780000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.89,
      "danceability": 0.60,
      "valence": 0.43,
      "tempo_normalized": 0.84,
      "acousticness": 0.01
    },
    "youtube_id": "IxxstCcJlsc",
    "spotify_id": "5GorFaKkSqSMWcHDaFMiFA"
  },

  # === CLASSICAL ===
  {
    "id": 26,
    "title": "Moonlight Sonata",
    "artist": "Ludwig van Beethoven",
    "genre": ["Classical"],
    "year": 1801,
    "play_count": 130000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.06,
      "danceability": 0.19,
      "valence": 0.06,
      "tempo_normalized": 0.21,
      "acousticness": 0.99
    },
    "youtube_id": "4Tr0otuiQuU",
    "spotify_id": "3NiLUzGpl3myNBrXMJTqDN"
  },
  {
    "id": 27,
    "title": "Clair de Lune",
    "artist": "Claude Debussy",
    "genre": ["Classical", "Impressionist"],
    "year": 1905,
    "play_count": 110000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.05,
      "danceability": 0.16,
      "valence": 0.26,
      "tempo_normalized": 0.17,
      "acousticness": 0.99
    },
    "youtube_id": "CvFH_6DNRCY",
    "spotify_id": "2RM4jf1Xa9zPgMGRDiht8O"
  },
  {
    "id": 28,
    "title": "Canon in D",
    "artist": "Johann Pachelbel",
    "genre": ["Classical", "Baroque"],
    "year": 1694,
    "play_count": 200000000,
    "activity": ["belajar", "bekerja"],
    "features": {
      "energy": 0.10,
      "danceability": 0.25,
      "valence": 0.55,
      "tempo_normalized": 0.30,
      "acousticness": 0.99
    },
    "youtube_id": "NlprozGcs98",
    "spotify_id": "3qSJD2hjnZ7YqiMcKIYKlp"
  },
  {
    "id": 29,
    "title": "Symphony No. 9",
    "artist": "Ludwig van Beethoven",
    "genre": ["Classical", "Romantic"],
    "year": 1824,
    "play_count": 75000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.58,
      "danceability": 0.31,
      "valence": 0.75,
      "tempo_normalized": 0.65,
      "acousticness": 0.98
    },
    "youtube_id": "_4IRMYuE1hI",
    "spotify_id": "7AXSWqiVkFPD7tRpG5LFAM"
  },
  {
    "id": 30,
    "title": "The Four Seasons – Spring",
    "artist": "Antonio Vivaldi",
    "genre": ["Classical", "Baroque"],
    "year": 1725,
    "play_count": 95000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.52,
      "danceability": 0.38,
      "valence": 0.82,
      "tempo_normalized": 0.60,
      "acousticness": 0.99
    },
    "youtube_id": "GRxofEmo3HA",
    "spotify_id": "5GhOkNkNbFnJFXJZPkiHWp"
  },

  # ============================================================
  # BATCH 2 — LAGU TAMBAHAN (ID 31–60)
  # ============================================================

  # === POP ===
  {
    "id": 31,
    "title": "Shape of You",
    "artist": "Ed Sheeran",
    "genre": ["Pop"],
    "year": 2017,
    "play_count": 5900000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.65,
      "danceability": 0.83,
      "valence": 0.93,
      "tempo_normalized": 0.67,
      "acousticness": 0.08
    },
    "youtube_id": "JGwWNGJdvx8",
    "spotify_id": "7qiZfU4dY1lWllzX7mPBI3"
  },
  {
    "id": 32,
    "title": "Bad Guy",
    "artist": "Billie Eilish",
    "genre": ["Pop", "Electropop"],
    "year": 2019,
    "play_count": 3200000000,
    "activity": ["bekerja", "bersantai"],
    "features": {
      "energy": 0.43,
      "danceability": 0.70,
      "valence": 0.56,
      "tempo_normalized": 0.60,
      "acousticness": 0.07
    },
    "youtube_id": "DyDfgMOUjCI",
    "spotify_id": "2Fxmhks0live0DHtgx1k8Z"
  },
  {
    "id": 33,
    "title": "Watermelon Sugar",
    "artist": "Harry Styles",
    "genre": ["Pop", "Indie Pop"],
    "year": 2020,
    "play_count": 2100000000,
    "activity": ["bersantai", "berolahraga"],
    "features": {
      "energy": 0.82,
      "danceability": 0.55,
      "valence": 0.96,
      "tempo_normalized": 0.76,
      "acousticness": 0.12
    },
    "youtube_id": "E07s5ZYygMg",
    "spotify_id": "6UelLqGlWMcVH1E5c4H7lY"
  },
  {
    "id": 34,
    "title": "Flowers",
    "artist": "Miley Cyrus",
    "genre": ["Pop"],
    "year": 2023,
    "play_count": 2800000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.71,
      "danceability": 0.76,
      "valence": 0.87,
      "tempo_normalized": 0.72,
      "acousticness": 0.05
    },
    "youtube_id": "G7KNmW9a75Y",
    "spotify_id": "0yLdNVWF3Srea0uzk55zFn"
  },
  {
    "id": 35,
    "title": "Cruel Summer",
    "artist": "Taylor Swift",
    "genre": ["Pop", "Synth-pop"],
    "year": 2019,
    "play_count": 3500000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.70,
      "danceability": 0.55,
      "valence": 0.45,
      "tempo_normalized": 0.81,
      "acousticness": 0.01
    },
    "youtube_id": "ic8j13piAhQ",
    "spotify_id": "1BxfuPKGuaTgP7aM0Bbdwr"
  },

  # === ROCK ===
  {
    "id": 36,
    "title": "Stairway to Heaven",
    "artist": "Led Zeppelin",
    "genre": ["Rock", "Hard Rock"],
    "year": 1971,
    "play_count": 1800000000,
    "activity": ["bersantai", "belajar"],
    "features": {
      "energy": 0.34,
      "danceability": 0.34,
      "valence": 0.23,
      "tempo_normalized": 0.48,
      "acousticness": 0.65
    },
    "youtube_id": "QkF3oxziUI4",
    "spotify_id": "5CQ30WqJwcep0pYcV4AMNc"
  },
  {
    "id": 37,
    "title": "Sweet Child O' Mine",
    "artist": "Guns N' Roses",
    "genre": ["Rock", "Hard Rock"],
    "year": 1987,
    "play_count": 1600000000,
    "activity": ["bekerja", "berolahraga"],
    "features": {
      "energy": 0.84,
      "danceability": 0.43,
      "valence": 0.65,
      "tempo_normalized": 0.63,
      "acousticness": 0.02
    },
    "youtube_id": "1w7OgIMMRc4",
    "spotify_id": "7snQQk1zcKl8gZ92AnueZW"
  },
  {
    "id": 38,
    "title": "Don't Stop Believin'",
    "artist": "Journey",
    "genre": ["Rock", "Arena Rock"],
    "year": 1981,
    "play_count": 1400000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.77,
      "danceability": 0.50,
      "valence": 0.72,
      "tempo_normalized": 0.70,
      "acousticness": 0.04
    },
    "youtube_id": "1k8craCGpgs",
    "spotify_id": "4bHsxqR3GMrXTxEPLuK5ue"
  },
  {
    "id": 39,
    "title": "Creep",
    "artist": "Radiohead",
    "genre": ["Rock", "Alternative"],
    "year": 1992,
    "play_count": 950000000,
    "activity": ["bersantai", "belajar"],
    "features": {
      "energy": 0.52,
      "danceability": 0.29,
      "valence": 0.13,
      "tempo_normalized": 0.56,
      "acousticness": 0.18
    },
    "youtube_id": "XFkzRNyygfk",
    "spotify_id": "70LcF31zb1H0PyJoS1Sx1r"
  },
  {
    "id": 40,
    "title": "Come As You Are",
    "artist": "Nirvana",
    "genre": ["Rock", "Grunge"],
    "year": 1991,
    "play_count": 1100000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.64,
      "danceability": 0.47,
      "valence": 0.38,
      "tempo_normalized": 0.62,
      "acousticness": 0.06
    },
    "youtube_id": "vabnZ9-ex7o",
    "spotify_id": "75JFxkI2RXiU7L9VmCVUsV"
  },

  # === HIP-HOP / RAP ===
  {
    "id": 41,
    "title": "Lose Yourself",
    "artist": "Eminem",
    "genre": ["Hip-Hop", "Rap"],
    "year": 2002,
    "play_count": 2200000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.90,
      "danceability": 0.69,
      "valence": 0.28,
      "tempo_normalized": 0.86,
      "acousticness": 0.01
    },
    "youtube_id": "_Yhyp-_hX2s",
    "spotify_id": "5Z01UMMf7V1o0MzF86s6WJ"
  },
  {
    "id": 42,
    "title": "Hotline Bling",
    "artist": "Drake",
    "genre": ["Hip-Hop", "R&B"],
    "year": 2015,
    "play_count": 1900000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.46,
      "danceability": 0.78,
      "valence": 0.40,
      "tempo_normalized": 0.59,
      "acousticness": 0.09
    },
    "youtube_id": "uxpDa-c-4Mc",
    "spotify_id": "0wwPcA6wtMf6HUMpIRdeP7"
  },
  {
    "id": 43,
    "title": "Money Longer",
    "artist": "Lil Uzi Vert",
    "genre": ["Hip-Hop", "Trap"],
    "year": 2016,
    "play_count": 750000000,
    "activity": ["berolahraga"],
    "features": {
      "energy": 0.77,
      "danceability": 0.84,
      "valence": 0.62,
      "tempo_normalized": 0.74,
      "acousticness": 0.02
    },
    "youtube_id": "3Iu4ByZnMBY",
    "spotify_id": "5HCyHkniMN6OMUD4KPTfWu"
  },
  {
    "id": 44,
    "title": "Mask Off",
    "artist": "Future",
    "genre": ["Hip-Hop", "Trap"],
    "year": 2017,
    "play_count": 1100000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.57,
      "danceability": 0.77,
      "valence": 0.25,
      "tempo_normalized": 0.68,
      "acousticness": 0.03
    },
    "youtube_id": "xvZqHgFz51I",
    "spotify_id": "7E89s8VxR6A0NwPbGzSnpM"
  },
  {
    "id": 45,
    "title": "All Falls Down",
    "artist": "Kanye West",
    "genre": ["Hip-Hop"],
    "year": 2004,
    "play_count": 680000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.62,
      "danceability": 0.65,
      "valence": 0.43,
      "tempo_normalized": 0.71,
      "acousticness": 0.27
    },
    "youtube_id": "8kyWDhB_QeI",
    "spotify_id": "1r5oCkRzAoH28QOjbDJGp5"
  },

  # === JAZZ ===
  {
    "id": 46,
    "title": "Round Midnight",
    "artist": "Thelonious Monk",
    "genre": ["Jazz", "Bebop"],
    "year": 1947,
    "play_count": 45000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.22,
      "danceability": 0.31,
      "valence": 0.14,
      "tempo_normalized": 0.35,
      "acousticness": 0.97
    },
    "youtube_id": "0Rc0vUBJQiA",
    "spotify_id": "2bN5A3F0HqyBhJm1vHBNbH"
  },
  {
    "id": 47,
    "title": "My Favorite Things",
    "artist": "John Coltrane",
    "genre": ["Jazz", "Modal Jazz"],
    "year": 1961,
    "play_count": 60000000,
    "activity": ["belajar", "bekerja"],
    "features": {
      "energy": 0.41,
      "danceability": 0.44,
      "valence": 0.47,
      "tempo_normalized": 0.55,
      "acousticness": 0.95
    },
    "youtube_id": "qWG2dsXV5HI",
    "spotify_id": "2TZrzHalY1bBBRpwDfcNBH"
  },
  {
    "id": 48,
    "title": "Girl from Ipanema",
    "artist": "Stan Getz & João Gilberto",
    "genre": ["Jazz", "Bossa Nova"],
    "year": 1964,
    "play_count": 120000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.26,
      "danceability": 0.58,
      "valence": 0.71,
      "tempo_normalized": 0.42,
      "acousticness": 0.93
    },
    "youtube_id": "UJkxFhFer0s",
    "spotify_id": "3bHBuFnKbUGcFsAB3N7fBX"
  },
  {
    "id": 49,
    "title": "Summertime",
    "artist": "Ella Fitzgerald & Louis Armstrong",
    "genre": ["Jazz", "Blues"],
    "year": 1957,
    "play_count": 85000000,
    "activity": ["bersantai", "belajar"],
    "features": {
      "energy": 0.18,
      "danceability": 0.37,
      "valence": 0.28,
      "tempo_normalized": 0.28,
      "acousticness": 0.96
    },
    "youtube_id": "Wt8tHfioxME",
    "spotify_id": "1Fyd4UxFGbKTGsYzfNbDpV"
  },
  {
    "id": 50,
    "title": "Blue in Green",
    "artist": "Miles Davis",
    "genre": ["Jazz", "Cool Jazz"],
    "year": 1959,
    "play_count": 55000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.14,
      "danceability": 0.26,
      "valence": 0.11,
      "tempo_normalized": 0.22,
      "acousticness": 0.98
    },
    "youtube_id": "PvKtSWpb4cg",
    "spotify_id": "1h0LmtqHoJ8UuKmFGnqKIG"
  },

  # === ELECTRONIC / EDM ===
  {
    "id": 51,
    "title": "Strobe",
    "artist": "deadmau5",
    "genre": ["Electronic", "Progressive House"],
    "year": 2009,
    "play_count": 320000000,
    "activity": ["bekerja", "belajar"],
    "features": {
      "energy": 0.59,
      "danceability": 0.52,
      "valence": 0.22,
      "tempo_normalized": 0.65,
      "acousticness": 0.01
    },
    "youtube_id": "tKi9Z-f6qX4",
    "spotify_id": "5BgMeNkPiKKR87lBNlF39c"
  },
  {
    "id": 52,
    "title": "Sandstorm",
    "artist": "Darude",
    "genre": ["Electronic", "Trance"],
    "year": 1999,
    "play_count": 450000000,
    "activity": ["berolahraga"],
    "features": {
      "energy": 0.95,
      "danceability": 0.68,
      "valence": 0.79,
      "tempo_normalized": 0.93,
      "acousticness": 0.00
    },
    "youtube_id": "y6120QOlsfU",
    "spotify_id": "4m2880jivSbbyEGAKfITCa"
  },
  {
    "id": 53,
    "title": "Midnight City",
    "artist": "M83",
    "genre": ["Electronic", "Synth-pop"],
    "year": 2011,
    "play_count": 380000000,
    "activity": ["bekerja", "bersantai"],
    "features": {
      "energy": 0.72,
      "danceability": 0.56,
      "valence": 0.64,
      "tempo_normalized": 0.79,
      "acousticness": 0.03
    },
    "youtube_id": "dX3k_QDnzHE",
    "spotify_id": "5LyRpMTnzGPbMRhAqKCNyA"
  },
  {
    "id": 54,
    "title": "Pursuit of Happiness",
    "artist": "Kid Cudi",
    "genre": ["Electronic", "Hip-Hop"],
    "year": 2009,
    "play_count": 410000000,
    "activity": ["bersantai", "berolahraga"],
    "features": {
      "energy": 0.68,
      "danceability": 0.62,
      "valence": 0.37,
      "tempo_normalized": 0.73,
      "acousticness": 0.04
    },
    "youtube_id": "fBQMmjw1h_c",
    "spotify_id": "6p7V3BPmxQzN5FgFxpDZ5j"
  },
  {
    "id": 55,
    "title": "Wake Me Up",
    "artist": "Avicii",
    "genre": ["Electronic", "Folk EDM"],
    "year": 2013,
    "play_count": 1900000000,
    "activity": ["berolahraga", "bekerja"],
    "features": {
      "energy": 0.78,
      "danceability": 0.64,
      "valence": 0.62,
      "tempo_normalized": 0.83,
      "acousticness": 0.11
    },
    "youtube_id": "IcrbM1l_BoI",
    "spotify_id": "0nJW01T7XtvILxQgC5J7Wh"
  },

  # === CLASSICAL ===
  {
    "id": 56,
    "title": "Nocturne Op. 9 No. 2",
    "artist": "Frédéric Chopin",
    "genre": ["Classical", "Romantic"],
    "year": 1832,
    "play_count": 90000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.07,
      "danceability": 0.22,
      "valence": 0.19,
      "tempo_normalized": 0.18,
      "acousticness": 0.99
    },
    "youtube_id": "9E6b3swbnWg",
    "spotify_id": "6J7biCCQjWUMxGGVT52fFH"
  },
  {
    "id": 57,
    "title": "Für Elise",
    "artist": "Ludwig van Beethoven",
    "genre": ["Classical"],
    "year": 1810,
    "play_count": 150000000,
    "activity": ["belajar", "bersantai"],
    "features": {
      "energy": 0.12,
      "danceability": 0.28,
      "valence": 0.33,
      "tempo_normalized": 0.45,
      "acousticness": 0.99
    },
    "youtube_id": "sS1G1CiVers",
    "spotify_id": "3GN2d0pBzllLHFkEqkfbFb"
  },
  {
    "id": 58,
    "title": "Ave Maria",
    "artist": "Franz Schubert",
    "genre": ["Classical", "Romantic"],
    "year": 1825,
    "play_count": 75000000,
    "activity": ["bersantai", "belajar"],
    "features": {
      "energy": 0.09,
      "danceability": 0.18,
      "valence": 0.39,
      "tempo_normalized": 0.20,
      "acousticness": 0.99
    },
    "youtube_id": "HsOVYCE5OA0",
    "spotify_id": "7GMCJaKlOgkNh4kWnTAzQ1"
  },

  # === R&B / SOUL ===
  {
    "id": 59,
    "title": "Superstition",
    "artist": "Stevie Wonder",
    "genre": ["R&B", "Soul", "Funk"],
    "year": 1972,
    "play_count": 310000000,
    "activity": ["berolahraga", "bersantai"],
    "features": {
      "energy": 0.86,
      "danceability": 0.82,
      "valence": 0.79,
      "tempo_normalized": 0.80,
      "acousticness": 0.05
    },
    "youtube_id": "0CFuCYNx-1g",
    "spotify_id": "1h0LmtqHoJ8UuKmFGnqK0H"
  },
  {
    "id": 60,
    "title": "Killing Me Softly",
    "artist": "Fugees",
    "genre": ["R&B", "Hip-Hop", "Soul"],
    "year": 1996,
    "play_count": 480000000,
    "activity": ["bersantai", "bekerja"],
    "features": {
      "energy": 0.44,
      "danceability": 0.71,
      "valence": 0.48,
      "tempo_normalized": 0.57,
      "acousticness": 0.16
    },
    "youtube_id": "8NVZY-lHXeI",
    "spotify_id": "7FhcVG26TeT8tAzn8pGPMG"
  }
]
