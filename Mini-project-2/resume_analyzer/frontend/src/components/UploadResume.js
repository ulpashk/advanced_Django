import React, { useState } from 'react';
import axios from 'axios';

const UploadResume = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState('');

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      setMessage('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
        const response = await axios.post(
            'http://localhost:8000/api/resumes/upload/',
            formData,
            {
              headers: {
                'Content-Type': 'multipart/form-data',
                Authorization: `Bearer ${localStorage.getItem('accessToken')}`,
              },
            }
          );
    //   const response = await axios.post('/api/resumes/upload/', formData, {
    //     headers: {
    //       'Content-Type': 'multipart/form-data',
    //       Authorization: `Bearer ${localStorage.getItem('token')}`, // Assuming JWT token is stored in localStorage
    //     },
    //   });
      setMessage(response.data.message);
    } catch (error) {
      setMessage('Failed to upload resume.');
    }
  };

  return (
    <div>
      <h2>Upload Resume</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      <p>{message}</p>
    </div>
  );
};

export default UploadResume;
