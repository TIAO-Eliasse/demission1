import streamlit as st
import numpy as np
import pandas as pd
from sklearn.utils.validation import check_array

import joblib
st.title("Prédiction de la demission d'un membre du personnel de l'entreprise")
st.subheader("Application réalisé par TIAO ELIASSE")
st.markdown("**Cette application utilise un modèle de machine learning pour prédire la démission d'un employé de l'entreprise**")
# Chargement du modèle
model=joblib.load(filename="final_model.joblib")



#,Heures_supplémentaires
#Définition d'une fonction inférence

Var=['Age', 'DailyRate', 'HourlyRate', 'Revenu_mensuel', 'MonthlyRate',
       'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears',
       'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole',
       'YearsSinceLastPromotion', 'YearsWithCurrManager', 'DistanceFromHome',
       'EnvironmentSatisfaction', 'Implication_dans_emploi', 'JobLevel',
       'Satisfaction_travail', 'StockOptionLevel', 'WorkLifeBalance',
       'Voyage_affaires_Travel_Frequently', 'Voyage_affaires_Travel_Rarely',
       'EducationField_Life Sciences', 'EducationField_Marketing',
       'EducationField_Medical', 'EducationField_Other',
       'EducationField_Technical Degree', 'JobRole_Human Resources',
       'JobRole_Laboratory Technician', 'JobRole_Manager',
       'JobRole_Manufacturing Director', 'JobRole_Research Director',
       'JobRole_Research Scientist', 'JobRole_Sales Executive',
       'JobRole_Sales Representative', 'État_civil_Married',
       'État_civil_Single']

def inférence(Age,DailyRate,HourlyRate,Revenu_mensuel,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,TotalWorkingYears,
              TrainingTimesLastYear,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager,DistanceFromHome,Voyage_affaires, EducationField,JobRole,État_civil,
              EnvironmentSatisfaction, Implication_dans_emploi,JobLevel, Satisfaction_travail, StockOptionLevel,
       WorkLifeBalance):
    data=[[Age,DailyRate,HourlyRate,Revenu_mensuel,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,TotalWorkingYears,
              TrainingTimesLastYear,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager,DistanceFromHome,Voyage_affaires,EducationField,JobRole,État_civil,EnvironmentSatisfaction, Implication_dans_emploi,
       JobLevel, Satisfaction_travail, StockOptionLevel,
       WorkLifeBalance]]
    new_data=pd.DataFrame(data, columns=["Age","DailyRate","HourlyRate","Revenu_mensuel","MonthlyRate","NumCompaniesWorked","PercentSalaryHike","TotalWorkingYears",
              "TrainingTimesLastYear","YearsAtCompany","YearsInCurrentRole","YearsSinceLastPromotion","YearsWithCurrManager","DistanceFromHome","Voyage_affaires","EducationField","JobRole","État_civil",'EnvironmentSatisfaction', 'Implication_dans_emploi',
       'JobLevel', 'Satisfaction_travail', 'StockOptionLevel',
       'WorkLifeBalance'])
    categ=['Voyage_affaires','EducationField','JobRole','État_civil']
    data_final=pd.get_dummies(data=new_data,columns=["Voyage_affaires","EducationField","JobRole","État_civil"])
    for col in Var:
        if col not in data_final.columns:
            data_final[col] =False
    
    data_final=data_final[Var]
    
    df_dummies = data_final
    bool_columns = df_dummies.select_dtypes(include=['bool']).columns
    

# Convertir les colonnes booléennes en entiers
    df_dummies[bool_columns] = df_dummies[bool_columns].astype(int)
    #data_final1 = check_array(df_dummies, dtype=np.float64)

    pred=model.predict(df_dummies)
    #st.write(data_final)

    return pred

#L'utilisateur chaisi une valeur pour chaque caractéristique de l'employé
#Age', 'DailyRate', 'HourlyRate', 'Revenu_mensuel', 'MonthlyRate',
 #      'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears',
 #      'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole',
  #     'YearsSinceLastPromotion', 'YearsWithCurrManager', 'DistanceFromHome'
