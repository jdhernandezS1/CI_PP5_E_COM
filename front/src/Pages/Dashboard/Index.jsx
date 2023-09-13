import React from 'react';
import { Outlet, Link } from 'react-router-dom';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import Footer from './Footer';
import Header from './Header';
import Main from './Main';
function Index() {
  return (
    <>
      <Header />
      <Main/>
      <Footer />
    </>
  );
}

export default Index;
