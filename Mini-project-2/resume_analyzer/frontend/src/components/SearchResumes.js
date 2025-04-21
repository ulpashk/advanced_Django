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
    <div className="container">
      <h2 className="my-4">Search Resumes by Skills</h2>
      <div className="input-group mb-3">
        <input
          type="text"
          className="form-control"
          placeholder="Enter skills separated by commas"
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
        />
        <button className="btn btn-primary" onClick={handleSearch}>
          Search
        </button>
      </div>
      {error && <div className="alert alert-danger">{error}</div>}

      {results.length > 0 && (
        <ul className="list-group mt-4">
          {results.map((result, index) => (
            <li key={index} className="list-group-item mb-4">
              <h4 className="text-primary mb-3">Resume #{index + 1}</h4>

              <h5>User Info</h5>
              <p><strong>Name:</strong> {result.user.name}</p>
              <p><strong>Email:</strong> {result.user.email}</p>
              <p><strong>Role:</strong> {result.user.role}</p>
              <p><strong>Uploaded At:</strong> {new Date(result.uploaded_at).toLocaleString()}</p>

              <hr />
              <h6>Resume Details</h6>
              <p><strong>Skills:</strong> {result.skills.join(', ')}</p>
              {result.education?.length > 0 && (
                <p><strong>Education:</strong> {result.education.join(', ')}</p>
              )}
              {result.experience?.length > 0 && (
                <p><strong>Experience:</strong> {result.experience}</p>
              )}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default SearchResumes;








// import React, { useState } from 'react';
// import axios from 'axios';

// const SearchResumes = () => {
//   const [skills, setSkills] = useState('');
//   const [results, setResults] = useState([]);
//   const [error, setError] = useState('');

//   const handleSearch = async () => {
//     if (!skills) {
//       setError('Please enter at least one skill.');
//       return;
//     }

//     try {
//       const response = await axios.get('http://localhost:8000/api/resumes/search/', {
//         params: { skill: skills.split(',').map(skill => skill.trim()) },
//         headers: {
//           Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
//         },
//       });
//       setResults(response.data.results);
//       setError('');
//     } catch (error) {
//       setError('Failed to fetch results.');
//     }
//   };

//   return (
//     <div className="container">
//       <h2 className="my-4">Search Resumes by Skills</h2>
//       <div className="input-group mb-3">
//         <input
//           type="text"
//           className="form-control"
//           placeholder="Enter skills separated by commas"
//           value={skills}
//           onChange={(e) => setSkills(e.target.value)}
//         />
//         <button className="btn btn-primary" onClick={handleSearch}>
//           Search
//         </button>
//       </div>
//       {error && <div className="alert alert-danger">{error}</div>}

//       {results.length > 0 && (
//           <ul className="list-group mt-4">
//           {results.map((result, index) => (
//             <li key={index} className="list-group-item mb-4"> {/* added mb-4 here */}
//               <h5>User Info</h5>
//               <p><strong>Name:</strong> {result.user.name}</p>
//               <p><strong>Email:</strong> {result.user.email}</p>
//               <p><strong>Role:</strong> {result.user.role}</p>
//               <p><strong>Uploaded At:</strong> {new Date(result.uploaded_at).toLocaleString()}</p>

//               <hr />
//               <h6>Resume Details</h6>
//               <p><strong>Skills:</strong> {result.skills.join(', ')}</p>
//               {result.education?.length > 0 && (
//                 <p><strong>Education:</strong> {result.education.join(', ')}</p>
//               )}
//               {result.experience?.length > 0 && (
//                 <p><strong>Experience:</strong> {result.experience}</p>
//               )}
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// };

// export default SearchResumes;





// import React, { useState } from 'react';
// import axios from 'axios';

// const SearchResumes = () => {
//   const [skills, setSkills] = useState('');
//   const [results, setResults] = useState([]);
//   const [error, setError] = useState('');

//   const handleSearch = async () => {
//     if (!skills) {
//       setError('Please enter at least one skill.');
//       return;
//     }

//     try {
//         const response = await axios.get('http://localhost:8000/api/resumes/search/', {
//             params: { skill: skills.split(',').map(skill => skill.trim()) },
//             headers: {
//               Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
//             },
//           });
//       setResults(response.data.results);
//       setError('');
//     } catch (error) {
//       setError('Failed to fetch results.');
//     }
//   };

//   return (
//     <div>
//       <h2>Search Resumes by Skills</h2>
//       <input
//         type="text"
//         placeholder="Enter skills separated by commas"
//         value={skills}
//         onChange={(e) => setSkills(e.target.value)}
//       />
//       <button onClick={handleSearch}>Search</button>
//       {error && <p>{error}</p>}
//       {results.length > 0 && (
//         <ul>
//           {results.map((result, index) => (
//             <li key={index}>
//               <strong>Skills:</strong> {result.skills.join(', ')}
//             </li>
//           ))}
//         </ul>
//       )}
//     </div>
//   );
// };

// export default SearchResumes;
