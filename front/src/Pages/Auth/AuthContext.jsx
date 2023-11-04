import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function AuthProvider({ children }) {
  var [refresh, setRefresh] = useState(null);
  var [access, setAccess] = useState(null);
  var [user, setUser] = useState(null);
  const login = (newRefres, newAccess, newUser) => {

    setRefresh(newRefres);
    setAccess(newAccess);
    setUser(newUser);
  };

  const logout = () => {
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
