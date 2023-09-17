import React, { Component } from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import body from '../../Assets/Styles/Body.module.scss'
import Footer from './Footer';
import DropdownMenu from './DropMenu';
function Header() {
    const handleItemSelected = (item) => {
        // Handle the selected item here
        console.log(`Selected item: ${item.label}`);
    };
    return (
        <header className={`${styles.HeaderStandard}`}>
            <nav>
                <ul className={styles.Nav}>
                    <li className={styles.NavLi}>
                        <Link to="/">Capricio</Link>
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
                </ul>
            </nav>
            <div className={styles.DropdownMenu}>
                <DropdownMenu
                    triggerText="Select an Option" // Text for the button that triggers the dropdown
                     // Array of dropdown menu items
                    onItemSelected={handleItemSelected} // Callback function for item selection
                />

            </div>
        </header >
    );
}

export default Header;