quant=['Age', 'DailyRate', 'HourlyRate', 'Revenu_mensuel', 'MonthlyRate',
       'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears',
       'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole',
       'YearsSinceLastPromotion', 'YearsWithCurrManager', 'DistanceFromHome',
       'EnvironmentSatisfaction', 'Implication_dans_emploi',
       'JobLevel', 'Satisfaction_travail', 'StockOptionLevel',
       'WorkLifeBalance']

#for col in quant:
   # str(col)=st.number_input(label=str(col), min_value=0)
    
Age=st.number_input(label="age:", min_value=0,value=30)
DailyRate=st.number_input(label="Saisi le DailyRate de l'employé :Son taux horaire:", min_value=0, value=500)
HourlyRate=st.number_input(label="Saisi HourlyRate i.e le montant que l'employé gagne entant que taux horaire",
                           min_value=0, value=100)
EnvironmentSatisfaction=st.number_input(label="EnvironmentSatisfaction", min_value=0)
Implication_dans_emploi=st.number_input(label="Implication_dans_emploi", min_value=0)
JobLevel=st.number_input(label='JobLevel', min_value=0, max_value=5)
Satisfaction_travail=st.number_input(label="Satisfaction_travail", min_value=0, max_value=5)
StockOptionLevel=st.number_input(label="StockOptionLevel", min_value=0, max_value=5)
WorkLifeBalance=st.number_input(label="WorkLifeBalance", min_value=0)
Revenu_mensuel=st.number_input(label="revenu mensuel", min_value=0, value=100)
MonthlyRate=st.number_input(label="MouthlyRate", min_value=0, value=300)
NumCompaniesWorked=st.number_input(label="NumCompagniesWorked", min_value=0, value=5)
PercentSalaryHike=st.number_input(label="PercentSalaryHike", min_value=0, value=5)
TotalWorkingYears=st.number_input(label="TotalWorkingYears", min_value=0, value=17)
TrainingTimesLastYear=st.number_input(label="TrainingTimesLastYear", min_value=0, value=3)
YearsAtCompany=st.number_input(label="YearsAtCompany", min_value=0, value=14)
YearsInCurrentRole=st.number_input(label="YearsInCurrentRole", min_value=0, value=3)
YearsSinceLastPromotion=st.number_input(label="YearsSinceLastPromotion", min_value=0, value=3)
YearsWithCurrManager=st.number_input(label="YearsWithCurrManager", min_value=0, value=3)
DistanceFromHome=st.number_input(label="DistanceFromHome", min_value=0, value=3)

#Voyage_affaires,
  
Voyage_affaires=st.selectbox("Choisi la fréquence à laquelle l'employé voyage", ["Travel_Rarely","Travel_Frequently","Non-Travel"])
#EducationField,EducationField,Jobrole,État_civil,Heures_supplémentaires     
Educa=["Life Sciences","Medical","Marketing","Technical Degree","Other","Human Resources"]
EducationField=st.selectbox("chosisis EducationField", Educa)
#JobRole
Job=["Sales Executive","Research Scientist","Laboratory Technician","Manufacturing Director","Healthcare Representative","Manager",
     "Sales Representative","Research Director","Human Resources"]
JobRole=st.selectbox("chosis le role de votre travail", Job)
#État_civil
Etatcivil=["Married","Single","Divorced"]

État_civil=st.selectbox("choisi le statut matrimonial de l'employé",Etatcivil)
h=["0","1"]
#Heures_supplémentaires=st.selectbox("Choisis 1 si l'employé a des heures supplementaires et 0 sinon",h)



# Création de bouton qui retourne la prédiction du modèle
if st.button("Predict"):
    predictions=inférence(Age,DailyRate,HourlyRate,Revenu_mensuel,MonthlyRate,NumCompaniesWorked,PercentSalaryHike,TotalWorkingYears,
              TrainingTimesLastYear,YearsAtCompany,YearsInCurrentRole,YearsSinceLastPromotion,YearsWithCurrManager,DistanceFromHome,Voyage_affaires, EducationField,JobRole,État_civil,
              EnvironmentSatisfaction, Implication_dans_emploi,JobLevel, Satisfaction_travail, StockOptionLevel,
       WorkLifeBalance)
    st.success(predictions)
