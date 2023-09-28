import React from 'react';
import { HashRouter, Routes, Route, useParams } from "react-router-dom";
import Index from './Index';
import ContactUs from '../ContactUs/ContactUs';
import Products from '../Products/Products';
import Product from '../Products/ProductId';
import Courses from '../Courses/Courses';
import Home from '../Home/Home';
import Error from '../Error/Error';
import Auth from '../Auth/LogIn';
import LogOut from '../Auth/Logout';
function Router() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Index />}>
          <Route index element={<Home />} />
          <Route path="courses" element={<Courses />} />
          <Route path="contactUs" element={<ContactUs />} />
          <Route path="products">
            <Route index element={<Products />} />
            <Route path=":id" element={<Product />} />
          </Route>
          <Route path="auth" >
            <Route path="login" element={<Auth />} />
            <Route path="logout" element={<LogOut />} />
          </Route>
          <Route path="*" element={<Error />} />
        </Route>
      </Routes>
    </HashRouter>

  );
}

export default Router;