import React, { useState, useEffect, useRef } from 'react';
import styles from '../../Assets/Styles/NavigationBar.module.scss';
import { Link, useNavigate } from 'react-router-dom';
import FloatingButtons from 'react-floating-buttons';
import home from '../../Assets/Icons/homeIcon.svg';
import buy from '../../Assets/Icons/buy.svg';
import courses from '../../Assets/Icons/courses.svg';
import contact from '../../Assets/Icons/contact.svg';

function DropdownMenu(props) {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);
  const menuRef = useRef(null);

  const buttonsList = [
    { onClick: () => navigate('/'), src: home },
    { onClick: () => navigate('/products'), src: buy },
    { onClick: () => navigate('/Courses'), src: courses },
    { onClick: () => navigate('/ContactUs'), src: contact },
  ];

  const toggleMenu = () => {
    setIsOpen((prevIsOpen) => !prevIsOpen);
  };

  const closeMenu = () => {
    setIsOpen(false);
  };


  return (
    <div className={styles.DropdownMenuTitle}>
      <div className={styles.DropdownMenuButton} ref={menuRef}>
        <FloatingButtons
          onClick={toggleMenu}
          variant="plus"
          dimension={50}
          buttonsList={buttonsList}
          top={'calc(50% - 25px)'}
          left={'5%'}
          direction="down"
        >
          Capriccio
        </FloatingButtons>
      </div>
      <div>
        <h1><Link to="/" className={styles.TitleLink}>Capriccio</Link></h1>
      </div>
    </div>
  );
}

export default DropdownMenu;
