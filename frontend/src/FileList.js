import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FileList = () => {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    axios.get('/api/files/')
      .then(response => {
        setFiles(response.data);
      })
      .catch(error => {
        console.error('There was an error fetching the files!', error);
      });
  }, []);

  const handleDelete = (id) => {
    axios.delete(`/api/files/${id}/`)
      .then(response => {
        setFiles(files.filter(file => file.id !== id));
      })
      .catch(error => {
        console.error('There was an error deleting the file!', error);
      });
  };

  return (
    <div>
      <h2>Files</h2>
      <ul>
        {files.map(file => (
          <li key={file.id}>
            {file.name}
            <button onClick={() => handleDelete(file.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FileList;
