import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
datastudent = pd.read_csv('Student Mental health.csv')


depressionstudent=datastudent["Do you have Depression?"].value_counts().sort_values(ascending=False)
yes_depressionstudent = datastudent[datastudent["Do you have Depression?"]== 'Yes']
no_depressionstudent = datastudent[datastudent["Do you have Depression?"]== 'No']
yes_anxietystudent = datastudent[datastudent["Do you have Anxiety?"]== 'No']
#Setting up of grid space for the plot.

fig  = plt.figure(facecolor='black',figsize=(20,16))
gridplane = plt.GridSpec(4, 4, hspace=0.5, wspace=0.3)
#Grid used for Student ID name and title
axisname = fig.add_subplot(gridplane[0,:])
axisname.text(.5,.5,'Students mental health',ha='center', va='center', fontsize=40, color='orange',weight= 'bold')
# Placement of Student Name And ID
axisname.text(0.2,0,'Student Name: Indira Golla Student ID: 22085312', ha='center', va='bottom', fontsize=20, color='white')
axisname.axis('off')

#plotting Pie chart on the plot.
axpie = fig.add_subplot(gridplane[1,:-2])
axpie.pie(depressionstudent,labels=depressionstudent.index,autopct="%0.2f%%",
          textprops={'color': 'red',"fontsize":19,'weight':'bold'},explode=[0,0.4])
axpie.legend(bbox_to_anchor=(0.5,-0.15),ncol=4)
textpara = {'fontsize': 18, 'color': 'blue', 'fontweight': 'bold'}
boxpara = dict(boxstyle='round', facecolor='grey', alpha=0.30,edgecolor='black')
axpie.set_title('Ratio of students Undergoing depression', fontdict=textpara, bbox=boxpara);

#plotting Pie for genders
genderstudents = datastudent['Choose your gender'].value_counts().sort_values(ascending=False)
axpie2 = fig.add_subplot(gridplane[2,1:2])
axpie2.pie(genderstudents,labels=genderstudents.index,autopct="%0.0f%%",
        textprops={'color': 'red',"fontsize":15,'weight':'bold'},explode=[0,0.4])
axpie2.legend(bbox_to_anchor=(0.5,-0.15),ncol=4)
textpara = {'fontsize': 12, 'color': 'blue', 'fontweight': 'bold'}
boxpara = dict(boxstyle='round', facecolor='grey', alpha=0.30,edgecolor='black')
axpie2.set_title('Gender Group effected by depression', fontdict=textpara, bbox=boxpara);

Genderwithoutdepression =yes_anxietystudent['Choose your gender'].value_counts().sort_values(ascending=False)
axpie3 = fig.add_subplot(gridplane[2,0])
axpie3.pie(Genderwithoutdepression,labels=Genderwithoutdepression.index,autopct="%0.0f%%",
        textprops={'color': 'red',"fontsize":19,'weight':'bold'},explode=[0,0.4])
axpie3.legend(bbox_to_anchor=(0.5,-0.15),ncol=4)
axpie3.set_title('Gender Group effected by Anxiety', fontdict=textpara, bbox=boxpara);

#barplot for age groups with any kind of mental issues
sns.axes_style()
x=datastudent.loc[(datastudent["Do you have Depression?"]=="Yes") | (datastudent["Do you have Anxiety?"]=="Yes") | (datastudent["Do you have Panic attack?"]=="Yes")]
axisbar = fig.add_subplot(gridplane[1,2:])
axisbar =sns.countplot(x="Age",edgecolor="black",data=x)
textpara = {'fontsize': 18, 'color': 'blue', 'fontweight': 'bold'}
boxpara = dict(boxstyle='round', facecolor='grey', alpha=0.30,edgecolor='black')
axisbar.set_title('Age group which are undergoing mental health issues', fontdict=textpara, bbox=boxpara);
for pat in axisbar.patches:
    axisbar.annotate(format(pat.get_height(), '.0f'),
                (pat.get_x() + pat.get_width() / 1.8, pat.get_height()),
                ha = 'center', va = 'center',fontsize=9 ,color='green',fontweight= 'bold',
                xytext = (0,9),
                textcoords = 'offset points')
axisbar.set_xticklabels(axisbar.get_xticklabels(), color='white', fontsize=12)
axisbar.xaxis.label.set_color('white')
axisbar.set_yticks(axisbar.get_yticks())
axisbar.set_yticklabels(axisbar.get_yticklabels(), color='white', fontsize=12)
axisbar.yaxis.label.set_color('white')

def Cleans(Texts):
    Texts = Texts[-1]
    Texts = int(Texts)
    return Texts
datastudent["Your current year of Study"] = datastudent["Your current year of Study"].apply(Cleans)
axvol = fig.add_subplot(gridplane[2,2:])
axvol=sns.violinplot(x = 'Your current year of Study', y = 'Age', data = datastudent,  hue = 'Do you have Anxiety?', palette = ['#72A98F', '#CBEF43'])
axvol.set_title('Student with Anxiety in different years of education', fontdict=textpara, bbox=boxpara);
axvol.set_xticklabels(axvol.get_xticklabels(), color='white', fontsize=15)
axvol.xaxis.label.set_color('white')
axvol.set_yticks(axvol.get_yticks())
axvol.set_yticklabels(axvol.get_yticklabels(), color='white', fontsize=15)
axvol.yaxis.label.set_color('white')
axvol.tick_params(axis='both', which='major', labelsize=12)  

axtext = fig.add_subplot(gridplane[3,:])
text_kwargs = dict(ha='center', va='center', fontsize=14, color='white')
textexplain = 'The mental well-being of students represents a significant concern in contemporary educational settings. The pie chart shows that 34.65% of students reported feeling stressed or \n\
anxious, which is quiet considering the ratio.The pie graphs show that female students are more likely than male students to report having a diagnosed mental health condition.\n\
For example, 76%–74% of female students reported having been diagnosed with depression and anxiety, while only 24% of male students reported the same. From the bar plot, it is\n\
shown that students in the age groups 18–19 and 23–24 are going through mental health issues. This might be because, at the age of 18, students have to choose their career path,\n\
and at the age of 23, students are entering the market.The violin plot shows the distribution of panic attacks by academic year. It appears that panic attacks are more common \n\
among students in their first year of study. Overall, the image suggests that mental health problems are common among students and that female students and students in their\n\
first year of study are particularly at risk.'

axtext.text(.5,.5,textexplain, **text_kwargs)
plt.axis('off')
plt.savefig("22085312.png", format="png", dpi=300)