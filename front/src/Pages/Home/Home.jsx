import React, { Component, Fragment } from 'react';
import { fetchDataFromApi } from '../../Services/Utils//httpClient'; // Import the reusable function
import styles from '../../Assets/Styles/Home.module.scss'
import { Outlet, Link } from 'react-router-dom';
import { FaShopify } from 'react-icons/fa';

class Home extends Component {
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
      const data = await fetchDataFromApi('products/'); // Replace with your specific path
      this.setState({ responseData: data });
    } catch (error) {
      this.setState({ error: error });
    }
  }

  render() {
    const { responseData, error } = this.state;
    if (error) {

      return (
        <div>Error: {error.message}</div>
      );
    }

    if (!responseData) {
      return <div>Loading...</div>;
    }

    // Render the component with the received data
    return (
      <div className={styles.mainDiv}>
        <div >
          <h1 >
            Look around our new stock
          </h1>
          <h4>
            <button>

              <Link to={`Products`}>
                <FaShopify /> Shop Now
              </Link>
            </button>
          </h4>
        </div>

        <div className={styles.home}>
        </div>
      </div>

    );
  }
}
export default Home;