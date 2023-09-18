import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
st.title("RealState REDFIN analyst")
st.markdown("I can provide stats summary for your Data")
st.markdown('### Upload csv file :point_down:')


def additional_bedroom_opportunity(x):
  try:
    # 2bd >= 1300 can usually fit an additional bd
    # 3bd >= 1950 can usually fit an additional bd
    # 4bd >= 2600 can usually fit an additional bd
    if (x['ratio_sqft_bd'] >= 650) and (x['ratio_sqft_bd'] is not None) and (x['BEDS'] > 1) and (x['PROPERTY TYPE'] == 'Single Family Residential'):
      return True
    else:
      return False
  
  except:
    return False


def adu_potential(x):
  try:
    if (x['ratio_lot_sqft'] >= 5) and (x['ratio_lot_sqft'] is not None) and (x['HOA/MONTH'] is not None) and (x['PROPERTY TYPE'] == 'Single Family Residential'):
      return True
    else:
      return False
  except:
    return False


def convert_df(df):
  return df.to_csv(index=False).encode('utf-8')






uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    st.write("Dataframe sample")
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head(10))
    st.write("Dataframe summary")
    st.write(df.describe())
    st.markdown("## Metrics")
    col1,col2,col3,col4=st.columns(4)
    col1.metric("total",len(df),help="Number of properties")
    col2.metric("Avg Price","${:,}".format(df["PRICE"].mean())+"M" ,help="average price of properties")
    col3.metric("Avg Days on market",int(df["DAYS ON MARKET"].mean()),help="average days on market for properties")    
    col4.metric("Avg price per sqft","${:,}".format(int(df["$/SQUARE FEET"].mean())),help="average price per square foot for properties")
        

    st.markdown("## Charts")
    with st.expander("charts"):
        fig=px.histogram(df,x="DAYS ON MARKET",title="days on market chart")
        st.plotly_chart(fig,use_container_width=True)
        fig=px.box(df,x="PRICE",title="price on market box plot")
        st.plotly_chart(fig,use_container_width=True)
        fig=px.histogram(df,x="$/SQUARE FEET")
        st.plotly_chart(fig,use_container_width=True)
    
    st.markdown("## Features")
    df_features = df.copy()
    df_features["ratio_sqft_bd"]=df["SQUARE FEET"]/df_features["BEDS"]
    df_features["addional_bd_opp"]=df_features.apply(lambda x:additional_bedroom_opportunity(x),axis=1)
    df_features["ration_lot_sqft"]=df_features["LOT SIZE"]/df_features["SQUARE FEET"]
    df_features["adu_potential"]=df_features.apply(lambda x:adu_potential(x),axis=1)

    with st.expander("opportunity",expanded=True):
        st.markdown("## opportunity")
        df_add_bd=df_features.loc[df_features["addional_bd_opp"]==True]
        df_adu=df_features.loc[df_features["adu_potential"]==True]
        
        col1,col2=st.columns(2)
        col1.metric("total add bd",len(df_add_bd),help="number of properties with additional bedroom opportunituy")
        col2.metric("total ADU",len(df_adu),help="number of properties with accessory dwelling unit potential")
        st.markdown("## Featurized Dataset")
        st.dataframe(df_features)
        
        
        csv=convert_df(df_features)
        st.download_button("download",csv,"file.csv","text/csv",key="download-csv")