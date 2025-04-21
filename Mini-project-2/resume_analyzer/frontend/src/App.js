import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import NavBar from './components/NavBar';
import LoginForm from './components/LoginForm';
import SignupForm from './components/SignupForm';
import UploadResume from './components/UploadResume';
import SearchResumes from './components/SearchResumes';
import { logoutUser } from './api/auth';
import axios from 'axios';
import Home from './components/Home';

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const validateToken = async () => {
      const token = localStorage.getItem('accessToken');
      if (!token) {
        setLoading(false);
        return;
      }

      try {
        // Use any authenticated endpoint to validate the token
        await axios.get('http://localhost:8000/api/resumes/search/?skill[]=test', {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        });
        setIsAuthenticated(true);
      } catch (error) {
        localStorage.removeItem('accessToken');
        setIsAuthenticated(false);
      } finally {
        setLoading(false);
      }
    };

    validateToken();
  }, []);

  const handleLogout = () => {
    logoutUser();
    setIsAuthenticated(false);
  };

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
  };

  const handleSignupSuccess = () => {
    setIsAuthenticated(true);
  };

  if (loading) return <div className="text-center mt-5">Loading...</div>;

  return (
    <Router>
      <NavBar isAuthenticated={isAuthenticated} onLogout={handleLogout} />
      <div className="container mt-4">
        <Routes>
          {!isAuthenticated ? (
            <>
              <Route path="/login" element={<LoginForm onLoginSuccess={handleLoginSuccess} />} />
              <Route path="/signup" element={<SignupForm onSignupSuccess={handleSignupSuccess} />} />
              <Route path="*" element={<Navigate to="/login" replace />} />
            </>
          ) : (
            <>
              <Route path="/home" element={<Home />} />
              <Route path="/upload" element={<UploadResume />} />
              <Route path="/search" element={<SearchResumes />} />
              <Route path="*" element={<Navigate to="/home" replace />} />
            </>
          )}
        </Routes>
      </div>
    </Router>
  );
};

export default App;






// // src/App.js
// import React, { useState } from 'react';
// import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
// import 'bootstrap/dist/css/bootstrap.min.css';
// import NavBar from './components/NavBar';
// import LoginForm from './components/LoginForm';
// import SignupForm from './components/SignupForm';
// import UploadResume from './components/UploadResume';
// import SearchResumes from './components/SearchResumes';
// import { logoutUser } from './api/auth';

// const App = () => {
//   const [isAuthenticated, setIsAuthenticated] = useState(!!localStorage.getItem('accessToken'));

//   const handleLogout = () => {
//     logoutUser();
//     setIsAuthenticated(false);
//   };

//   const handleLoginSuccess = () => {
//     setIsAuthenticated(true);
//   };

//   const handleSignupSuccess = () => {
//     setIsAuthenticated(true);
//   };

//   return (
//     <Router>
//       <NavBar isAuthenticated={isAuthenticated} onLogout={handleLogout} />
//       <div className="container mt-4">
//         <Routes>
//           {!isAuthenticated ? (
//             <>
//               <Route path="/login" element={<LoginForm onLoginSuccess={handleLoginSuccess} />} />
//               <Route path="/signup" element={<SignupForm onSignupSuccess={handleSignupSuccess} />} />
//               <Route path="*" element={<Navigate to="/login" />} />
//             </>
//           ) : (
//             <>
//               <Route path="/upload" element={<UploadResume />} />
//               <Route path="/search" element={<SearchResumes />} />
//               <Route path="*" element={<Navigate to="/upload" />} />
//             </>
//           )}
//         </Routes>
//       </div>
//     </Router>
//   );
// };

// export default App;





// import React, { useState } from 'react';
// import LoginForm from './components/LoginForm';
// import SignupForm from './components/SignupForm';
// import UploadResume from './components/UploadResume';
// import SearchResumes from './components/SearchResumes';
// import { logoutUser } from './api/auth';


// const App = () => {
//   const [isAuthenticated, setIsAuthenticated] = useState(
//     !!localStorage.getItem('accessToken')
//   );
//   const [isSignup, setIsSignup] = useState(false);

//   const handleLogout = () => {
//     logoutUser();
//     setIsAuthenticated(false);
//   };

//   const handleLoginSuccess = () => {
//     setIsAuthenticated(true);
//   };

//   const handleSignupSuccess = () => {
//     setIsSignup(false); // Redirect back to login after successful signup
//   };

//   return (
//     <div>
//       {isAuthenticated ? (
//         <>
//           <button onClick={handleLogout}>Logout</button>
//           <UploadResume />
//           <SearchResumes />
//         </>
//       ) : (
//         <>
//           {isSignup ? (
//             <SignupForm onSignupSuccess={handleSignupSuccess} />
//           ) : (
//             <LoginForm onLoginSuccess={handleLoginSuccess} />
//           )}
//           <button onClick={() => setIsSignup(!isSignup)}>
//             {isSignup ? 'Already have an account? Login' : "Don't have an account? Signup"}
//           </button>
//         </>
//       )}
//     </div>
//   );
// };




// export default App;