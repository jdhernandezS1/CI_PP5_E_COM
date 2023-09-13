import React from 'react';
import {Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.css'

function NavigationBar() {
  return (
    <>
      <nav >
        <ul>
          <li className={styles.NavLi}>
            <Link to="/">Home</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/about">About</Link>
          </li>
          <li className={styles.NavLi}>
            <Link to="/contact">Contact</Link>
          </li>
        </ul>
      </nav>
      <Outlet />
    </>
  );
}

export default NavigationBar;
