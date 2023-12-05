import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [refresh, setRefresh] = useState(localStorage.getItem('refresh') || null);
  const [access, setAccess] = useState(localStorage.getItem('access') || null);
  const [user, setUser] = useState(localStorage.getItem('user') || null);

  const login = (newRefresh, newAccess, newUser) => {
    localStorage.setItem('refresh', newRefresh);
    localStorage.setItem('access', newAccess);
    localStorage.setItem('user', newUser);

    setRefresh(newRefresh);
    setAccess(newAccess);
    setUser(newUser);
  };

  const logout = () => {
    localStorage.removeItem('refresh');
    localStorage.removeItem('access');
    localStorage.removeItem('user');

    setRefresh(null);
    setAccess(null);
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ refresh, access, user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
