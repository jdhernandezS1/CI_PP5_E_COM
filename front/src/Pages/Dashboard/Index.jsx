import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import NavigationBar from './NavigationBar';
import ContactUs from '../ContactUs/ContactUs';
import Products from '../Products/Products';
import Courses from '../Courses/Courses';
import Home from '../Home/Home';
import Error from '../Error/Error';
import Footer from './Footer';
function Index() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<NavigationBar />}>
          <Route index element={<Home />} />
          <Route path="Courses" element={<Courses />} />
          <Route path="ContactUs" element={<ContactUs />} />
          <Route path="Products" element={<Products />} />
          <Route path="*" element={<Error />} />
        </Route>
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default Index;