import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Index from './Index';
import ContactUs from '../ContactUs/ContactUs';
import Products from '../Products/Products';
import Courses from '../Courses/Courses';
import Home from '../Home/Home';
import Error from '../Error/Error';

function Router() {
  return (
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Index />}>
            <Route index element={<Home />} />
            <Route path="Courses" element={<Courses />} />
            <Route path="ContactUs" element={<ContactUs />} />
            <Route path="Products" element={<Products />} />
            <Route path="*" element={<Error />} />
          </Route>
        </Routes>
      </BrowserRouter>
      
  );
}

export default Router;