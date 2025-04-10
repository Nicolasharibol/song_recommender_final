# 💻 Song Recommender System: 
Welcome to my Song Recommender System—a tool designed to tailor song suggestions based on a blend of your musical preferences, mood, and style. By integrating data from Billboard's Hot 100 through web scraping and an additional set called audio features curated, both datasets are meticulously processed. Audio features curated is organized into clusters such as pop, ambient, acoustic chill, energetic upbeats, mellow grooves, and more. These clusters help in delivering recommendations that align with different moods and music styles.

This Unsupervised Machine Learning project employs standard scaling and K-means clustering to categorize songs, with Silhouette Score evaluation ensuring optimal cluster quality. The system is crafted in a Streamlit app and seamlessly connects with Spotify's API, making it easy to discover your next favorite track.


# 📊 Data Sourcing:
• Billboard's Hot 100: Data obtained through web scraping to identify popular trends.(www.billboard.com/charts/hot-100/)

• Audio Features Dataset: A curated dataset containing detailed audio features for songs.(audio_features_dataset_curated.csv)

# 📐 Preprocessing Steps Applied to "audio features dataset curated":

• Retained 9 features essential for the machine learning project, as other features were deemed unnecessary.

• Applied Standard Scaler in the audio features curated dataset, ensuring each contributes equally to the analysis. 

# 💡 Machine Learning Approach:

• Used K-Means Clustering to group songs into distinct clusters based on audio feature similarities, naming them to reflect varied moods and styles.

• Used Silhouette Score to help evaluate cluster separation, with higher scores indicating clearer or coherent clusters.  

# ⚙️ System Integration:

The application brings together Streamlit and Spotify's API to deliver an engaging song recommendation experience. 

Spotify API's credentials and the client ID, are stored in config.py and secured via .gitignore to prevent exposure. These credentials are essential for running the function and displaying songs through Spotify's embedded player. Visitors to the GitHub repository will need their own Spotify credentials and client ID to operate the app. For assistance in setting up their credentials or running the project, they are welcome to contact me.

1) In Visual Studio Code, I crafted the Streamlit application code that integrates user interaction with song recommendation features. The code allows users to select their musical preferences, which in turn drives personalized song recommendations in real-time. The script was named song_recommender.py, and securely stored within the project's directory.

2) To run song_recommender.py with Streamlit, I opened the terminal on my Mac/Intel system and I simply copied the full path to where the file is stored and pasted it. Once there, I ran the Streamlit command to launch the app. (streamlit run "/Users/admin/Downloads/project/project_week_11/song_recommender_final /song_recommender_final.py")
  
3) Streamlit generated a local link (http://localhost:8501). By opening it in my browser, I easily accessed and interacted with the app, experiencing its features in real-time.


Enjoy! 😎 and Thank you 🫶 .
