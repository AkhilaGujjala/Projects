import React, { useState } from 'react';
import axios from 'axios';

const SearchPage = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('/api/search', { searchTerm });
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <form onSubmit={handleSearch}>
        <input
          type="text"
          name="search"
          placeholder="Enter search term"
          value={searchTerm}
          onChange={(e) => setSearchTerm(e.target.value)}
        />
        <button type="submit">Search</button>
      </form>

      {searchResults.length > 0 ? (
        <div>
          {searchResults.map((result) => (
            <div key={result.id}>
              <h3>{result.title}</h3>
              <p>Author: {result.author}</p>
              {/* Add more fields as needed */}
            </div>
          ))}
        </div>
      ) : (
        <p>No search results found.</p>
      )}
    </div>
  );
};

export default SearchPage;
