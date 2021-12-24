import { Route } from 'react-router-dom';
import { useEffect } from 'react';
import { useAuth } from './Auth';
import Header from '../components/Common/Header';

const AuthenticatedRoute = ({ component, ...rest }) => {
  const { isAuthenticated, refresh, loading, me } = useAuth();
  useEffect(() => {
    if (!isAuthenticated) {
      refresh();
    }
  }, [isAuthenticated, refresh]);

  if (loading) return <div>Loading</div>;

  return (
    <>
      <Header user={me} />
      <Route {...rest} component={component} />
    </>
  );
};

export default AuthenticatedRoute;
