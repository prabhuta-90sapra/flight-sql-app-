import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()

st.sidebar.title('Flights Analytics')

user_option = st.sidebar.selectbox('Menu',['Select One','Check Flights','Analytics'])

if user_option == 'Check Flights':
    st.title('Check Flights')
    col1,col2 = st.columns(2)

    city = db.fetch_city_names()
    with col1:
        source = st.selectbox('Source',sorted(city))
    with col2:
        destination = st.selectbox('Destination',sorted(city))

    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)

elif user_option == 'Analytics':
    airline, frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)

    city, frequency1 = db.busy_airport()
    fig = px.bar(
        x=city,
        y=frequency1
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    date, frequency2 = db.daily_frequency()
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)


else:
    st.title('About the Project -')
    st.markdown("""
    **Welcome to our all- in -one flight insights hub!**
    
    This dashboard presents a comprehensive analysis of flight data — including trends in passenger traffic, route efficiency, airline performance, delays, cancellations, and more.
    Our goal is to help you explore patterns, uncover insights, and make data-driven decisions with ease.
    
    Start analyzing flight operations, discover peak travel times, identify bottlenecks, and monitor key performance indicators — all in one place.
    """)



