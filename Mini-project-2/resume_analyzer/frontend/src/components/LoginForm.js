// src/components/LoginForm.js
import React, { useState } from 'react';
import { loginUser } from '../api/auth';

const LoginForm = ({ onLoginSuccess }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await loginUser(email, password);

      alert('Logged in!');
      onLoginSuccess(); // notify App component
    } catch (err) {
      console.error(err);
      alert('Login failed!');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Login</h2>
      <input
        type="email"
        placeholder="Email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      /><br />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      /><br />
      <button type="submit">Login</button>
    </form>
  );
};

export default LoginForm;








// // src/components/LoginForm.js
// import React, { useState } from 'react';
// import { loginUser } from '../api/auth';

// const LoginForm = ({ onLoginSuccess }) => {
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');

//   const handleSubmit = async (e) => {
//     e.preventDefault();
//     try {
//       await loginUser(email, password);
//       alert('Logged in!');
//       onLoginSuccess(); // notify App component
//     } catch (err) {
//       alert('Login failed!');
//     }
//   };

//   return (
//     <form onSubmit={handleSubmit}>
//       <h2>Login</h2>
//       <input
//         type="email"
//         placeholder="Email"
//         value={email}
//         onChange={(e) => setEmail(e.target.value)}
//         required
//       /><br />
//       <input
//         type="password"
//         placeholder="Password"
//         value={password}
//         onChange={(e) => setPassword(e.target.value)}
//         required
//       /><br />
//       <button type="submit">Login</button>
//     </form>
//   );
// };

// export default LoginForm;
