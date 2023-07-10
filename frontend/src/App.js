import logo from './logo.svg';
import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [inputField, setInputField] = useState('');
  const [searchResults, setSearchResults] = useState([]);

  const handleFormSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post('api/search', { searchTerm: inputField });
      setSearchResults(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleInputChange = (e) => {
    setInputField(e.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Library Management System</p>
        <div className="Login">
          <form onSubmit={handleFormSubmit}>
            <input type="text" name="input_field" value={inputField} onChange={handleInputChange} /> <br />
            <input type="submit" value="Submit" />
          </form>
        </div>
      </header>
      {searchResults.length > 0 &&
        <div className="SearchResults">
          {searchResults.map(result => (
            <div key={result.id}>
              <h3>{result.title}</h3>
              <p>Author: {result.author}</p>
              {/* Add more fields as needed */}
            </div>
          ))}
        </div>
      }
    </div>
  );
}


export default App;

