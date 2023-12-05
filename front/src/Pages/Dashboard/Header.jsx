import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss';
import DropdownMenu from './DropMenu';
import { useAuth } from '../Auth/AuthContext'; // Import useAuth
import { FaSignOutAlt, FaSignInAlt } from 'react-icons/fa';
import Dropdown from 'react-bootstrap/Dropdown';



function Header() {
  // Drop menu
  const [isOpen, setIsOpen] = useState(false);
  const [selectedOption, setSelectedOption] = useState('Account');

  const handleOptionClick = (option) => {
    setSelectedOption(option);
    setIsOpen(false);
  };
// Access the useAuth credentials
  const { refresh, access, user, logout } = useAuth(); 
  const [isAuthenticated, setIsAuthenticated] = useState(
    sessionStorage.getItem('isAuthenticated') === 'true'
  );

  const handleItemSelected = (item) => {
    // Handle the selected item here
    console.log(`Selected item: ${item.label}`);
  };
  const navigate = useNavigate();

  const buttonsList = [
    { onClick: () => navigate('/'), cao: "Home" },
  ];

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
            <Link to="/Courses">Courses</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/ContactUs">Contact</Link>
          </li>
          <li className={styles.NavLi}>
            {user ? (<Link to="/auth/LogOut"> {user} <FaSignOutAlt /></Link>) : (
              <div className="dropdown">
                <Link className="dropdown-toggle" onClick={() => setIsOpen(!isOpen)}>
                  {selectedOption}
                </Link>
                {isOpen && (
                  <div className={styles.DropLogin}>
                    <div className="dropdown-item" onClick={() => handleOptionClick('Login')}>
                    <Link to="/auth/LogIn"> {user}Login </Link>
                    </div>
                    <div className="dropdown-item" onClick={() => handleOptionClick('Register')}>
                    <Link to="/auth/LogOut"> {user}Register<FaSignOutAlt /></Link>
                    </div>
                    {/* Add more dropdown items as needed */}
                  </div>
                )}
              </div>)
            }
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
