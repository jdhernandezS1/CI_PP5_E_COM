import React, { Component } from 'react';
import { fetchDataFromApi } from '../../Services/Utils//httpClient'; // Import the reusable function
import styles from '../../Assets/Styles/Products.module.scss'

class Products extends Component {
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
      <div>
        <h1>Stock:</h1>
        <ul className={styles.ProductsGrid}>
            {responseData.map((item) => (
              <li key={item.id} className={styles.ProductCard}>
                {/* {item.category} */}
                {/* {item.price} */}
                {/* {item.scount} */}
                <div>
                  <picture className={styles.ProductPicture}>
                    <img src={`https://res.cloudinary.com/djvwk7zf2/${item.featured_image}`} alt={item.slug_title}  className={styles.ProductImage}/>
                  </picture>
                </div>
                <div className={styles.ProductDescription}>
                  {item.title}
                <p>Remains: {item.quantity}</p>
                <p>{item.description}</p>
                </div>
                {/* {item.scountbool} */}

              </li>
            ))}
        </ul>
      </div >
    );
  }
}
export default Products;