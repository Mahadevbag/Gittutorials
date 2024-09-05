import pandas as pd
import numpy as np
import streamlit as st

st.title("This is streamlit example of my page")
## display the simple text 

st.write("This is a simple text")

df=pd.DataFrame({
     'First column':[1,2,3,4,5,6],
     'Second Column':[10,20,30,40,50,60]

})
st.write('Here is the data frame  :')

st.write(df)
#create a line chart
chart_data=pd.DataFrame(
    np.random.rand(30,3),columns=['a','b','c']
)

st.line_chart(chart_data)