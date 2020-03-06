#!/usr/bin/env python
# coding: utf-8

# In[115]:


# ........................................ Q3(a)..........................................................................


# fist of all we will import our data
import pandas as pd
df= pd.read_csv("accidents-crashes.csv")

#X Value were were given values from 1 to 8 and y, y=1 and y=2
x=[1, 2,  3,  4,  5, 6, 7, 8]
y= [0, 1]

# extract data for joint probability calculation
val_xy0=df["Alcoholic impaired crashes"].values 
val_xy1= df["Non-alcoholic impared crashes"].values

# Joint probablity calculation 
val_total= sum(val_xy0)+sum(val_xy1)

def joint_prb_calculation(xy, total_outcome):
     
        pxy=xy/total_outcome
        return pxy
pxy0= joint_prb_calculation(val_xy0, val_total) # joint prob along the first column
pxy1=joint_prb_calculation(val_xy1, val_total) # joint prob along the second column

# marginal probability calculation( Probality of X and Y)
def prob_x(p_xy0, p_xy1):
    pxi= p_xy0[:]+p_xy1[:]
    return pxi
px_i=prob_x(pxy0,pxy1)

def prob_y(py0xi, py1xi):
    pyi=[sum(py0xi),sum(py1xi)]
    return pyi
py_i= prob_y(pxy0,pxy1)


# In[116]:



# Conditional Probablities calculation
def cond_prob(pxyi, pyi):         # pxyyi = px/yi, pyi=py(y=i)
    p_xyi=pxyi/pyi
    return p_xyi
px_y0= cond_prob(pxy0, py_i[0] )
px_y1= cond_prob(pxy1, py_i[1] )

def cond_py_xi(pxiy0,pxiy1, pxi ):  # pxiyo= pxy(xi,yo=), pxiy1=pxy(xi,y=1)
    py_xi=[pxiy0/pxi, pxiy1/pxi]
    return py_xi


# Conditional probability py/xi
pyx1= cond_py_xi(pxy0[0], pxy1[0],px_i[0])
print(pyx1)
py_x1= cond_py_xi(pxy0[0], pxy1[0],px_i[0])
py_x2= cond_py_xi(pxy0[1], pxy1[1],px_i[1])
py_x3 =cond_py_xi(pxy0[2], pxy1[2],px_i[2])
py_x4= cond_py_xi(pxy0[3], pxy1[3],px_i[3])
py_x5 =cond_py_xi(pxy0[4], pxy1[4],px_i[4])
py_x6 =cond_py_xi(pxy0[5], pxy1[5],px_i[5])
py_x7 =cond_py_xi(pxy0[6], pxy1[6],px_i[6])
py_x8 =cond_py_xi(pxy0[7], pxy1[7],px_i[7])
       


# In[117]:


#..............Expectations calculations......................................................#

def exp_calculation(x_value, p):
    exp=0
    for i in range(0, len(x_value)):
#                    exp= x_value[i]*p[i]
                   exp+= (x_value[i]*p[i])
    return  exp
EXP_X= exp_calculation(x, px_i)
EXP_Y= exp_calculation(y, py_i)
print ("E[X]=", EXP_X)
print ("E[Y] =", EXP_Y)

#xpectation of EX/Yi

EXPX_Y0= exp_calculation(x, px_y0)
EXPX_Y1 = exp_calculation(x, px_y1)
print ("E[X/Y0] =",EXPX_Y0, "\nE[X/Y1] =",EXPX_Y1 )

# Expextation of E[Y/Xi]

EXPY_X1= exp_calculation(y, py_x1)
EXPY_X2= exp_calculation(y, py_x2)
EXPY_X3=exp_calculation(y, py_x3)
EXPY_X4=exp_calculation(y, py_x4)
EXPY_X5=exp_calculation(y, py_x5)
EXPY_X6=exp_calculation(y, py_x6)
EXPY_X7=exp_calculation(y, py_x7)
EXPY_X8=exp_calculation(y, py_x8)

print ("E[Y\X1]=",EXPY_X1, "\nE[Y\X2]=",EXPY_X2,"\nE[Y\X3]=",EXPY_X3, "\nE[Y\X4]=",EXPY_X4 , 
       "\nE[Y\X5]=",EXPY_X5,"\nE[Y\X6]=",EXPY_X6, "\nE[Y\X7]=",EXPY_X7, "\nE[Y\X8]=",EXPY_X8 )

## Variance 
x_sq=[1, 4,9,16, 25, 36, 49, 64]
y_sqr=[0, 1]

