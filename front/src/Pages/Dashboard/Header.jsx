import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss';
import DropdownMenu from './DropMenu';

function Header() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    sessionStorage.getItem('isAuthenticated') === 'true'
  );

  const handleItemSelected = (item) => {
    // Handle the selected item here
    console.log(`Selected item: ${item.label}`);
  };

  const toggleAuthentication = () => {
    // Toggle the authentication state
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
              <Link to="/Logout">Logout</Link>
            ) : (
              <Link to="/Auth" >{isAuthenticated ? 'Logout' : 'Login'}</Link>
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
