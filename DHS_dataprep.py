#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import geopandas as gpd
import numpy as np


# In[2]:


social = pd.read_csv('DHS_IPUMS_social16.csv')


# In[3]:


envo = gpd.read_file('DHS16.shp')


# In[4]:


dhs16 = envo.merge(social, on='DHSID')


# In[5]:


dhs16


# In[6]:


columns = dhs16.columns
print(columns)
for x in columns:
  print(x)


# In[7]:


dhs16[['HHPHONEHH','MOBPHONE','PC','RADIOHH','TVHH']] = dhs16[['HHPHONEHH','MOBPHONE','PC','RADIOHH','TVHH']].replace({'6':'999','8':'999','9':'999'})


# In[8]:


dhs16[['EDYEARS']] = dhs16[['EDYEARS']].replace({'90':'999','96':'999','97':'999','98':'999','99':'999'})


# In[9]:


dhs16[['WEALTHQHH']] = dhs16[['WEALTHQHH']].replace({'8':'999','9':'999'})


# In[10]:


dhs16 = dhs16[dhs16 != -999.000]
dhs16 = dhs16[dhs16 != -998.000]
dhs16 = dhs16[dhs16 != -997.000]
dhs16 = dhs16[dhs16 != -996.000]
dhs16 = dhs16[dhs16 != -995.000]


# In[11]:


dhs16 = dhs16.dropna()


# In[12]:


dhs16['DHSYEAR'] = dhs16['DHSYEAR'].astype(int)


# In[13]:


dhs16['NDVI_AVG'] = (dhs16['NDVI_60']+dhs16['NDVI_59']+dhs16['NDVI_58']+dhs16['NDVI_57']+dhs16['NDVI_56']+dhs16['NDVI_55']
                     +dhs16['NDVI_54']+dhs16['NDVI_53']+dhs16['NDVI_52']+dhs16['NDVI_51']+dhs16['NDVI_50']+dhs16['NDVI_49']
                     +dhs16['NDVI_48']+dhs16['NDVI_47']+dhs16['NDVI_46']+dhs16['NDVI_45']+dhs16['NDVI_44']+dhs16['NDVI_43']
                     +dhs16['NDVI_42']+dhs16['NDVI_41']+dhs16['NDVI_40']+dhs16['NDVI_39']+dhs16['NDVI_38']+dhs16['NDVI_37']
                     +dhs16['NDVI_36']+dhs16['NDVI_35']+dhs16['NDVI_34']+dhs16['NDVI_33']+dhs16['NDVI_32']+dhs16['NDVI_31']
                     +dhs16['NDVI_30']+dhs16['NDVI_29']+dhs16['NDVI_28']+dhs16['NDVI_27']+dhs16['NDVI_26']+dhs16['NDVI_25']
                     +dhs16['NDVI_24']+dhs16['NDVI_23']+dhs16['NDVI_22']+dhs16['NDVI_21']+dhs16['NDVI_20']+dhs16['NDVI_19']
                     +dhs16['NDVI_18']+dhs16['NDVI_17']+dhs16['NDVI_16']+dhs16['NDVI_15']+dhs16['NDVI_14']+dhs16['NDVI_13']
                     +dhs16['NDVI_12']+dhs16['NDVI_11']+dhs16['NDVI_10']+dhs16['NDVI_09']+dhs16['NDVI_08']+dhs16['NDVI_07']
                     +dhs16['NDVI_06']+dhs16['NDVI_05']+dhs16['NDVI_04']+dhs16['NDVI_03']+dhs16['NDVI_02']+dhs16['NDVI_01']
                     +dhs16['NDVI_00']+dhs16['NDVI_A01']+dhs16['NDVI_A02']+dhs16['NDVI_A03']+dhs16['NDVI_A04']+dhs16['NDVI_A05']
                     +dhs16['NDVI_A06']+dhs16['NDVI_A07']+dhs16['NDVI_A08']+dhs16['NDVI_A09']+dhs16['NDVI_A10']+dhs16['NDVI_A11'])/72


# In[14]:


