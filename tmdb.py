import requests

def fetch_poster_url(tmdb_id: int, api_key: str):
    """Return full poster URL or None if not available."""
    try:
        resp = requests.get(
            f"https://api.themoviedb.org/3/movie/{tmdb_id}",
            params={"api_key": api_key},
            timeout=10
        )
        if resp.status_code != 200:
            return None
        data = resp.json()
        path = data.get("poster_path")
        if not path:
            return None
        return f"https://image.tmdb.org/t/p/w342{path}"
    except Exception:
        return None
