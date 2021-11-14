import './App.css';
import { useState } from 'react';
import Header from './components/Common/Header';
import { Route, Switch, Redirect } from "react-router-dom";

import HomeScreen from './screens/HomeScreen';
import EventScreen from './screens/EventScreen';
import LoginScreen from './screens/LoginScreen';
import RegisterScreen from './screens/RegisterScreen';

function App() {
  const [user, setUser] = useState();

  if (!user) {
    return (
      <div className="App">
        <Switch>
          <Route path="/login">
            <LoginScreen setUser={setUser} />
          </Route>
          <Route path="/register">
            <RegisterScreen />
          </Route>
          <Redirect exact from="/" to="/login" />
        </Switch>
      </div>

    )
  }

  return (
    <div className="App">
      <Header user={user} />
      <Switch>
        <Route path="/event/:id" component={EventScreen} />
        <Route path="/" component={HomeScreen} />
      </Switch>
    </div>
  );
}

export default App;
