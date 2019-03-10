# -*- coding: utf-8 -*-
import pickle
p_f=open("C:/Users/lenovo/Desktop/m_p_l.pkl","rb")
r_l=pickle.load(p_f)
p_f.close()
print(r_l)