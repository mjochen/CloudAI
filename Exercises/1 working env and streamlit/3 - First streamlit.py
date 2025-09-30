# import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# import files
df = pd.read_excel('files/titanic3.xlsx', engine='openpyxl')

# range slide to get the range of ages
values = st.slider(
    'Select a range of values',
    df.age.min(), df.age.max(), (10.0, 75.0))
st.write('Values:', values)

# filter the dataframe, show rows within range
df_filtered = df[(df.age >= values[0]) & (df.age <= values[1])]
st.dataframe(df_filtered)

# show histogram
fig, ax = plt.subplots()

df_filtered.age.plot.hist(bins=20, edgecolor='k', ax=ax)
ax.set_title('Titanic passengers')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig)

# selectbox to filter by embarked
embarked = st.selectbox('Select a value', df_filtered.embarked.unique())
df_filtered = df[df.embarked == embarked]

fig, ax = plt.subplots()

df_filtered.boxplot(column='age', by='pclass', ax=ax)
ax.set_title('Titanic passengers')
ax.set_xlabel('Pclass')
ax.set_ylabel('Age')
st.pyplot(fig)

# run by typing...
# streamlit run '.\3.3 - First streamlit.py'
# in the terminal