dhs16['PRECIP_AVG'] = (dhs16['PRECIP_60']+dhs16['PRECIP_59']+dhs16['PRECIP_58']+dhs16['PRECIP_57']+dhs16['PRECIP_56']+dhs16['PRECIP_55']
                     +dhs16['PRECIP_54']+dhs16['PRECIP_53']+dhs16['PRECIP_52']+dhs16['PRECIP_51']+dhs16['PRECIP_50']+dhs16['PRECIP_49']
                     +dhs16['PRECIP_48']+dhs16['PRECIP_47']+dhs16['PRECIP_46']+dhs16['PRECIP_45']+dhs16['PRECIP_44']+dhs16['PRECIP_43']
                     +dhs16['PRECIP_42']+dhs16['PRECIP_41']+dhs16['PRECIP_40']+dhs16['PRECIP_39']+dhs16['PRECIP_38']+dhs16['PRECIP_37']
                     +dhs16['PRECIP_36']+dhs16['PRECIP_35']+dhs16['PRECIP_34']+dhs16['PRECIP_33']+dhs16['PRECIP_32']+dhs16['PRECIP_31']
                     +dhs16['PRECIP_30']+dhs16['PRECIP_29']+dhs16['PRECIP_28']+dhs16['PRECIP_27']+dhs16['PRECIP_26']+dhs16['PRECIP_25']
                     +dhs16['PRECIP_24']+dhs16['PRECIP_23']+dhs16['PRECIP_22']+dhs16['PRECIP_21']+dhs16['PRECIP_20']+dhs16['PRECIP_19']
                     +dhs16['PRECIP_18']+dhs16['PRECIP_17']+dhs16['PRECIP_16']+dhs16['PRECIP_15']+dhs16['PRECIP_14']+dhs16['PRECIP_13']
                     +dhs16['PRECIP_12']+dhs16['PRECIP_11']+dhs16['PRECIP_10']+dhs16['PRECIP_09']+dhs16['PRECIP_08']+dhs16['PRECIP_07']
                     +dhs16['PRECIP_06']+dhs16['PRECIP_05']+dhs16['PRECIP_04']+dhs16['PRECIP_03']+dhs16['PRECIP_02']+dhs16['PRECIP_01']
                     +dhs16['PRECIP_00']+dhs16['PRECIP_A01']+dhs16['PRECIP_A02']+dhs16['PRECIP_A03']+dhs16['PRECIP_A04']+dhs16['PRECIP_A05']
                     +dhs16['PRECIP_A06']+dhs16['PRECIP_A07']+dhs16['PRECIP_A08']+dhs16['PRECIP_A09']+dhs16['PRECIP_A10']+dhs16['PRECIP_A11'])/72


# In[15]:


dhs16['min_TEMP'] = dhs16[['TEMPMIN_60','TEMPMIN_59','TEMPMIN_58','TEMPMIN_57','TEMPMIN_56','TEMPMIN_55','TEMPMIN_54',
                           'TEMPMIN_53','TEMPMIN_52','TEMPMIN_51','TEMPMIN_50','TEMPMIN_49','TEMPMIN_48','TEMPMIN_47',
                           'TEMPMIN_46','TEMPMIN_45','TEMPMIN_44','TEMPMIN_43','TEMPMIN_42','TEMPMIN_41','TEMPMIN_40',
                           'TEMPMIN_39','TEMPMIN_38','TEMPMIN_37','TEMPMIN_36','TEMPMIN_35','TEMPMIN_34','TEMPMIN_33',
                           'TEMPMIN_32','TEMPMIN_31','TEMPMIN_30','TEMPMIN_29','TEMPMIN_28','TEMPMIN_27','TEMPMIN_26',
                           'TEMPMIN_25','TEMPMIN_24','TEMPMIN_23','TEMPMIN_22','TEMPMIN_21','TEMPMIN_20','TEMPMIN_19',
                           'TEMPMIN_18','TEMPMIN_17','TEMPMIN_16','TEMPMIN_15','TEMPMIN_14','TEMPMIN_13','TEMPMIN_12',
                           'TEMPMIN_11','TEMPMIN_10','TEMPMIN_09','TEMPMIN_08','TEMPMIN_07','TEMPMIN_06','TEMPMIN_05',
                           'TEMPMIN_04','TEMPMIN_03','TEMPMIN_02','TEMPMIN_01','TEMPMIN_00','TEMPMIN_A0','TEMPMIN__1',
                           'TEMPMIN__2','TEMPMIN__3','TEMPMIN__4','TEMPMIN__5','TEMPMIN__6','TEMPMIN__7','TEMPMIN__8',
                           'TEMPMIN_A1','TEMPMIN__9']].min(axis=1)


# In[16]:


dhs16['max_TEMP'] = dhs16[['TEMPMAX_60','TEMPMAX_59','TEMPMAX_58','TEMPMAX_57','TEMPMAX_56','TEMPMAX_55','TEMPMAX_54',
                           'TEMPMAX_53','TEMPMAX_52','TEMPMAX_51','TEMPMAX_50','TEMPMAX_49','TEMPMAX_48','TEMPMAX_47',
                           'TEMPMAX_46','TEMPMAX_45','TEMPMAX_44','TEMPMAX_43','TEMPMAX_42','TEMPMAX_41','TEMPMAX_40',
                           'TEMPMAX_39','TEMPMAX_38','TEMPMAX_37','TEMPMAX_36','TEMPMAX_35','TEMPMAX_34','TEMPMAX_33',
                           'TEMPMAX_32','TEMPMAX_31','TEMPMAX_30','TEMPMAX_29','TEMPMAX_28','TEMPMAX_27','TEMPMAX_26',
                           'TEMPMAX_25','TEMPMAX_24','TEMPMAX_23','TEMPMAX_22','TEMPMAX_21','TEMPMAX_20','TEMPMAX_19',
                           'TEMPMAX_18','TEMPMAX_17','TEMPMAX_16','TEMPMAX_15','TEMPMAX_14','TEMPMAX_13','TEMPMAX_12',
                           'TEMPMAX_11','TEMPMAX_10','TEMPMAX_09','TEMPMAX_08','TEMPMAX_07','TEMPMAX_06','TEMPMAX_05',
                           'TEMPMAX_04','TEMPMAX_03','TEMPMAX_02','TEMPMAX_01','TEMPMAX_00','TEMPMAX_A0','TEMPMAX__1',
                           'TEMPMAX__2','TEMPMAX__3','TEMPMAX__4','TEMPMAX__5','TEMPMAX__6','TEMPMAX__7','TEMPMAX__8',
                           'TEMPMAX_A1','TEMPMAX__9']].max(axis=1)


