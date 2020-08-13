import React from 'react';
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
                        </div>
                        <div id="yesContent">
                        <div id="yourSubjects">Your Subjects</div>
                        <div id="subjects"></div>
                        <div id="status"></div>
                        <form id="toggleStatus" method="post" action="toggleActiveStatus">
                            <div className="button">
                            <input type="submit" value="Toggle"/>
                            </div>
                        </form>
                        </div>
                    </div>
                    </div>
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
                        </form>
                        </div>
                    </div>
                    </div>
                </div>
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