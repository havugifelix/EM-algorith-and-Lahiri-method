#!/usr/bin/env python
# coding: utf-8

# # Question 1: Simple Linear Regression Model

# #### Importing dataset and putting them into different categories

# In[2]:


import pandas as pd
data= pd.read_csv("diabetes-data1.csv")
AGE= data["AGE"].values
GENDER= data["Gender"].values
BMI= data["BMI"].values
BP= data["BP"].values


# ### Part1: Parameters estimation
#             
#     - Mean values calculation
#     - B1= sum((x-x_mean)*(y-y_mean))/sum(x-x_mean)
#     - B0= y_mean-b1*x_mean

# In[3]:


# Mean values
bp_mean= BP.mean()
age_mean= AGE.mean()

#bp1= bp-p_mean and age1= = age-age_mean
bp1= BP-bp_mean
age1= AGE-age_mean

#denominator and numerator in B1 formula
product= bp1*age1
age1_sq= age1**2

B1= sum ( product)/sum(age1_sq)
B0 = bp_mean-( B1*age_mean)


# #### part b: Fitting the model

# In[4]:


from matplotlib import pyplot as plt
x= AGE
y= B0 + B1*x

y=B0 + B1*x

fig= plt.figure()
ax= fig.add_axes([0,0,1,1])
ax.plot(x,y,'r',linewidth=3)
ax.set_title(" Simple Linear Regression")
ax.set_xlabel("Age")
ax.set_ylabel("Blood Pressure")

plt.scatter(AGE,BP,c='g',marker='^')
plt.show()


# #### part c: Residual error(E) plot
#      Residual error is equal to the difference between observered data BP and predicted dat Y

# In[5]:


E= BP-y
fig= plt.figure()
ay= fig.add_axes([0,0,1,1])
ay.scatter(y,E,marker="*")
ay.set_title( " Residual Error VS Predicted BP")
ay.set_xlabel(" Predicted Blood Pressure")
ay.set_ylabel(" Residual Error")


# #### Part D: Variance of regression model

# In[6]:


DOF= len(BP)- 2 ## degree of fredom
var_model= sum(E**2)/DOF
print("Model Variance= ",var_model)


# #### Part E : Variance of Regression Parameters
#      Variance of parameter B1 IS given by var(B1)=var(model)=sum(x-x_mean)
#      We assume that our error follow normal distribution

# In[7]:


var_B1= var_model/sum(age1_sq) # age1_sq: (age-age_mean)^2
print("Variance of parameter B1=",var_B1)


# #### Part F: Significance testing
# - t_critical= t(n-2,1-alph/2) =t(440,0.975)
# - from the table, t(440,0.975)~= t(1000,0.975)= 1.962
#      

# In[15]:


from scipy.stats import t
# define probability
p = 0.95
DOF = 440
# retrieve value <= probability
tcritical = t.ppf(p, DOF)

B=0, # 
sig_B1= var_B1**0.5
t_calc=B1/sig_B1
print("tcalc=",t_calc,"\ntcritical=",tcritical)
if(t_calc>tcritical):
    print("Age is a significant risk factor")
else:
    print("Age is not a significant risk factor")


# #### Part G: Confidence interval estimation

# In[9]:


Lower_bound= B1- (t_critical*sig_B1)
Upper_bound= B1+ (t_critical*sig_B1)
print(" 95% of the time B1 is between",Lower_bound, "and",Upper_bound)

