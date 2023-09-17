import React, { Component } from 'react';
import { fetchDataFromApi } from '../../Services/Utils//httpClient'; // Import the reusable function

class ContactUs extends Component {
  constructor(props) {
    super(props);

    this.state = {
      responseData: null,
      error: null,
    };
  }

  async componentDidMount() {
    try {
      // Use the fetchDataFromApi function to make a GET request
      const data = await fetchDataFromApi('users/'); // Replace with your specific path
      this.setState({ responseData: data });
    } catch (error) {
      this.setState({ error: error });
    }
  }

  render() {
    const { responseData, error } = this.state;

    if (error) {
      return <div>Error: {error.message}</div>;
    }

    if (!responseData) {
      return <div>Loading...</div>;
    }

    // Render the component with the received data
    return (
      <div>
        <h1>Data</h1>
        {responseData.map((item) => (
          <li key={item.id}>{item.email}</li>
        ))}
      </div>
    );
  }
}

export default ContactUs;
