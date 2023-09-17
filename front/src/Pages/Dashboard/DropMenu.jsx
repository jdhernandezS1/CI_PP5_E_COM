import React, { Component } from 'react';
import styles from '../../Assets/Styles/NavigationBar.module.scss'

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
          <ul className="dropdown-menu">
            {this.props.items.map((item) => (
              <li key={item.id} onClick={() => this.props.onItemSelected(item)}>
                {item.label}
              </li>
            ))}
          </ul>
        )}
      </div>
    );
  }
}

export default DropdownMenu;
