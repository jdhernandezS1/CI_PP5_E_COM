import React, { useState } from 'react';
import { postDataFromApi } from '../../Services/Utils/postDataClient';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext'; // Import the useAuth hook

import Loged from './Loged';
import styles from '../../Assets/Styles/Auth.module.scss';

function LogIn() {
  const { login } = useAuth();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      var response = await postDataFromApi('token/', { username, password });
      console.log(response);
      if (response && response.access) {
        login(response.access);
        // authenticated = true;
        navigate('/'); // Replace with the desired redirect route
      }
    } catch (error) {
      // Handle login error (e.g., show an error message)
      console.error('Login error:', error);
    }
  };
  return (
    <div>
      <h1>Login</h1>
      <input
        type="text"
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="password"
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={handleLogin}>Login</button>
      

    </div>
  );
}


export default LogIn;
