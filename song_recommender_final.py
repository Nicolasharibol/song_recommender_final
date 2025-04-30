import streamlit as st
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import config 

df = pd.read_csv('/Users/admin/Downloads/project/project_week_11/song_recommender_final /billboard_100.csv') 
audio_features_cluster = pd.read_csv('/Users/admin/Downloads/project/project_week_11/song_recommender_final /audio_features_cluster.csv')  


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=config.client_id,
    client_secret=config.client_secret
))

cluster_labels_mapping = {
    0: "mellow grooves", 1: "acoustic chill", 2: "ambient", 3: "energetic upbeat",
    4: "pop", 5: "party beats", 6: "balanced beats", 7: "soulful sounds",
    8: "smooth", 9: "rock and pop"
}

def get_user_preference():
    options = ["Mellow Grooves", "Acoustic Chill", "Ambient", "Energetic Upbeat", "Pop", 
               "Party Beats", "Balanced Beats", "Soulful Sounds", "Smooth", "Rock and Pop", "Trending Now"]
    return st.selectbox("Select a music type:", options).lower()

def recommend_song(preference, df, audio_features_cluster):
    if preference == "trending now":
        song = df.sample(n=1).iloc[0]
        song_title = song['song']
        song_artist = song['artist']
    else:
        cluster_id = next((cluster_id for cluster_id, label in cluster_labels_mapping.items() if label.lower() == preference), None)
        if cluster_id is not None:
            song_options = audio_features_cluster[audio_features_cluster['cluster_id'] == cluster_id]
            song = song_options.sample(n=1).iloc[0]
            song_title = song['track_name']
            song_artist = song['artists']
        else:
            st.write(f"No songs found for the category '{preference}'.")
            return

    st.write(f"Enjoy the song: \"{song_title}\" by {song_artist}")

    query = f"track:{song_title} artist:{song_artist}"
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track_id = results['tracks']['items'][0]['id']
        st.components.v1.iframe(f"https://open.spotify.com/embed/track/{track_id}", width=320, height=80)
    else:
        st.write("Could not find the track on Spotify.")

def main():
    st.title('Song Recommender System')
    preference = get_user_preference()
    recommend_song(preference, df, audio_features_cluster)

if __name__ == "__main__":
    main()
