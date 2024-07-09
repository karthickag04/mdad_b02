#!/usr/bin/env python
# coding: utf-8

# In[5]:


x = 10
y = 20

# arithmatic operator
print(x+y)
print(x*y)
print(x-y)
print(x/y)
print(x%y)
print(x**y)

# comparision operator
print(x==y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)



# In[6]:


def operatordemo():
    z = 10
    v = 10
    print(z + v)
    print(z - v)
    print(z * v)
    print(z / v)


# In[8]:


operatordemo()
operatordemo()
operatordemo()
operatordemo()


# In[20]:


def addition():
    z = 10
    v = 11
    print( "added value of z and v is " , z + v)
    print( "added value of z :" ,z,"and v:" ,v, " is ", z + v)
    print( f"added value of z : {z} and v: {v} is" , z + v)

addition()


# In[22]:


def additionr():
    z = 10
    v = 11
    return z + v

additionr()


# In[23]:


resutl_1=addition()
resutl_2=additionr()


# In[24]:


print(resutl_1)


# In[25]:


print(resutl_2)


# In[27]:


if(resutl_1==21):
    print("its equal under normal")
if(resutl_2==21):
    print("its equal under r")


# In[29]:


def addition_wit_args(z,v):
    return z + v

addition_wit_args(10,31)


# In[31]:


x


# In[34]:


def operatordemo1(x,y):
    """This function takes two numbers and returns their sum"""
    print("addition",x+y)
    print("addition",x+y)
    print("addition",x+y)
    print("addition",x+y)
    print("addition",x+y)
    print("addition",x+y)
    print("addition",x+y)


# In[37]:


def operator_with_if(operatorsymbol, x,y):
    if(operatorsymbol=='+'):
        print("addition", x + y)
    elif(operatorsymbol == '-'):
        print("subtraction", x - y)
    
    elif(operatorsymbol == '*'):
        print("subtraction", x * y)
    else:
        print("division", x / y)



# In[38]:


operatordemowithselection('+',33,22)

