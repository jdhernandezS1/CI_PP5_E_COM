import React, { Component } from 'react';
import { postDataFromApi } from '../../Services/Utils/postDataClient'; // Import the reusable function
import { useNavigate } from 'react-router-dom';

class Loged extends Component {
    constructor(props) {
        super(props);
        
        this.state = {
            username: '',
            password: '',
            responseData: null,
            error: null,
        };
    }

    render() {
        const { responseData, error } = this.state;

        return (
            <div>
                Loged successful
            </div>
        );
    }
}

export default Loged;
