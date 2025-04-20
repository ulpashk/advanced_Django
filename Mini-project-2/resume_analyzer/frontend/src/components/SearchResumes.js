import React, { useState } from 'react';
import axios from 'axios';

const SearchResumes = () => {
  const [skills, setSkills] = useState('');
  const [results, setResults] = useState([]);
  const [error, setError] = useState('');

  const handleSearch = async () => {
    if (!skills) {
      setError('Please enter at least one skill.');
      return;
    }

    // try {
    //   // Split the input skills by commas and send each skill as a separate query parameter
    //   const skillArray = skills.split(',').map(skill => skill.trim());
    //   const response = await axios.get('http://localhost:8000/api/resumes/search/', {
    //     params: { skill: skillArray },
    //     headers: {
    //       Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
    //     },
    //   });
  
    //   setResults(response.data.results);
    //   setError('');
    // } catch (error) {
    //   setError('Failed to fetch results.');
    // }

    try {
        const response = await axios.get('http://localhost:8000/api/resumes/search/', {
            params: { skill: skills.split(',').map(skill => skill.trim()) },
            headers: {
              Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
            },
          });
      setResults(response.data.results);
      setError('');
    } catch (error) {
      setError('Failed to fetch results.');
    }
  };

  return (
    <div>
      <h2>Search Resumes by Skills</h2>
      <input
        type="text"
        placeholder="Enter skills separated by commas"
        value={skills}
        onChange={(e) => setSkills(e.target.value)}
      />
      <button onClick={handleSearch}>Search</button>
      {error && <p>{error}</p>}
      {results.length > 0 && (
        <ul>
          {results.map((result, index) => (
            <li key={index}>
              <strong>Skills:</strong> {result.skills.join(', ')}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchResumes;