def var_calculation(val_sqr, prb, val_avg):
    var_val= (exp_calculation(val_sqr, prb))- val_avg**2
    return  var_val
var_x= var_calculation(x_sq,px_i, EXP_X )
var_y= var_calculation(y_sqr,py_i, EXP_Y )
print("var[x]=",var_x, "\nvar[y]=", var_y)

## Conditional variance calculation 

## var[x/Y=j]= E[X^2/Y=J] - (E[X/Y])^2=== var calculation wit parameters x^2, px/y, E[X/Y]
varx_y0= var_calculation(x_sq,px_y0, EXPX_Y0 )## var[X/Y=0]
varx_y1= var_calculation(x_sq,px_y1, EXPX_Y1 )
print("\nCondition Variance VAR[x/y]")
print("var[x/y=0]= ",varx_y0, "\nvar[x/y=1]= ", varx_y1 )

## var[y/x=i]= E[y^2/x=i] - (E[y/x])^2

vary_x1= var_calculation(y_sqr,py_x1, EXPY_X1 )
vary_x2=var_calculation(y_sqr,py_x2, EXPY_X2 )
vary_x3=var_calculation(y_sqr,py_x3, EXPY_X3 )
vary_x4=var_calculation(y_sqr,py_x4, EXPY_X4 )
vary_x5=var_calculation(y_sqr,py_x5, EXPY_X5 )
vary_x6=var_calculation(y_sqr,py_x6, EXPY_X6 )
vary_x7=var_calculation(y_sqr,py_x7, EXPY_X7 )
vary_x8= var_calculation(y_sqr,py_x8, EXPY_X8 )
print("\nCondition Variance VAR[Y/X]")
print("\nvar[y/x1]=", vary_x1, "\nvar[y/x2]=", vary_x2,"\nvar[y/x3]=", vary_x3,"\nvar[y/x4]=", vary_x4,"\nvar[y/x5]=",
      vary_x5,"\nvar[y/x6]=",vary_x6,"\nvar[y/x7]=", vary_x7, "\nvar[y/x8]=", vary_x8)

## Covariance calculation
# COV(X,Y)= EXP[XY]- E[X]E[Y]
XY =[0,0,0,0,0,0,0,0,1,2,3,4,5,6,7,8]
PXY=[0.047487854, 0.041859225, 0.082000237, 0.088636094, 0.114942529, 0.126466406, 0.107714184, 0.078208319,
   0.085407039, 0.040318758, 0.013864202,0.008679938,0.014101197,0.031283327, 0.050539163, 0.068491527 ]
ex_ey= EXP_X*EXP_Y 

COV_XY= exp_calculation(XY, PXY)-ex_ey
print("\ncovariance COV[X,Y]")
print("cov[x,y]=",COV_XY)
# correlation corr= cov(x,y)/(stdx*stdy)
stdx= (var_x)**0.5
stdy= (var_y)**0.5
corr_xy= COV_XY/(stdx*stdy)
print("\ncorrelation coefficient")
print("corr(x,y)=",corr_xy)


# In[118]:


##----------------------------------------------------------------------------------------------------#
##---------------------------------------Q3.B----------------------------------------------------------#
# from the table we were given joint probability for variables x and y
X= [1,2]
Y= [1,2,3]
#joint probability
p_xy1=[0.2,0.1]
p_xy2=[0.1,0.1]
p_xy3 =[0.3,0.2]
PX=[0.6, 0.4]

PY=[0.333333333,0.166666667,0.5]

# Conditional probabilities
PX_Y1= [0.666666667,0.333333333]
PX_Y2= [0.5, 0.5]
PX_Y3=[0.6,0.4]

PY_X1=[0.333333333,0.166666667,0.5]
PY_X2 =[0.25,0.25, 0.5]
# Expectation calculations
EX=  exp_calculation(X,PX)
EY= exp_calculation(Y, PY)

print ("\n question 3.b")
print("E[X]=",EX, "\nE[Y]=", EY)

# Conditional expectations
EX_Y1=  exp_calculation(X, PX_Y1)
EX_Y2= exp_calculation(X, PX_Y2) 
EX_Y3= exp_calculation(X, PX_Y3)
EY_X1 = exp_calculation(Y, PY_X1)
EY_X2 = exp_calculation(Y, PY_X2)

print("\n conditional expectations")

