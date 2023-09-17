import React, { useState } from 'react';
import styles from '../../Assets/Styles/NavigationBar.module.scss';
import { Link, useNavigate } from 'react-router-dom';
import { FaHome } from 'react-icons/fa';
import FloatingButtons from 'react-floating-buttons';

function DropdownMenu(props) {
  const navigate = useNavigate();
  const [isOpen, setIsOpen] = useState(false);

  const buttonsList = [
    { onClick: () => { navigate('/'); }, text: ' Home', },
    { onClick: () => { navigate('/products'); }, text: ' Home', icon: <FaHome />, },
  ];

  const toggleMenu = () => {
    setIsOpen((prevIsOpen) => !prevIsOpen);
  };

  return (
      <div className={styles.DropdownMenuTitle}>
        <div className={styles.DropdownMenuButton}><FloatingButtons
          onClick={toggleMenu}
          // buttonType="plus"
          variant="plus"
          dimension={50}
          buttonsList={buttonsList}
          top={'calc(50% - 25px)'}
          left={'5%'}
          direction="right"
        >
          Capriccio
        </FloatingButtons></div>
      <div><h1>Capriccio</h1></div>
      </div>
  );
}

export default DropdownMenu;
