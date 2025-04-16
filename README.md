# 💻 Song Recommender System: Unsupervised Machine Lerning Project
Welcome to my Song Recommender System—a tool designed to tailor song suggestions based on a blend of your musical preferences, mood, and style. By integrating data from Billboard's Hot 100 through web scraping and an additional set called "audio_features_curated".

Within "audio_features_curated", songs are grouped into engaging clusters such as pop, ambient, acoustic chill, energetic upbeats, mellow grooves, and more.

Following the creation of a Billboard's Hot 100 DataFrame, a streamlined process is established that allows users to select "trending now" and instantly receive a song recommendation from the curated top 100 list.

Finally, the setup features a function that retrieves song recommendations tailored to user preferences, offering options aligned with selected clusters or the "trending now" list. Crafted within a Streamlit app and seamlessly connected to Spotify's API, the system makes discovering your next favorite track effortless.


# 📊 Data Sourcing:
• Billboard's Hot 100: Data obtained through web scraping to identify popular trends.(www.billboard.com/charts/hot-100/)

• Audio Features Dataset: A curated dataset containing detailed audio features for songs.(audio_features_dataset_curated.csv)

# 📐 Preprocessing Steps Applied to "audio features dataset curated":

• Retained 9 features essential for the machine learning project, as other features were deemed unnecessary.

• Applied Standard Scaler, ensuring each feature contributes equally to the analysis. 

# 💡 Machine Learning Approach:

• Used K-Means Clustering to group songs into distinct clusters based on audio feature similarities, naming them to reflect varied moods and styles.

• Used Silhouette Score to help evaluate cluster separation, with higher scores indicating clearer clusters.

# ⚙️ System Integration:

Spotify API's credentials and the client ID, are stored in config.py and secured via .gitignore to prevent exposure. These credentials are essential for running the function and displaying songs through Spotify's embedded player. Visitors to the GitHub repository will need their own Spotify credentials and client ID to operate the app. For assistance in setting up their credentials or running the project, they are welcome to contact me.

1) After preprocessing the datasets and setting up functions like get_user_preference() and recommend_song(). Next, I transitioned to Visual Studio Code to build the Streamlit application. It integrates everything seamlessly, allowing users to easily obtain personalized song recommendations directly from the app. I saved the script as song_recommender.py in the project's directory.

2) To run song_recommender.py with Streamlit, I opened the terminal on my Mac/Intel system and I simply copied the full path to where the file is stored and pasted it. Once there, I ran the Streamlit command to launch the app. (streamlit run "/Users/admin/Downloads/project/project_week_11/song_recommender_final /song_recommender_final.py")
  
3) Streamlit generated a local link (http://localhost:8501). By opening it in my browser, I easily accessed and interacted with the app, experiencing its features in real-time.

Enjoy! 😎 and Thank you.

![Descriptive Alt Text](/Users/admin/Downloads/project/project_week_11/song_recommender_final /Photos/Image1.jpg)
