import streamlit as st
import json
import time

# page config

# file handling function

def load_books():
    try:
        with open("books.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_books(books):
    with open("books.json", "w") as file:
        json.dump(books, file)

books = load_books()

st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in {
        animation: fadeIn 1.5s ease-in-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Book Management")
options = st.sidebar.radio("Navigation", ["📚 Home","➕ Add Book", "❌ Remove a Book", "🔍Search for a book", "📖 Display all books  ", "📊 Display statistics","🚪 Exit"])

# home page
if options == "📚 Home":
    st.markdown("""
               <div class="fade-in" style="text-align: center; background: linear-gradient(to right, #6a11cb, #2575fc); padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0, 0, 0, 0.2); color: #fff; max-width: 600px; margin: auto; animation: fadeIn 1.5s ease-in-out;">
    <h1 style="margin-bottom: 15px; font-size: 24px;">📖 Welcome to library management system</h1>
    <p style="color: #f7f7f7; font-size: 16px;">📚 Easily add, remove, search and display books</p>
</div>

<style>
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-10px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
        """, unsafe_allow_html=True
                )

# add book page
if options == "➕ Add Book":
    st.title("Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.checkbox("Read")
    
    if st.button("Add Book"):
        if title and author and year and genre:
            books.append({
                "title": title, "Author": author, "Year": year, "Genre": genre, "Read": read_status
            })
            save_books(books)
            st.success("Book added successfully!")
            st.balloons()
           
        else:
            st.error("Please fill in all fields")



# remove book page
elif options == "❌ Remove a Book":
    st.header("🗑 Remove a Book")
    titles = [book["title"] for book in books]

    if titles:
        book_to_remove = st.selectbox("Select a book to remove", titles)
        if st.button("Remove Book"):
            books = [book for book in books if book["title"] != book_to_remove]
            save_books(books)
            st.toast("Book removed successfully!", icon="✅")
            st.success(f"'{book_to_remove}' removed from library!")
            st.snow()
    else:
        st.info("No books in the library yet!")


# search book page
elif options == "🔍Search for a book":
    st.header("🔍 Search for a book")
    search_term = st.text_input("Enter a book title or author")

    if st.button("Search"):
        results = [book for book in books if search_term.lower() in book["title"].lower() or search_term.lower() in book["Author"].lower()]
        if results:
            for book in results:
                st.write(f"**Title:** {book['title']} / **Author:** {book['Author']} / **Year:** {book['Year']} / **Genre:** {book['Genre']} / **Read:** {book['Read']}")
        else:
            st.info("No books found matching your search")

# Display all books

elif options == "📖 Display all books  ":
    st.header("📖 Collection of all books")
    
    if books:
        cols = st.columns(3)
        for idx, book in enumerate(books):
            with cols[idx % 3]:
                st.markdown(
                    f"""
                    <div style="
    border: 2px solid #6a0dad; 
    padding: 20px; 
    border-radius: 12px; 
    background: linear-gradient(135deg, #6a0dad, #9370db); 
    box-shadow: 4px 4px 15px rgba(0,0,0,0.2);
    color: #fff;
    max-width: 350px;
    margin: 10px auto;
    text-align: left;
">
    <h4 style="font-weight: bold; font-size: 20px; margin-bottom: 10px;">
        📖 {book['title']}
    </h4>
    <p style="font-size: 16px; margin: 5px 0;"><b>✍️ Author:</b> {book['Author']}</p>
    <p style="font-size: 16px; margin: 5px 0;"><b>📅 Year:</b> {book['Year']}</p>
    <p style="font-size: 16px; margin: 5px 0;"><b>📚 Genre:</b> {book['Genre']}</p>
    <p style="font-size: 16px; margin: 5px 0;">
        <b>📖 Status:</b> 
        <span style="color: { 'lightgreen' if book['Read'] else 'tomato' };">
            {"✅ Read" if book['Read'] else "❌ Unread"}
        </span>
    </p>
</div>

                    """,
                    unsafe_allow_html=True
                )
                
    else:
        st.info("No books in the library yet!")


# Display statistics
elif options == "📊 Display statistics":
    st.header("📊 Library Collection Statistics")

    total_books = len(books)
    read_books = len([book for book in books if book['Read']])
    st.metric("Total Books", total_books)
    st.metric("Read Books", read_books)
    if total_books > 0:
        st.metric(f"Percentage of Read Books", f"{read_books / total_books * 100:.2f}%")
    else:
        st.metric("Percentage of Read Books", "0.00%")

        
st.sidebar.write("📌 Use the sidebar to navigate different sections.")


# Exit Library Management System
if options == "🚪 Exit":
      st.header("👋 Thank you for using the Library Management System!")
      if st.button("Exit"):
          save_books(books)
          st.success("Data saved. Exiting...")
          st.balloons()
          time.sleep(2)
          st.rerun()
          
# Footer
st.markdown("---")
st.markdown("""
    <p style='text-align: center; color: gray;'>© 2025 Library Manager | Developed by Sumair Khan</p>
""", unsafe_allow_html=True)