import './App.css';
import { Route, Switch, Redirect } from 'react-router-dom';

import HomeScreen from './screens/HomeScreen';
import EventScreen from './screens/EventScreen';
import EventDetailScreen from './screens/EventDetailScreen';
import CreateEventScreen from './screens/CreateEventScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';
import Profile from './screens/Profile';
import ParticipantsScreen from './screens/ParticipantsScreen';

import { QueryClient, QueryClientProvider } from 'react-query';
import ForgotPasswordScreen from './screens/ForgotPasswordScreen';
import SearchScreen from './screens/SearchScreen';
import AuthenticatedRoute from './auth/AuthenticatedRoute';
import { Auth } from './auth/Auth';

function App() {
  const queryClient = new QueryClient();

  //console.log(me);

  return (
    <div className="App">
      <QueryClientProvider client={queryClient}>
        <Auth>
          <Switch>
            <Route path="/login">
              <LoginScreen />
            </Route>
            <Route path="/forgot-password">
              <ForgotPasswordScreen />
            </Route>
            <Route path="/register">
              <RegisterScreen />
            </Route>

            <AuthenticatedRoute path="/event/:id" component={EventScreen} />
            <AuthenticatedRoute path="/profile" component={Profile} />
            <AuthenticatedRoute path="/search" exact component={SearchScreen} />
            <AuthenticatedRoute path="/createEvent" component={CreateEventScreen} />
            <AuthenticatedRoute path="/eventDetail/:id" component={EventDetailScreen} />
            <AuthenticatedRoute path="/eventParticipants/:id" component={ParticipantsScreen} />
            <AuthenticatedRoute path="/" exact component={HomeScreen} />

            <Redirect exact from="/" to="/login" />
          </Switch>
        </Auth>
      </QueryClientProvider>
    </div>
  );
}

export default App;
