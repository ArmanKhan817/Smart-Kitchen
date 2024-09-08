
# coding: utf-8

# PUT Things 

# In[1]:


from IPython.display import Image
Image("IoT.png")


# In[2]:


import requests

url = 'https://18fb106h5f.execute-api.us-west-2.amazonaws.com/dev/putThings'

data = {
  "customerid": "6777",
  "things": "Milk",
  "Milk": 1
}
r = requests.post(url,json=data)
print(r)


# Crtical data

# In[3]:


from IPython.display import Image
Image("Critical.jpg")


# In[1]:


import requests

url = 'https://akujjoyzwi.execute-api.us-west-2.amazonaws.com/alert/alert'
alert={"Gas_lickage": "yes","Temperature": 150}
a = requests.post(url,json=alert)
print(a)

