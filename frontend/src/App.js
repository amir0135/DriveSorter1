import React from 'react';
import './App.css';
import FileUpload from './FileUpload';
import FileList from './FileList'; // Ensure you have a FileList component for displaying files

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>DriveSorter</h1>
      </header>
      <main>
        <FileUpload />
        <FileList />
      </main>
    </div>
  );
}

export default App;
