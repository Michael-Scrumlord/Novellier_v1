import React, { useState } from 'react';

const LoginForm = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Attempting to log in...');
        // TODO: Implement API call to /api/login
        // Example:
        // try {
        //     const response = await fetch('/api/login', {
        //         method: 'POST',
        //         headers: { 'Content-Type': 'application/json' },
        //         body: JSON.stringify({ username, password }),
        //     });
        //     const data = await response.json();
        //     if (response.ok) {
        //         setMessage(`Login successful. User ID: ${data.user_id}`);
        //         // TODO: Handle successful login (e.g., store token, redirect)
        //     } else {
        //         setMessage(`Login failed: ${data.message}`);
        //     }
        // } catch (error) {
        //     setMessage(`Login error: ${error.message}`);
        // }
        console.log('Login form submitted with:', { username, password });
        // Replace with actual API call
        setTimeout(() => setMessage('Login functionality to be implemented.'), 1000);
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="login-username">Username:</label>
                    <input
                        type="text"
                        id="login-username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="login-password">Password:</label>
                    <input
                        type="password"
                        id="login-password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Login</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default LoginForm;
