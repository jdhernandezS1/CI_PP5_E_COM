import React, { Component } from 'react';
import { postDataFromApi } from '../../Services/Utils/postDataClient'; // Import the reusable function
import { useNavigate } from 'react-router-dom';
import Loged from './Loged'; // Import useNavigate

class Auth extends Component {
  constructor(props) {
    super(props);

    this.state = {
      username: '',
      password: '',
      responseData: null,
      error: null,
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
      // Replace 'token/' with the actual endpoint for authentication
      const data = await postDataFromApi('token/', { username, password });
      this.setState({ responseData: data });

      // Check if the authentication was successful
      if (data && data.token) {
        // Use the navigate function to redirect to a new route
        const navigate = useNavigate();
        navigate('/home'); // Replace with the desired redirect route
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
        <div>
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

    // Render the component with the received data (if needed)
    return (
      <div>
        {<Loged/>}
      </div>
    );
  }
}

export default Auth;