print( "E[X\Y1]=", EX_Y1, "\nE[X/Y2]=", EX_Y2,"\nE[X/Y3]=", EX_Y3, "\nE[Y/X1]=",EY_X1, "\nE[Y/X2]=",EY_X2)

# VARIANCE CALCULATIONS
X_SQ= [1,4]
Y_SQ=[1, 4, 9]
VAR_X= var_calculation(X_SQ, PX, EX)
VAR_Y= var_calculation(Y_SQ, PY, EY)
print("var[x]=",VAR_X, "\nvar[y]=", VAR_Y)

# conditional variance
VAR_XY1= var_calculation(X_SQ, PX_Y1, EX_Y1)
VAR_XY2= var_calculation(X_SQ, PX_Y2, EX_Y2)
VAR_XY3= var_calculation(X_SQ, PX_Y3, EX_Y3)
VAR_YX1= var_calculation(Y_SQ,PY_X1, EY_X1)
VAR_YX2= var_calculation(Y_SQ, PY_X2, EY_X2)
print("\nvar[x/y1]=", VAR_XY1, "\nvar[x/y2]=",VAR_XY2,"\nvar[x/y3]=",VAR_XY3,"\nvar[y/x1]=", VAR_YX1,"\nvar[y/x2]=",
      VAR_YX2)

# covariance cov[x,y]=E[XY]-EX*EY
XY=[1,2,3,2,4,6]
PXY=[0.2,0.1,0.3,0.1,0.1,0.2] 
E_XY= EX*EY
cov_xy= exp_calculation(XY, PXY)-E_XY
print ("cov[x,y]=", cov_xy)
STDX= (VAR_X)**0.5
STDY= (VAR_Y)**0.5
CORR= cov_xy/(STDX*STDY)
print ("cor[x,y]=",CORR)


# In[121]:


# question 5 
#AS the previous questions, I firt loaded the data set with Pandas and
# extracted random variables

data= pd.read_csv("diabetes-data1.csv")
AGE= data["AGE"].values
GENDER= data["Gender"].values
BMI= data["BMI"].values
BP= data["BP"].values

#  pairwise multipication to find a term for E[XY]
age_bmi= AGE*BMI
age_bp= AGE*BP
gender_bmi= GENDER*BMI
gender_bp= GENDER*BP

# expectation calculations . Expections were calculated with mean formula
E_age= sum(AGE)/len(AGE)
E_gender= sum(GENDER)/len(GENDER)
E_bmi= sum(BMI)/len(BMI)
E_bp=sum(BP)/len(BP)
E_age_bmi= sum(age_bmi)/len(age_bmi)
E_age_bp= sum(age_bp)/len(age_bp)
E_gender_bmi= sum(gender_bmi)/len(gender_bmi)
E_gender_bp = sum(gender_bp )/len(gender_bp)

# covariance calculations. We are using covariance fx from q3
def cov_calculation(E_XY, EX, EY):
    cov = E_XY-(EX*EY)
    return cov

cov_age_bmi= cov_calculation(E_age_bmi, E_age, E_bmi)
cov_age_bp= cov_calculation(E_age_bp, E_age, E_bp)
cov_gender_bmi=cov_calculation(E_gender_bmi,  E_gender, E_bmi)
cov_gender_bp= cov_calculation(E_gender_bp, E_gender, E_bp)

# variance and std calculations
def variance(x, exp):
    var= (sum(x**2)/len(x))-exp**2
    return var
var_age = variance(AGE,E_age)
std_age=(var_ge)**0.5
var_bmi= variance(BMI,E_bmi)
std_bmi = (var_bmi)**0.5

var_gender= variance(GENDER, E_gender)
std_gender= (var_gender)**0.5

var_bp = variance(BP, E_bp)
std_bp = (var_bp)**0.5

# correlation calculations
def correlation (cov_xy, stdx, stdy):
    cor= cov_xy/(stdx*stdy)
    return cor
cor_age_bmi= correlation(cov_age_bmi, std_bmi,std_age)
cor_age_bp= correlation(cov_age_bp, std_bp,std_age)
cor_gender_bmi= correlation(cov_gender_bmi, std_bmi,std_gender)
cor_gender_bp= correlation(cov_gender_bp, std_bp,std_gender)

print("corr(age,bmi) = ",cor_age_bmi, "\ncorr[age,BP] = ",cor_age_bp,
      "\ncorr[gender,BMI] = ",cor_gender_bmi,"\ncorr(gender, BP) = ",cor_gender_bp )












# In[ ]:





# In[ ]:





# In[ ]:




