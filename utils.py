
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import f_oneway



def plot_numerical_pies(data, bins=5):
    custom_colors = sns.color_palette("Set2")

    for col in data.select_dtypes(include=['number']).columns:
        # Bin the numerical column into categories
        binned = pd.cut(data[col], bins=bins, labels=[f"Bin {i+1}" for i in range(bins)])
        values = binned.value_counts()
        labels = values.index
        sizes = values.values

        fig, ax = plt.subplots(figsize=(6, 6))
        wedges, texts, autotexts = ax.pie(
            sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            wedgeprops=dict(width=0.5), colors=custom_colors,
            textprops={'fontsize': 10, 'color': 'white', 'weight': 'bold'}
        )
        ax.set_title(f"Distribution of {col}", fontsize=13, fontweight='bold')
        plt.tight_layout()
        plt.show()


def categorical_analysis(col, categorical):
    custom_colors = ["#4caba4", "#6782a8", "#a3c4dc", "#96d1c7", "#d0e1f9", "#7da6bf", "#b0d6d5"]
    
    value_counts = categorical[col].value_counts()
    counts = categorical[col].value_counts()
    labels = counts.index.tolist()
    values = counts.values
    colors = custom_colors[:len(labels)]

    fig, ax = plt.subplots(1, 2, figsize=(16, 5))
    fig.suptitle(col, fontsize=16, fontweight='bold')

    # Donut chart
    wedges, texts, autotexts = ax[0].pie(
        values, labels=labels, autopct='%1.1f%%', startangle=90,
        wedgeprops=dict(width=0.5), colors=colors,
        pctdistance=0.75, textprops={'fontsize': 10, 'color': 'white', 'weight': 'bold'}
    )
    ax[0].set_title('Donut Chart', fontsize=12, fontweight='bold')

    # Bar plot
    sns.countplot(data=categorical, y=col, ax=ax[1], order=labels, palette=colors)
    for i, v in enumerate(value_counts):
        ax[1].text(v + 1, i, str(v), color='black',fontsize=10, va='center')
    sns.despine(ax=ax[1])
    ax[1].set_ylabel('')
    ax[1].set_xlabel('')
    ax[1].set_title('Count Plot', fontsize=12, fontweight='bold')
    ax[1].tick_params(axis='y', labelsize=9)
    

    plt.tight_layout()
    plt.show()


def plot_categorical_data(data , column):
    
    fig,axes = plt.subplots(nrows=1,ncols=3,figsize=(20,5))
    
    sns.countplot(data=data,x=column,palette="Blues_d",ax=axes[0])
    sns.countplot(data=data,x=column,palette="Blues_d",hue="NObeyesdad",ax=axes[1])
    sns.countplot(data=data,x="NObeyesdad",palette="Blues_d",hue=column,ax=axes[2])
    
    for ax in axes:
        ax.tick_params(axis='x', rotation=90)


def plot_numerical_data(data : pd.DataFrame , column : str):
    
    fig,axes = plt.subplots(nrows=1,ncols=4,figsize=(20,5))
    
    sns.histplot(data=data,x=column,palette="Blues_d",ax=axes[0])
    sns.histplot(data=data,x=column,hue="NObeyesdad",ax=axes[1])
    
    sns.boxplot(data=data,x=column,palette="Blues_d",ax=axes[2])
    
    mean = data[[column,"NObeyesdad"]].groupby(by="NObeyesdad").mean().reset_index()
    sns.barplot(data=mean,x="NObeyesdad",y=column,palette="Blues_d",ax=axes[3])
    
    for ax in axes:
        ax.tick_params(axis='x', rotation=90)



def map_data(df, train):
    Gender_map = {'Female': 0, 'Male': 1}
    yes_no_map = {'yes': 1, 'no': 0}
    caec_map = {"no": 0, "Sometimes": 1, "Frequently": 2, "Always": 3}
    calc_map = {"no": 0, "Sometimes": 1, "Frequently": 2}
    mtrans_map = {"Public_Transportation": 0, "Automobile": 1, "Motorbike": 2, "Bike": 3, "Walking": 4}
    target_map = {"Insufficient_Weight": 0, "Normal_Weight": 1, "Overweight_Level_I": 2, "Overweight_Level_II": 3,
                "Obesity_Type_I": 4, "Obesity_Type_II": 5, "Obesity_Type_III": 6}
    
    # Map categorical variables to numerical values
    if train == True:
        df['NObeyesdad'] = df['NObeyesdad'].map(target_map)
    
    df['Gender'] = df['Gender'].map(Gender_map)
    df['family_history'] = df['family_history'].map(yes_no_map)
    df["FAVC"] = df["FAVC"].map(yes_no_map)
    df['CAEC'] = df['CAEC'].map(caec_map)
    df['SMOKE'] = df['SMOKE'].map(yes_no_map)
    df['SCC'] = df['SCC'].map(yes_no_map)
    df['CALC'] = df['CALC'].map(calc_map)
    df['MTRANS'] = df['MTRANS'].map(mtrans_map)
    return df
