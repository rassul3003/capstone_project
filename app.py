import streamlit as st

def app():
    st.title("Elementary School Recommender")
    st.markdown('Welcome to my application. Please enjoy your stay!')
    st.markdown('Input the **housing budget**, **school ranking** and **top preference** in the boxes below.')

    housing = st.number_input('Housing budget:', 0, 10000000, value=500000, step=1000)
    ranking = st.number_input('School ranking:', 0, 10, value=7, step=1)
    preference = st.number_input('Top preference:', 0.0, 0.150, value=0.010, step=0.005)

    data = query_db( housing, ranking, preference)
    if len(data) == 0:
        st.write('Your query returned no results, please try again!')
    else:
        st.write('Thank you!')

if __name__ == '__main__':
    app()
