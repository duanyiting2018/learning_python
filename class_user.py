# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 20:35:57 2020

@author: duanyiting
"""
class user:
    def user_see1(self):
        self.user_name1="Danny"
        self.user_password1=193752
        print(self.user_name1,", password:",self.user_password1)
    def user_change(self,user_name2,user_password2):
        self.user_name1=user_name2
        if len(str(user_password2))==6:
            self.user_password1=user_password2
            print("修改成功！")
        else:
            print("无法改密码，数位错误！")
        int(user_password2)
    def user_see2(self):
        return self.user_name1+", password:"+str(self.user_password1)
user=user()
user.user_see1()
#user.user_change("duanyiting",33654)
user.user_change("duanyiting",336549)
print(user.user_see2())