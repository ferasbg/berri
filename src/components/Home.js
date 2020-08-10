import React from 'react';
import { GoogleLogin } from 'react-google-login';
import { connect } from 'react-redux';
import { firestoreConnect } from 'react-redux-firebase'
import { createUser } from '../store/actions/userActions';

class Home extends React.Component {
    constructor (props) {
        super (props)
        this.onSignIn = this.onSignIn.bind (this)
    }

    state = {}

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.createUser(this.state);
    }

    onSignIn (response) {
      console.log(response);
        // TODO: send login post request to backend API
    }
    
    render () {

    return (
        <div>
            <div class="titleHead">
                <h1 id="title-text">Go Berri</h1>
                <p>Join the ever-increasing market of high school tutors today</p>
            </div>
            <div class="app" >
                <div class="container__signup">
                    <form id="signupformA" onSubmit={this.handleSubmit} >
                        <div class="form-group"><label for="firstname">First Name</label><br/><input class="form-control" id="first" onChange={this.handleChange} type="text" name="firstname" placeholder="First Name" required=" /" /></div>
                        <div class="form-group"><label for="lastname">Last Name</label><br/><input class="form-control" id="last" onChange={this.handleChange} type="text" name="lastname" placeholder="Last Name" required="" /></div>
                        <div class="form-group"><label for="email">Email</label><br/><input class="form-control" id="email" onChange={this.handleChange} type="text" name="email" placeholder="Email Address" required="" /></div>
                        <div class="form-group"><label for="password">Password</label><br/><input class="form-control" id="password" onChange={this.handleChange} type="password" name="password" placeholder="Password" required=""/></div>
                        <div class="form-group"><label for="passwordRepeat">Repeat Password</label><br/><input class="form-control" id="passwordRepeat" onChange={this.handleChange} type="password" name="passwordRepeat" placeholder="Repeat Password" required=""/></div>
                        <div class="button in-line"><input type="submit" value="Sign Up"/></div>
                        <GoogleLogin
                            clientId="787660474330-srqgc8h2jbt1tuicaqrk023lpd4ai1d9.apps.googleusercontent.com"
                            buttonText="Login"
                            onSuccess={this.onSignIn}
                            onFailure={this.onSignIn}
                            cookiePolicy={'single_host_origin'}
                        />
                        <p>Already have an account? <a href="/">Sign in</a></p>
                    </form>
                </div>
                {/* <!-- form#google-form(action="googleSignup", method="post")-->
                <!--   .g-sign-in-button#google-button-->
                <!--     .content-wrapper-->
                <!--       .logo-wrapper-->
                <!--         img(src='https://developers.google.com/identity/images/g-logo.png')-->
                <!--       span.text-container -->
                <!--         span Sign up with Google--> */}
            </div>

        </div>
    )}

}

const mapDispatchToProps = dispatch => {
    return {
        createUser: (user) => dispatch(createUser(user))
    }
}

export default connect(null, mapDispatchToProps)(Home);