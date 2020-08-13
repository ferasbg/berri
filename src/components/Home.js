import React from 'react';
import GoogleBtn from './GoogleBtn';
import { connect } from 'react-redux';
import { signUp } from '../store/actions/authActions';
import { Redirect } from 'react-router-dom';

class Home extends React.Component {
    constructor (props) {
        super (props)
    }

    state = {}

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleSubmit = (e) => {
        e.preventDefault();
        this.props.signUp(this.state);
    }
    
    render () {
        const { authError, auth } = this.props;
        if (auth.uid) return <Redirect to='/profile' /> 
        return (
            <div>
                <div class="titleHead">
                    <h1 id="title-text">Go Berri</h1>
                    <p>Join the ever-increasing market of high school tutors today</p>
                    <div className="signin-error">
                        { authError ? <p>{ authError }</p> : null }
                    </div>
                </div>
                <div class="app" >
                    <div class="container__signup">
                        <form id="signupformA" onSubmit={this.handleSubmit} >
                            <div class="form-group"><label>First Name</label><br/><input class="form-control" id="first" onChange={this.handleChange} type="text" name="firstname" placeholder="First Name" required=" /" /></div>
                            <div class="form-group"><label>Last Name</label><br/><input class="form-control" id="last" onChange={this.handleChange} type="text" name="lastname" placeholder="Last Name" required="" /></div>
                            <div class="form-group"><label>Email</label><br/><input class="form-control" id="email" onChange={this.handleChange} type="text" name="email" placeholder="Email Address" required="" /></div>
                            <div class="form-group"><label>Password</label><br/><input class="form-control" id="password" onChange={this.handleChange} type="password" name="password" placeholder="Password" required=""/></div>
                            <div class="form-group"><label>Repeat Password</label><br/><input class="form-control" id="passwordRepeat" onChange={this.handleChange} type="password" name="passwordRepeat" placeholder="Repeat Password" required=""/></div>
                            <div class="button in-line"><input type="submit" value="Sign Up"/></div>
                            <GoogleBtn/>
                            <p>Already have an account? <a class="login-link" href="/login">Sign in</a></p>
                        </form>
                    </div>
                </div>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return { 
        authError: state.auth.authError,
        auth: state.firebase.auth
    }
}

const mapDispatchToProps = dispatch => {
    return {
        signUp: (creds) => dispatch(signUp(creds))
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Home);