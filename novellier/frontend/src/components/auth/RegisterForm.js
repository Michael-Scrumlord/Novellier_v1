import React, { useState } from 'react';

const RegisterForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage('Attempting to register...');
        // TODO: Implement API call to /api/register
        // Example:
        // try {
        //     const response = await fetch('/api/register', {
        //         method: 'POST',
        //         headers: { 'Content-Type': 'application/json' },
        //         body: JSON.stringify({ username, email, password }),
        //     });
        //     const data = await response.json();
        //     if (response.ok) {
        //         setMessage(data.message);
        //         // TODO: Handle successful registration (e.g., redirect to login)
        //     } else {
        //         setMessage(`Registration failed: ${data.message}`);
        //     }
        // } catch (error) {
        //     setMessage(`Registration error: ${error.message}`);
        // }
        console.log('Register form submitted with:', { username, email, password });
        // Replace with actual API call
        setTimeout(() => setMessage('Registration functionality to be implemented.'), 1000);
    };

    return (
        <div>
            <h2>Register</h2>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="register-username">Username:</label>
                    <input
                        type="text"
                        id="register-username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="register-email">Email:</label>
                    <input
                        type="email"
                        id="register-email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />
                </div>
                <div>
                    <label htmlFor="register-password">Password:</label>
                    <input
                        type="password"
                        id="register-password"
                        value={password}
                        onChange={(e) => setPassword(e.target.value)}
                        required
                    />
                </div>
                <button type="submit">Register</button>
            </form>
            {message && <p>{message}</p>}
        </div>
    );
};

export default RegisterForm;
