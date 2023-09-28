import React, { Component } from 'react';
import { postDataFromApi } from '../../Services/Utils/postDataClient';
import { useNavigate } from 'react-router-dom';
import Loged from './Loged';
import styles from '../../Assets/Styles/Auth.module.scss';
import { AuthProvider } from './AuthContext'; // Import AuthProvider

class LogIn extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: '',
      responseData: null,
      error: null,
      data:'',
    };
  }

  handleInputChange = (event) => {
    this.setState({
      [event.target.name]: event.target.value,
    });
  };

  handleLogin = async () => {
    const { username, password } = this.state;

    try {
      const data = await postDataFromApi('token/', { username, password });
      this.setState({ responseData: data });

      if (data && data.token) {
        // Store the token in the AuthProvider
        AuthProvider.login(data.token);
        console.log(data.token);
        const navigate = useNavigate();
        navigate('/home');
      }
    } catch (error) {
      this.setState({ error: error });
    }
  };

  render() {
    const { responseData, error } = this.state;
    if (error) {
      return (
        <div>Error: {error.message}</div>
      );
    }

    if (!responseData) {
      return (
        <div className={styles.Login}>
          <input
            type="text"
            name="username"
            placeholder="Username"
            onChange={this.handleInputChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            onChange={this.handleInputChange}
          />
          <button onClick={this.handleLogin}>Login</button>
        </div>
      );
    }

    return (
      <div>
        {<Loged />}
      </div>
    );
  }
}

export default LogIn;
