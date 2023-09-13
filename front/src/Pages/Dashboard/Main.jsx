import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import body from '../../Assets/Styles/Body.module.scss'

function Main() {
    return (
        <>
        <hr className={body.MainContent}></hr>
            <main className={body.Standard}>
                <Outlet />
            </main>
        </>
    );
}

export default Main;