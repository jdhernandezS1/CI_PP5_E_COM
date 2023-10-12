import React from 'react';

import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext';

function Logout(props) {
  const { refresh, access, logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout(); // Call the logout function to clear the token

    // Redirect to the login or home page after logout
    navigate('/'); // Replace with the desired redirect route
  };

  return (
    <div>
      <p>Logged Out</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Logout;
