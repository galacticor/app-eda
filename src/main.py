import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

@st.cache
def load_random():
    df = pd.DataFrame(
        np.random.rand(100, 5),
        columns=['a', 'b', 'c', 'd', 'e']
    )
    return df

@st.cache
def load_csv(file):
	df = pd.read_csv(file)
	return df


def report(df):
	pr = ProfileReport(df, explorative=True)
	st.header('**Input DataFrame**')
	st.write(df)
	st.write('---')
	st.header('**Pandas Profiling Report**')
	st_profile_report(pr)

def main():
	# Web App Title
	st.markdown('''
	# **The EDA App**

	This is the **EDA App** created in Streamlit using the **pandas-profiling** library.

	---
	''')

	# Upload CSV data
	with st.sidebar.header('1. Upload your CSV data'):
	    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])


	if not uploaded_file:
	    st.info('Awaiting for CSV file to be uploaded.')
	    if st.button('Use Example Dataset'):
	        df = load_random()
	        report(df)
	else:
	    if st.button('Use Uploaded File'):
	        df = load_csv(uploaded_file)
	        report(df)


if __name__ == "__main__":
	main()


