# -*- coding: utf-8 -*-
import pickle
mlist=["Martin","10","Hello there","86.9674e-7"]
p_f=open("C:/Users/lenovo/Desktop/m_p_l.pkl","wb")
pickle.dump(mlist,p_f)
p_f.close()