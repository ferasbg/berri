import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import './App.css';

import Home from "./components/Home"
import Login from "./components/Login"
import Profile from "./components/Profile"
import TutorProfile from "./components/TutorProfile"
import BecomeTutor from "./components/BecomeTutor"
import MessageBoard from "./components/MessageBoard"

function App() {
  return (
    <BrowserRouter>
      <div>
          <Switch>
            <Route path="/" component={Login} exact/>
            <Route path="/signup" component={Home} exact/>
            <Route path="/profile" component={Profile} exact/>
            <Route path="/tutorProfile" component={TutorProfile} exact/>
            <Route path="/becomeTutor" component={BecomeTutor} exact/>
          </Switch>
      </div> 
    </BrowserRouter>
  );
}

export default App;
