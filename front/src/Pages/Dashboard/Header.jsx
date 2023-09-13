import React, { Fragment } from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import body from '../../Assets/Styles/Body.module.scss'
import Footer from './Footer';

function Header() {
    return (
        <header className={`${styles.HeaderStandard}`}>
                <nav>
                    <ul  className={styles.Nav}>
                        <li className={styles.NavLi}>
                            <Link to="/">Home</Link>
                        </li>
                        <li className={styles.NavLi}>
                            <Link to="/Products">Products</Link>
                        </li>
                        <li className={styles.NavLi}>
                            <Link to="/Courses">About</Link>
                        </li>
                        <li className={styles.NavLi}>
                            <Link to="/ContactUs">Contact</Link>
                        </li>
                    </ul>
                </nav>
        </header >
    );
}

export default Header;

