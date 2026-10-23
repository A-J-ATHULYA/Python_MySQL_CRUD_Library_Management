import streamlit as st
from numpy.core import records

from Book_views import LibraryManager
# from MySQL_Works.Library_db.Book_views import library_instance

library_instance = LibraryManager()

tab1, tab2 = st.tabs(["ADD", "VIEW"])

with tab1:
    st.header("Add New Book")
    Title = st.text_input("Enter Book Name :")
    Author = st.text_input("Enter Author Name :")
    Price = st.text_input("Enter Book Price :")
    Category = st.text_input("Enter Book Category :")
    Published_Year = st.text_input("Enter Published Year :")
    if st.button("Add New Book"):
        library_instance.post(book_name=Title, author_name=Author, price=Price, type=Category,  published_year=Published_Year)
        st.success("New Book Added Successfully")

with tab2:
    st.header("View Book Details")
    records = library_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No Book Details Found")
