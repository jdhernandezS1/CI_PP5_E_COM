import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss';
import DropdownMenu from './DropMenu';
import { useAuth } from '../Auth/AuthContext'; // Import useAuth

function Header() {
  const { logout } = useAuth(); // Access the logout function from AuthContext
  const [isAuthenticated, setIsAuthenticated] = useState(
    sessionStorage.getItem('isAuthenticated') === 'true'
  );

  const handleItemSelected = (item) => {
    // Handle the selected item here
    console.log(`Selected item: ${item.label}`);
  };

  const toggleAuthentication = () => {
    //  i need to veryfy the token here 
    // Toggle the authentication state
    console.log(useAuth.token);
    const newIsAuthenticated = !isAuthenticated;
    setIsAuthenticated(newIsAuthenticated);

    // Store the authentication state in session storage
    sessionStorage.setItem('isAuthenticated', newIsAuthenticated.toString());
  };

  // Optional: You can use the useEffect hook to retrieve the authentication state on component mount
  useEffect(() => {
    const storedIsAuthenticated = sessionStorage.getItem('isAuthenticated') === 'true';
    setIsAuthenticated(storedIsAuthenticated);
  }, []);

  return (
    <header className={`${styles.HeaderStandard}`}>
      <nav>
        <ul className={styles.Nav}>
          <li className={`${styles.NavLi} ${styles.HomeButton}`}>
            <Link to="/"> Capricio</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/Products/">Products</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/Courses">About</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/ContactUs">Contact</Link>
          </li>
          <li className={styles.NavLi} onClick={toggleAuthentication}>
            {isAuthenticated ? (
              <Link to="/auth/LogOut">Logout</Link>
            ) : (
              <Link to="/auth/LogIn" >{isAuthenticated ? 'Logout' : 'Login'}</Link>
            )}

          </li>
        </ul>
      </nav>
      <div className={styles.DropdownMenu}>
        <DropdownMenu
          triggerText="Select an Option"
          onItemSelected={handleItemSelected}
        />
      </div>
    </header>
  );
}

export default Header;
