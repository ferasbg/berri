import React from 'react';
import { GoogleLogin } from 'react-google-login';


export default class Login extends React.Component {

    render () {
        return (
            <div>

                {/* <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie-edge">
                    <title></title>
                    <meta name="google-signin-client_id" content="787660474330-srqgc8h2jbt1tuicaqrk023lpd4ai1d9.apps.googleusercontent.com">
                    <script src="https://apis.google.com/js/platform.js" async defer></script>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                    <link rel="stylesheet" type="text/css" href="css/style.css">
                    <link href="https://fonts.googleapis.com/css?family=Roboto:300,400,500,700" rel="stylesheet" type="text/css">
                    <title>Sign Up for Berri</title>
                </head> */}
                <div className="titleHead">
                    <h1>Berri</h1>
                    <p>Problem-Solving Doesn't Have to Be So Complicated While at Home. Introducing, Berri.</p>
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
                <style jsx global> {`
                    body {
                        background: rgb(255, 255, 255);
                        font-family: Roboto;
                        overflow: visible;
                    }

                    .titleHead {
                        padding-top: 20px;
                        padding-left: 50px;
                        width: 40%;
                        float: left;
                        font-size: 50px;
                    }

                    .app {
                        background: rgb(253, 145, 145);
                        height: auto;
                        width: 50%;
                        margin: auto;
                        position: absolute;
                        right: 50px;
                        overflow: visible;
                        box-shadow: 0 20px 30px rgba(0, 0, 0, 0.24);
                        border-radius: 10px;
                        top: 10px;
                    }

                    .topSpace {
                        top: 60px;
                    }

                    .centerForm {
                        background: white;
                        position: relative;
                        margin: auto;
                        width: 80%;
                        top: 0px;
                        left: 0px;
                        right: 0px;
                        bottom: 0px;
                        transform: translateY(30%);
                        box-shadow: 0 0 0 rgba(0, 0, 0, 0.24);
                    }

                    .container__signup {
                        color: #fff;
                        padding: 2.5rem;
                        border-radius: 25px;
                    }

                    .form-group {
                        width: 100%;
                        margin: left;
                        position: relative;
                        text-align: start;
                        transition: .3s .6s;
                        padding-top: 20px;
                    }

                    label {
                        text-transform: uppercase;
                        padding-left: 2px;
                        font-weight: 400;
                    }

                    label[for=subject] {
                        color: black;
                        font-weight: 300;
                        font-size: 80px;
                    }

                    select {
                        width: 90%;
                    }

                    .form-control {
                        border-top: 0;
                        border-right: 0;
                        border-left: 0;
                        border-radius: 8px;
                        border-bottom: rgb(226, 108, 108);
                    }

                    input[type=text] {
                        display: inline-block;
                        background: #F9F9F9;
                        width: 80%;
                        margin: 15px auto;
                        border-radius: 8px;
                        border: 0;
                        padding: 12px 0;
                        outline: 0;
                        font-size: 15px;
                        padding-left: 10px;
                    }

                    input[type=password] {
                        display: inline-block;
                        background: #F9F9F9;
                        width: 80%;
                        margin: 15px auto;
                        border: 0;
                        border-bottom: 1px solid lightgrey;
                        border-radius: 8px;
                        padding: 12px 0;
                        outline: 0;
                        font-size: 15px;
                        padding-left: 10px;
                    }

                    .button {
                        position: relative;
                        box-shadow: 0 3px 12px rgba(0, 0, 0, 0.23), 0 3px 12px rgba(0, 0, 0, 0.16);
                        height: 56px;
                        width: 120px;
                        border-radius: 28px;
                        font-weight: 1000;
                        font-size: 20px;
                        cursor: pointer;
                        /*transition: .3s .7s, background .1s .3s;*/
                    }

                    .button input[type=submit] {
                        position: absolute;
                        top: 0;
                        bottom: 0;
                        width: 100%;
                        border: 0px;
                        border-radius: 28px;
                        font: 1000 20px Roboto;
                        background: white;
                        color: rgb(253, 145, 145);
                        cursor: pointer;
                    }

                    .in-line {
                        display: inline-block;
                        vertical-align: middle;
                    }

                    .topRight {
                        display: inline-block;
                        vertical-align: right;
                    }

                    *,
                    *:before,
                    *:after {
                        box-sizing: border-box;
                    }

                    .g-signin2 {
                        margin-left: 20px;
                    }


                    /*.g-sign-in-button {
                        margin: 10px;
                        display: inline-block;
                        width: 240px;
                        height: 50px;
                        background-color: #4285f4;
                        color: #fff;
                        border-radius: 1px;
                        box-shadow: 0 2px 4px 0 rgba(0, 0, 0, .25);
                        transition: background-color 0.218s, border-color 0.218s, box-shadow 0.218s;
                    }
                    .g-sign-in-button:hover {
                        cursor: pointer;
                        -webkit-box-shadow: 0 0 3px 3px rgba(66, 133, 244, .3);
                        box-shadow: 0 0 3px 3px rgba(66, 133, 244, .3);
                    }
                    .g-sign-in-button:active {
                        background-color: #3367d6;
                        transition: background-color 0.2s;
                    }
                    .g-sign-in-button .content-wrapper {
                        height: 100%;
                        width: 100%;
                        border: 1px solid transparent;
                    }
                    .g-sign-in-button img {
                        width: 18px;
                        height: 18px;
                    }
                    .g-sign-in-button .logo-wrapper {
                        padding: 15px;
                        background: #fff;
                        width: 48px;
                        height: 100%;
                        border-radius: 1px;
                        display: inline-block;
                    }
                    .g-sign-in-button .text-container {
                        font-family: Roboto, arial, sans-serif;
                        font-weight: 500;
                        letter-spacing: 0.21px;
                        font-size: 16px;
                        line-height: 48px;
                        vertical-align: top;
                        border: none;
                        display: inline-block;
                        text-align: center;
                        width: 180px;
                    }
                    .google__signup__button {
                        /* background: transparent; 
                        width: 100%;
                        height: 100%;
                        border: none !important;
                        font-size: 0;
                        padding-bottom: 10px;
                    }
                    */

                    .no__style {
                        all: revert;
                    }

                `} </style>

            </div>
        )
    }
}