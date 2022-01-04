import { createContext, useContext, useRef, useState } from 'react';
import {
  login as authLogin,
  me as authMe,
  refresh as authRefresh,
  logout as authLogout,
} from '../services/AuthService';
import { useQuery } from 'react-query';
import { useHistory } from 'react-router-dom';

const AuthContext = createContext({
  isAuthenticated: true,
  login() {
    return Promise.resolve();
  },
  loading: false,
  logout: () => { },
  refresh: () => { },
  me: undefined,
});

export const Auth = props => {
  const { children } = props;
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [loading, setLoading] = useState(true);
  const { data: me } = useQuery('me', authMe, { enabled: isAuthenticated });
  const history = useHistory();

  const login = loginForm => {
    return authLogin(loginForm).then(() => {
      setIsAuthenticated(true);
      setLoading(false);
      history.push('/'); // todo redirect to homepage after login
    });
  };

  const refresh = useRef(() => {
    authRefresh()
      .then(() => {
        setIsAuthenticated(true);
        setLoading(false);
        setTimeout(() => {
          refresh.current();
        }, 15 * 60000);
      })
      .catch(error => {
        history.push('/login');
        setLoading(false);
        setIsAuthenticated(false);
      });
  });

  const logout = () => {
    setIsAuthenticated(false);
    history.push('/login');
  };

  return (
    <AuthContext.Provider
      value={{
        isAuthenticated: isAuthenticated,
        login: login,
        me: me,
        logout: logout,
        refresh: refresh.current,
        loading: loading,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  return useContext(AuthContext);
};