# In[17]:


dhs16['comms'] = dhs16['HHPHONEHH']+dhs16['MOBPHONE']+dhs16['PC']+dhs16['RADIOHH']+dhs16['TVHH']


# In[18]:


dhs16['battle_avg'] = (dhs16['BATTLES_2010']+dhs16['BATTLES_2012']+dhs16['BATTLES_2013']+dhs16['BATTLES_2014']+
                       dhs16['BATTLES_2015']+dhs16['BATTLES_2016']+dhs16['BATTLES_2017']+dhs16['BATTLES_2018'])/8


# In[19]:


dhs16['riot_avg'] = (dhs16['RIOTS_2010']+dhs16['RIOTS_2012']+dhs16['RIOTS_2013']+dhs16['RIOTS_2014']+
                     dhs16['RIOTS_2015']+dhs16['RIOTS_2016']+dhs16['RIOTS_2017']+dhs16['RIOTS_2018'])/8


# In[20]:


dhs16['civ_avg'] = (dhs16['CIV_VIOLENCE_2010']+dhs16['CIV_VIOLENCE_2012']+dhs16['CIV_VIOLENCE_2013']+
                    dhs16['CIV_VIOLENCE_2014']+dhs16['CIV_VIOLENCE_2015']+dhs16['CIV_VIOLENCE_2016']+
                    dhs16['CIV_VIOLENCE_2017']+dhs16['CIV_VIOLENCE_2018'])/8


# In[21]:


dhs16['violence'] = dhs16['battle_avg']+dhs16['riot_avg']+dhs16['civ_avg']


# In[22]:


DHS16_PCA_ready = dhs16[['DHSID','DHSCC','DHSYEAR','DHSCLUST','CCFIPS','ADM1FIPS','ADM1FIPSNA','ADM1SALBNA',
                       'ADM1SALBCO','ADM1DHS','ADM1NAME','DHSREGCO','DHSREGNA','SOURCE','URBAN_RURA',
                       'LATNUM','LONGNUM','ALT_GPS','ALT_DEM','DATUM','SAMPLE_x','SAMPLESTR_x',
                       'COUNTRY_x','YEAR_x','IDHSHID_x','DHSID_1','HHID_x','TIMETOWTRH','POPDENSITY_x',
                       'POPDENSI_1','POPDENSI_2','POPDENSI_3','POPDENSI_4','POPDENSI_5','MALARIA_x',
                       'MALARIA_20','MALARIA_21','MALARIA_22','MALARIA_23','MALARIA_24','MALARIA_25',
                       'MALARIA_26','MALARIA_27','MALARIA_28','MALARIA_29','MALARIA_30','MALARIA_31',
                       'MALARIA_32','MALARIA_33','MALARIA_34','MALARIA_35','NDVI_AVG','PRECIP_AVG',
                       'min_TEMP','max_TEMP','WEALTHQHH','comms','battle_avg','riot_avg','civ_avg','violence',
                       'EDYEARS','geometry']]


# In[23]:


DHS16_PCA_ready.rename(columns= {'SAMPLE_x':'SAMPLE','SAMPLESTR_x':'SAMPLESTR','COUNTRY_x':'COUNTRY',
                                  'YEAR_x':'YEAR','IDHSHID_x':'IDHSHID','DHSID_1':'DHSID',
                                   'POPDENSITY_x':'POPDENSITY','MALARIA_x':'MALARIA','HHID_x':'HHID'})


# In[24]:


DHS16_PCA_ready.head()


# In[25]:


DHS16_PCA_ready['min_TEMP'] = DHS16_PCA_ready['min_TEMP']-273.15


# In[26]:


DHS16_PCA_ready['max_TEMP'] = DHS16_PCA_ready['max_TEMP']-273.15


# In[27]:


DHS16_PCA_ready


# In[28]:


DHS16_PCA_ready.to_file('DHS16_PCA_ready2.shp')


# In[29]:


DHS16_PCA_ready.to_csv('DHS16_PCA_ready2.csv')


# In[ ]:




