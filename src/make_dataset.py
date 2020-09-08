import numpy as np
import pandas as pd

coral_data = pd.read_csv('../data/raw/CRCP_Coral_Demographic_Survey_USVI_4f08_0ab5_9d84.csv')
coral_data.head()

fish_data = pd.read_csv('../data/raw/CRCP_Reef_Fish_Surveys_USVI_0a61_f090_a5e8.csv')
fish_data.head()

ocean_survey = pd.merge(coral_data, fish_data, on=['admin', 'administration_description', 'strat', 'strat_description'])
ocean_survey.head()
