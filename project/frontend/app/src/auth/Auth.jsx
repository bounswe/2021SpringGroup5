import { createContext, useContext, useState } from 'react';
import { login as authLogin } from '../services/AuthService';

const AuthContext = createContext({
    isAuthenticated: true,
    login() {
        return Promise.resolve();
    },
});

export const Auth = (props) => {
    const { children } = props;
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    const login = (loginForm) => {
        return authLogin(loginForm).then(() => {
            setIsAuthenticated(true);
            // history.push('/'); // todo redirect to homepage after login
        });
    };

    // logout here

    return (
        <AuthContext.Provider value={{ isAuthenticated, login }}>
            {children}
        </AuthContext.Provider>
    );
};

export const useAuth = () => {
    return useContext(AuthContext);
};