import './App.css';
import Header from './components/Common/Header';
import { Route, Switch } from "react-router-dom";

import HomeScreen from './screens/HomeScreen';
import EventScreen from './screens/EventScreen';

function App() {
  return (
    <div className="App">
      <Header />
      <Switch>
        <Route path="/event/:id" component={EventScreen} />
        <Route path="/" component={HomeScreen} />
      </Switch>
    </div>
  );
}

export default App;
