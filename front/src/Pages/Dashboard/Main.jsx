import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import body from '../../Assets/Styles/Body.module.scss'

function Main() {
    return (
        <>
            <main className={`${body.Standard} ${body.MainContent}`}>
                <Outlet />
            </main>
        </>
    );
}

export default Main;