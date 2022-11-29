import streamlit
import pandas

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
streamlit.multiselect("Pick Some fruits:", list(my_fruit_list.index))

# Display the table on the page



