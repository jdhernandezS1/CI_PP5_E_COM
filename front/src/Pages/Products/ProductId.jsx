import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { fetchDataFromApi } from '../../Services/Utils/httpClient'; // Import the reusable function
import styles from '../../Assets/Styles/Products.module.scss';

function Product() {
  const { id } = useParams(); // Access the 'id' parameter from the URL
  const [responseData, setResponseData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchData() {
      try {
        // Use the fetchDataFromApi function to make a GET request
        const data = await fetchDataFromApi(`products/${id}`); // Use the 'id' parameter
        setResponseData(data);
      } catch (error) {
        setError(error);
      }
    }

    fetchData();
  }, [id]);

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
      <h1>Product:</h1>
      <ul className={styles.ProductsGrid}>
          <li key={responseData.id} className={styles.ProductCard}>
            {/* {responseData.category} */}
            {/* {responseData.price} */}
            {/* {responseData.scount} */}
            <div>
                <picture className={styles.ProductPicture}>
                    <img src={`https://res.cloudinary.com/djvwk7zf2/${responseData.featured_image}`} alt={responseData.slug_title} className={styles.ProductImage} />
                  </picture>
            </div>
            <div className={styles.ProductDescription}>
              {responseData.title}
              <p>Remains: {responseData.quantity}</p>
              <p>{responseData.description}</p>
            </div>
            {/* {responseData.scountbool} */}
          </li>
      </ul>
    </div>
  );
}

export default Product;
