import React, { Component } from 'react'
import { GoogleLogin, GoogleLogout } from 'react-google-login';
import { connect } from 'react-redux';
import { gSignIn, signOut } from '../store/actions/authActions';

const CLIENT_ID = '787660474330-srqgc8h2jbt1tuicaqrk023lpd4ai1d9.apps.googleusercontent.com';


class GoogleBtn extends Component {
   constructor(props) {
    super(props);

    this.state = {
      isLogined: false,
      user: '',
      token: ''
    };

    this.login = this.login.bind(this);
    this.handleLoginFailure = this.handleLoginFailure.bind(this);
    this.logout = this.logout.bind(this);
    this.handleLogoutFailure = this.handleLogoutFailure.bind(this);
  }

  login (response) {
    if(response.accessToken){
      this.setState(state => ({
        isLogined: true,
        user: response.profileObj,
        token: response.accessToken
      }));
    }
  }

  logout (response) {
    this.setState(state => ({
      isLogined: false,
      user: '',
      token: ''
    }));
  }

  handleLoginFailure (response) {
    alert('Failed to log in')
  }

  handleLogoutFailure (response) {
    alert('Failed to log out')
  }

  render() {
    return (
        <div className="in-line">
        { this.state.isLogined ?
            <GoogleLogout
                clientId={ CLIENT_ID }
                buttonText='Sign out'
                onLogoutSuccess={ this.logout }
                onFailure={ this.handleLogoutFailure }
            ></GoogleLogout> :
            <GoogleLogin
                clientId={ CLIENT_ID }
                buttonText='Sign in'
                onSuccess={ this.login }
                onFailure={ this.handleLoginFailure }
                cookiePolicy={ 'single_host_origin' }
                responseType='code,token'
            />
        }
        { this.state.token ? this.props.gSignIn(this.state.user, this.state.token) : this.props.signOut() }

        </div>
    )
  }
}

const mapDispatchToProps = dispatch => {
    return {
        gSignIn: (user, token) => dispatch(gSignIn(user, token)),
        signOut: () => dispatch(signOut())
    }
}

export default connect(null, mapDispatchToProps)(GoogleBtn);