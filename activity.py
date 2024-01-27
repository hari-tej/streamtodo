import streamlit as st
from streamlit_option_menu import option_menu
import mysql.connector as sql

myobj=sql.connect(host="localhost",user="root",password="hariteja",database="application")
mycursor=myobj.cursor()

if(myobj.is_connected):
    print("Successfully connected")

st.title("TODO list")

with st.sidebar:
    option=option_menu("Activity",["create","read","update","delete"],icons=['pen','book','wrench','trash'],default_index=0)


if option=="create":
    username=st.text_input("Name")
    email=st.text_input("Email")

    if st.button("Add User"):
        sql="insert into user(username,email) values(%s,%s)"
        values=(username,email)
        mycursor.execute(sql,values)
        myobj.commit()
        st.success("Added successfully")

elif option=="read":
    st.subheader("DETAILS")
    mycursor.execute("select * from user")
    data=mycursor.fetchall()
    for row in data:
        st.write(row)
elif option=="update":
    id=st.number_input("Enter ID",min_value=1)
    newname=st.text_input("Enter new name")
    newmail=st.text_input("Enter new mail")
    if st.button("update"):
      sql="update user set username=%s, email=%s where id=%s"
      values=(newname,newmail,id)
      mycursor.execute(sql,values)
      myobj.commit()
      st.success("updated successfully")

else:
     iod=st.number_input("Enter the id",min_value=1)

     if st.button("delete"):
         sql="delete from user where id=%s"
         value=(iod,)
         mycursor.execute(sql,value)
         st.success("deleted successfully")
         myobj.commit()