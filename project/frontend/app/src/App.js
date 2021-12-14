import './App.css';
import { useState } from 'react';
import Header from './components/Common/Header';
import { Route, Switch, Redirect } from 'react-router-dom';

import HomeScreen from './screens/HomeScreen';
import EventScreen from './screens/EventScreen';
import EventDetailScreen from './screens/EventDetailScreen';
import CreateEventScreen from './screens/CreateEventScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import Profile from './screens/Profile';

import { QueryClient, QueryClientProvider } from 'react-query';
import ForgotPasswordScreen from './screens/ForgotPasswordScreen';
import SearchScreen from './screens/SearchScreen';

function App() {
  const [user, setUser] = useState(true);
  const queryClient = new QueryClient();

  return (
    <div className="App">
      <QueryClientProvider client={queryClient}>
        {user && (
          <>
            <Header user={user} />
            <Switch>
              <Route path="/event/:id" component={EventScreen} />
              <Route path="/profile" component={Profile} />
              <Route path="/search" component={SearchScreen} />
              <Route path="/createEvent" component={CreateEventScreen} />
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
            <Route path="/profile">
              <Profile />
            </Route>
            <Redirect exact from="/" to="/login" />
          </Switch>
        )}
      </QueryClientProvider>
    </div>
  );
}

export default App;
