import React from 'react';
<<<<<<< HEAD
import { connect } from 'react-redux';
import { firestoreConnect } from 'react-redux-firebase'
import { signOut } from '../store/actions/authActions';
import { Redirect } from 'react-router-dom';

class Profile extends React.Component {
    render () {
        const { auth } = this.props;
        if (!auth.uid) return <Redirect to='/login' /> 
        return (
            <div>
                <div className="row">
                    <div className="box-1">
                    <div className="imageSection circleCrop verticalAlign"><img className="circleCrop" id="prof" src='https://i.pinimg.com/originals/2e/2f/ac/2e2fac9d4a392456e511345021592dd2.jpg' alt="Profile Pic" /*onClick={ newProfPic() }*/ />
                        <div className="overlay circleCrop" /*onClick={ newProfPic() }*/ >
                        <div id="pfpText" /*onClick={ newProfPic() }*/ >Change Profile Picture</div>
                        </div>
                    </div>
                    </div>
                    <div className="box-2">
                    <div className="section" id="headerSection">
                        <div className="heading">Hello,    </div>
                        <form id="accessMessageBoard" method="post" action="messageBoard">
                        <input name="newTutor" style={{display: "none"}}/>
                        </form>
                        <div className="imgContainer circleCrop"><img src="https://i.postimg.cc/W4dRsw-RV/speech-bubble.png" /*onClick={ document.getElementById('accessMessageBoard').submit() }*/ /></div>
                    </div>
                    </div>
                </div>
                <div className="row">
                    <div className="box-3">
                    <div className="section" id="sect3">
                        <div id="noContent">
                        <p className="profile-p">Looks like you aren't a tutor yet!</p><a className="button" id="becomeTutor" href="/becomeTutor">Become a Tutor</a>
=======

export default class Profile extends React.Component {

    render () {
        return (
            <div>
                <div class="row">
                    <div class="box-1">
                    <div class="imageSection circleCrop verticalAlign"><img class="circleCrop" id="prof" src='https://i.pinimg.com/originals/2e/2f/ac/2e2fac9d4a392456e511345021592dd2.jpg' alt="Profile Pic" onclick="newProfPic()"/>
                        <div class="overlay circleCrop" onclick="newProfPic()">
                        <div id="pfpText" onclick="newProfPic()">Change Profile Picture</div>
                        </div>
                    </div>
                    </div>
                    <div class="box-2">
                    <div class="section" id="headerSection">
                        <div class="heading">Hello,    </div>
                        <form id="accessMessageBoard" method="post" action="messageBoard">
                        <input name="newTutor" style={{display: "none"}}/>
                        </form>
                        <div class="imgContainer circleCrop"><img src="https://i.postimg.cc/W4dRsw-RV/speech-bubble.png" onclick="document.getElementById('accessMessageBoard').submit()"/></div>
                    </div>
                    </div>
                </div>
                <div class="row">
                    <div class="box-3">
                    <div class="section" id="sect3">
                        <div id="noContent">
                        <p>Looks like you aren't a tutor yet!</p><a class="button" id="becomeTutor" href="/becomeTutor">Become a Tutor</a>
>>>>>>> POC-1
                        </div>
                        <div id="yesContent">
                        <div id="yourSubjects">Your Subjects</div>
                        <div id="subjects"></div>
                        <div id="status"></div>
                        <form id="toggleStatus" method="post" action="toggleActiveStatus">
<<<<<<< HEAD
                            <div className="button">
=======
                            <div class="button">
>>>>>>> POC-1
                            <input type="submit" value="Toggle"/>
                            </div>
                        </form>
                        </div>
                    </div>
                    </div>
<<<<<<< HEAD
                    <div className="box-4">
                    <div className="section column">
                        <div className="col-1">
                        <form id="subjectForm" method="GET" action="foundTutors">
                            <div className="dropdown">
                            <input className="greyBubble" id="chooseSubject" type="text" name="chosenSubject" placeholder="What do you need help with?" autoComplete="off"/>
                            <div id="dropdownContent"></div>
                            </div>
                            <input className="greyBubble" type="submit" value="→"/>
                        </form>
                        </div>
                        <div className="col-2">
                        <div className="heading">...or search tutors by</div>
                        <form id="searchForm" method="get" action="searchTutor">
                            <input className="greyBubble" id="searchEmails" type="text" name="searchTutor" placeholder="email"/>
=======
                    <div class="box-4">
                    <div class="section column">
                        <div class="col-1">
                        <form id="subjectForm" method="GET" action="foundTutors">
                            <div class="dropdown">
                            <input class="greyBubble" id="chooseSubject" type="text" name="chosenSubject" placeholder="What do you need help with?" autocomplete="off"/>
                            <div id="dropdownContent"></div>
                            </div>
                            <input class="greyBubble" type="submit" value="→"/>
                        </form>
                        </div>
                        <div class="col-2">
                        <div class="heading">...or search tutors by</div>
                        <form id="searchForm" method="get" action="searchTutor">
                            <input class="greyBubble" id="searchEmails" type="text" name="searchTutor" placeholder="email"/>
>>>>>>> POC-1
                        </form>
                        </div>
                    </div>
                    </div>
                </div>
<<<<<<< HEAD
                <button className="button" id="fixedButton" onClick={ this.props.signOut }>Logout</button>
                <form id="newPfpForm" action="newPfp" method="post" style={{display: "none"}} encType="multipart/form-data">
                <input id="myFile" type="file" name="pfp"/>
                </form>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        auth: state.firebase.auth
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        signOut: () => dispatch(signOut())
    }
}

export default connect(mapStateToProps, mapDispatchToProps)(Profile);
=======
                <form id="signupformA" action="logout" method="post">
                    <div class="button" id="fixedButton">
                    <input type="submit" value="Logout"/>
                    </div>
                </form>
                <form id="newPfpForm" action="newPfp" method="post" style={{display: "none"}} enctype="multipart/form-data">
                <input id="myFile" type="file" name="pfp"/>
                </form>

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

                    .formGroup {
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

                    .formControl {
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

                    .inLine {
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
>>>>>>> POC-1
