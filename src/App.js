import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';

import Home from "./components/Home"
import Login from "./components/Login"
import Profile from "./components/Profile"
import TutorProfile from "./components/TutorProfile"
import BecomeTutor from "./components/BecomeTutor"
import MessageBoard from "./components/MessageBoard"

export default class App extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <div className="App">
            <Switch>
              <Route path="/" component={Login} exact/>
              <Route path="/signup" component={Home} exact/>
              <Route path="/profile" component={Profile} exact/>
              <Route path="/tutor-profile" component={TutorProfile} exact/>
              <Route path="/become-tutor" component={BecomeTutor} exact/>
              <Route path="/messages" component={MessageBoard} exact/>
            </Switch>
        </div> 
      </BrowserRouter>
    );
  }
}
