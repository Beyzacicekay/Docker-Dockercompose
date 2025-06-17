import React, { useState, useEffect } from "react";

function App() {
  const [books, setBooks] = useState([]);
  const [title, setTitle] = useState("");
  const [author, setAuthor] = useState("");

  const fetchBooks = async () => {
    const response = await fetch("http://localhost:6060/api/books");
    const data = await response.json();
    setBooks(data);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await fetch("http://localhost:6060/api/books", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title, author })
    });
    setTitle("");
    setAuthor("");
    fetchBooks();
  };

  useEffect(() => {
    fetchBooks();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Kitap Ekle</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Kitap adı"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Yazar"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
          required
        />
        <button type="submit">Ekle</button>
      </form>
      <h2>Kitaplar</h2>
      <ul>
        {books.map((book) => (
          <li key={book.id}>{book.title} - {book.author}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
