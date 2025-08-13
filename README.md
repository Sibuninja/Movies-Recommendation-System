# 🎬 Hybrid Movie Recommendation System

A ready-to-run **hybrid recommender** that blends **content-based similarity** with **collaborative filtering (SVD)**. Built with **Streamlit**.

## ✨ Features
- Content-based recommendations using TF‑IDF over movie titles + genres
- Collaborative filtering with Surprise **SVD**
- Adjustable **blend (α)** between content and CF
- Top‑N control and neighbor window tuning
- Optional **TMDB** posters (enter your API key)
- Falls back to **popular movies** when needed

## 🛠️ Quickstart

```bash
# 1) Create & activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

# 2) Install dependencies
pip install -r requirements.txt

# 3) (Optional) Set your TMDB API key
# Windows PowerShell
$env:TMDB_API_KEY="YOUR_KEY"
# macOS/Linux
export TMDB_API_KEY="YOUR_KEY"

# 4) Run
streamlit run app.py
```

On first run, the app auto-downloads MovieLens **latest-small** (~1MB).

## 📂 Project Structure
```
.
├─ app.py
├─ recommender.py
├─ tmdb.py
├─ requirements.txt
└─ README.md
```

## 🧠 How it works

**Content-based**: TF‑IDF on `title + genres` → Cosine similarity between movies.  
**Collaborative**: Train SVD on `ratings.csv` (MovieLens).  
**Hybrid**: `score = α * content_norm + (1−α) * cf_norm`.

- CF uses the selected `userId` from the dataset. If you're in **Guest** mode, CF is skipped and the system relies on content + popularity.
- Posters come from **TMDB** using `tmdbId` found in `links.csv`.

## 🧪 Notes
- SVD is trained on the full MovieLens small dataset for speed. For production, add train/validation splits, early stopping, and model persistence.
- You can replace TF‑IDF with embeddings (e.g., Sentence-Transformers) for richer content signals.
- Cold-start users: blend in popularity or ask for a few seed likes.

## 🚀 Deploy
- **Streamlit Cloud**: Push to GitHub → "New app" → `streamlit run app.py`
- **Render/Heroku**: Same, ensure you add buildpacks and environment var `TMDB_API_KEY` if using posters.

## 📜 License
MIT — do what you love, watch what you love.# Movies-Recommendation-System
