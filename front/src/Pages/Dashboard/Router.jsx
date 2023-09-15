import React from 'react';
import { BrowserRouter, Routes, Route, useParams } from "react-router-dom";
import Index from './Index';
import ContactUs from '../ContactUs/ContactUs';
import Products from '../Products/Products';
import Product from '../Products/ProductId';
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
          <Route path="Products">
            <Route index element={<Products />}/>
            <Route path=":id" element={<Product />} />
          </Route>
          <Route path="*" element={<Error />} />
        </Route>
      </Routes>
    </BrowserRouter>

  );
}

export default Router;