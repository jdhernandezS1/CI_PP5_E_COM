import React, { Component } from 'react';
import styles from '../../Assets/Styles/NavigationBar.module.scss'
import { Outlet, Link } from 'react-router-dom';

class DropdownMenu extends Component {
  constructor(props) {
    super(props);

    this.state = {
      isOpen: false,
    };
  }

  toggleMenu = () => {
    this.setState((prevState) => ({
      isOpen: !prevState.isOpen,
    }));
  };

  render() {
    const { isOpen } = this.state;

    return (
      <div >
        <button className={styles.DropdownMenuButton} onClick={this.toggleMenu}>
          {this.props.triggerText}
        </button>
        {isOpen && (
          <ul className={styles.DropdownMenu}>
            <li ><Link to="/">Home</Link></li>
            <li ><Link to="/Products/">Products</Link></li>
            <li ><Link to="/">Home</Link></li>
          </ul>
        )}
      </div>
    );
  }
}

export default DropdownMenu;
