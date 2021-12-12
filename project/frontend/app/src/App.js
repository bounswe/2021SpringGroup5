import './App.css';
import { useState } from 'react';
import Header from './components/Common/Header';
import { Route, Switch, Redirect } from 'react-router-dom';

import HomeScreen from './screens/HomeScreen';
import EventScreen from './screens/EventScreen';
import EventDetailScreen from './screens/EventDetailScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import CreateEvent from './screens/CreateEventScreen';
import { QueryClient, QueryClientProvider } from 'react-query';
import ForgotPasswordScreen from './screens/ForgotPasswordScreen';

function App() {
  const [user, setUser] = useState();
  const queryClient = new QueryClient();

  return (
    <div className="App">
      <QueryClientProvider client={queryClient}>
        {user && (
          <>
            <Header user={user} />
            <Switch>
              <Route path="/event/:id" component={EventScreen} />
              <Route path="/createEvent" component={CreateEvent} />
              <Route path="/eventDetail/:id" component={EventDetailScreen} />
              <Route path="/" component={HomeScreen} />
            </Switch>
          </>
        )}
        {!user && (
          <Switch>
            <Route path="/login">
              <LoginScreen setUser={setUser} />
            </Route>
            <Route path="/forgot-password">
              <ForgotPasswordScreen />
            </Route>
            <Route path="/register">
              <RegisterScreen />
            </Route>
            <Redirect exact from="/" to="/login" />
          </Switch>
        )}
      </QueryClientProvider>
    </div>
  );
}

export default App;
