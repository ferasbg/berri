import React from 'react';
import { connect } from 'react-redux';
import { signIn } from '../store/actions/authActions';
import GoogleBtn from './GoogleBtn';
import { Redirect } from 'react-router-dom';

class Login extends React.Component {
    state = {}

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.signIn(this.state);
    }

    render () {
        const { auth } = this.props;
        if (auth.uid) return <Redirect to='/profile' /> 
        return (
            <div>
                <div className="titleHead">
                    <h1>Go Berri</h1>
                    <p>Join the ever-increasing market of high school tutors today</p>
                </div>
                <div className="app topSpace">
                    <div className="container__signup">
                        <form id="signupformA" onSubmit={this.handleSubmit} >
                            <div className="form-group"><label>Email</label><br/><input className="form-control" id="email" onChange={this.handleChange} type="text" name="email" placeholder="Email Address" required=""/></div>
                            <div className="form-group"><label>Password</label><br/><input className="form-controlawdawd" id="password" onChange={this.handleChange} type="password" name="password" placeholder="Password" required=""/></div>
                            <div className="button in-line" id="login"><input type="submit" value="Login"/></div>
                            <GoogleBtn />
                            <p>Don't have an account? <a className="login-link" href="/signup">Sign up now!</a></p>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        auth: state.firebase.auth
    }
}

const mapDispatchToProps = dispatch => {
    return {
        signIn: (creds) => dispatch(signIn(creds))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Login);