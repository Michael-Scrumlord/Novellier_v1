import React from 'react';
import LoginForm from './components/auth/LoginForm';
import RegisterForm from './components/auth/RegisterForm';
// Basic styling - consider moving to a CSS file
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Novellier</h1>
      </header>
      <main>
        <div className="auth-container">
          <div className="auth-form">
            <LoginForm />
          </div>
          <div className="auth-form">
            <RegisterForm />
          </div>
        </div>
        {/* More content will go here: Novel project management, editor, etc. */}
      </main>
    </div>
  );
}

export default App;
