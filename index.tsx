import { useState } from "react";

function HomePage() {
    const [books, setBooks] = useState([]);

    return (
        <div>
            <h1>Book Tracker</h1>
            {/* Add other components like AddBook, BookList, etc. */}
        </div>
    );
}

export default HomePage;
