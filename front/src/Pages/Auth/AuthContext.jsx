import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  var [refresh, setRefresh] = useState(null);
  var [access, setAccess] = useState(null);
  const login = (newRefres, newAccess) => {
    setRefresh(newRefres);
    setAccess(newAccess);
  };

  const logout = () => {
    setRefresh(null);
    setAccess(null);
  };

  return (
    <AuthContext.Provider value={{ refresh, access, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  return useContext(AuthContext);
}
