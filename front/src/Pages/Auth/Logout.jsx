import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './AuthContext'; // Import useAuth

function Logout() {
  const { logout } = useAuth(); // Access the logout function from AuthContext
  const navigate = useNavigate();
  const { token } = useAuth(); // Access the logout function from AuthContext

  const handleLogout = () => {
    logout(); // Call the logout function to clear the token

    // Redirect to the login or home page after logout
    navigate('/'); // Replace with the desired redirect route
  };

  return (
    <div>
      <p>Logged Out</p>
      <button onClick={handleLogout}>Logout</button>
      <p>Token: {token}</p>
    </div>
  );
}

export default Logout;
