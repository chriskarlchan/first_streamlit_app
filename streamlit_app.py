import streamlit
import pandas
import requests
import snowflake.connector #Reads requirements from a file

streamlit.title('My Parents New Healthy Dinner is Soup')

streamlit.text('Breakfast Menu')
streamlit.text('🥨 Some fresh bread')
streamlit.text('🧀 Some cheese')
streamlit.text('🥓 Crispy bacon')

streamlit.title('🍌🍉Build Your Own Smoothie🍇🍓')

# We want pandas to read our CSV file from that S3 buckett_list. 
# So we use a pandas function called read_csv  to pull the data into a dataframe we'll call my_fruit_list. 

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page
streamlit.dataframe(fruits_to_show)

#New Section to display fruitviceapi response
streamlit.header("Fruityvice Fruit Advice!")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

# Normalize the json code
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())

# output to the screen as a table
streamlit.dataframe(fruityvice_normalized)

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#don't run anything past here while we troubleshoot

#Snowflake code
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("Select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

#Second text entry box

#Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write('Thanks for adding jackfruit ', add_my_fruit)

#this will not work correctly, but just go with it for now
my_cur.execute("insert into fruit_load_list values ('from streamlit')")






