import React from 'react';
import { GoogleLogin } from 'react-google-login';


export default class Login extends React.Component {
    render () {
        return (
            <div>
                <div className="titleHead">
                    <h1>Go Berri</h1>
                    <p>Join the ever-increasing market of high school tutors today</p>
                </div>
                <div className="app topSpace">
                    <div className="container__signup">
                        <form id="signupformA" action="loginAuth" method="post">
                            <div className="form-group"><label for="email">Email</label><br/><input className="form-control" id="email" type="text" name="email" placeholder="Email Address" required=""/></div>
                            <div className="form-group"><label for="password">Password</label><br/><input className="form-controlawdawd" id="password" type="password" name="password" placeholder="Password" required=""/></div>
                            <div className="button in-line" id="login"><input type="submit" value="Login"/></div>
                            <GoogleLogin
                                clientId="787660474330-srqgc8h2jbt1tuicaqrk023lpd4ai1d9.apps.googleusercontent.com"
                                buttonText="Login"
                                onSuccess={this.onSignIn}
                                onFailure={this.onSignIn}
                                cookiePolicy={'single_host_origin'}
                            />
                            <p>Don't have an account? <a href="/signup">Sign up now!</a></p>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}