#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Load the dataset
dataset_path = r"C:\Users\SANTANU\Downloads\archive (11)\SingerAndSongs.csv"
spotify_data = pd.read_csv(dataset_path)

# Display the first few rows to get an overview
spotify_data.head(50)


# In[7]:


# Check columns and data types
spotify_data.info()

# Summary statistics
spotify_data.describe()

# Unique values in categorical columns
spotify_data['tempo'].unique()


# In[13]:


spotify_data.describe


# In[16]:


# Check for missing values
spotify_data.isnull().sum()

# Remove duplicates
spotify_data.drop_duplicates(inplace=True)



# In[21]:


# Count of songs by each artist
artist_counts = spotify_data['Singer'].value_counts()

# Plot the top N artists
import matplotlib.pyplot as plt

top_artists = artist_counts.head(10)
top_artists.plot(kind='barh', figsize=(10, 6), color='red')
plt.title('Top 10 Artists in the Dataset')
plt.xlabel('Number of Songs')
plt.ylabel('Artist')
plt.show()


# In[23]:


# Distribution of danceability
plt.figure(figsize=(8, 5))
plt.hist(spotify_data['danceability'], bins=20, color='lightgreen')
plt.title('Distribution of Danceability')
plt.xlabel('Danceability')
plt.ylabel('Frequency')
plt.show()


# In[24]:


# Count of songs by each artist
artist_counts = spotify_data['Singer'].value_counts()

# Print top 5 artists
top_artists = artist_counts.head(5)
print("Top 5 Artists:\n", top_artists)

# Calculate the percentage of songs by the top artist
percentage_top_artist = (top_artists.iloc[0] / len(spotify_data)) * 100
print(f"\nPercentage of songs by the top artist: {percentage_top_artist:.2f}%")


# In[25]:


# Calculate the average danceability
average_danceability = spotify_data['danceability'].mean()
print(f"\nAverage Danceability: {average_danceability:.2f}")

# Identify highly danceable songs (danceability > 0.8)
highly_danceable_songs = spotify_data[spotify_data['danceability'] > 0.8]
print(f"\nNumber of Highly Danceable Songs: {len(highly_danceable_songs)}")


# In[30]:


import seaborn as sns
# Scatter plot of energy vs. danceability
plt.figure(figsize=(8, 6))
sns.scatterplot(x='energy', y='danceability', data=spotify_data, color='purple')
plt.title('Energy vs. Danceability')
plt.xlabel('Energy')
plt.ylabel('Danceability')
plt.show()


# In[44]:


# Specify the singer's name
singer_name = "Atif Aslam"

# Find the list of songs by the specified singer
songs_by_singer = spotify_data[spotify_data['Singer'] == singer_name]

# Display the list of songs by the singer
if not songs_by_singer.empty:
    print(f"Songs by {singer_name}:\n")
    print(songs_by_singer[['Song name']])
else:
    print(f"No songs found for {singer_name}. Please check the spelling or try another singer.")
    
   



# In[52]:


def search_singer(singer_name, spotify_data):
    # Find the list of songs by the specified singer
    songs_by_singer = spotify_data[spotify_data['Singer'] == singer_name]
    
    # Display the list of songs by the singer
    if not songs_by_singer.empty:
        print(f"Songs by {singer_name}:\n")
        for index, song in songs_by_singer.iterrows():
            print(f"{song['Song name']} - {song['id']}")
    else:
        print(f"No songs found for {singer_name}. Please check the spelling or try another singer.")

# Example usage:
searched_singer = "Alka Yagnik"  # Replace with the singer you want to search
search_singer(searched_singer, spotify_data)


# In[ ]:




