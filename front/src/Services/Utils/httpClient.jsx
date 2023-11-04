import axios from 'axios';
import pathDefinition from './status';
// Create a reusable function for making GET requests
export async function fetchDataFromApi(path) {
  try {
    const apiUrl = pathDefinition(path); // Replace with your API base URL
    const response = await axios.get(apiUrl, { withCredentials: true });

    // Return the response data
    return response.data;
  } catch (error) {
    // Handle errors here
    throw error;
  }
}
