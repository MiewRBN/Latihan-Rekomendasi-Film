import streamlit as st
import pickle 
import requests

movies = pickle.load(open("list_movies.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movies Recomendation System")
selectvalue=st.selectbox("Select Movie", movies_list)

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

def recommand(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x:x[1])
    recommand_movies=[]
    recommand_poster=[]
    for i in distance[1:11]:
        movies_id=movies.iloc[i[0]].id
        recommand_poster.append(fetch_poster(movies_id))
        recommand_movies.append(movies.iloc[i[0]].title)
    return recommand_movies, recommand_poster

if st.button("Show Recommand"):
    movie_name, movie_poster = recommand(selectvalue)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
        # Baris kedua (5 kolom)
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.text(movie_name[5])
        st.image(movie_poster[5])
    with col7:
        st.text(movie_name[6])
        st.image(movie_poster[6])
    with col8:
        st.text(movie_name[7])
        st.image(movie_poster[7])
    with col9:
        st.text(movie_name[8])
        st.image(movie_poster[8])
    with col10:
        st.text(movie_name[9])
        st.image(movie_poster[9])