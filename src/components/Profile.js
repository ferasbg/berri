import React from 'react';
import { connect } from 'react-redux';

class Profile extends React.Component {
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
                        <p class="profile-p">Looks like you aren't a tutor yet!</p><a class="button" id="becomeTutor" href="/becomeTutor">Become a Tutor</a>
                        </div>
                        <div id="yesContent">
                        <div id="yourSubjects">Your Subjects</div>
                        <div id="subjects"></div>
                        <div id="status"></div>
                        <form id="toggleStatus" method="post" action="toggleActiveStatus">
                            <div class="button">
                            <input type="submit" value="Toggle"/>
                            </div>
                        </form>
                        </div>
                    </div>
                    </div>
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
                        </form>
                        </div>
                    </div>
                    </div>
                </div>
                <form id="signupformA" action="logout" method="post">
                    <div class="button" id="fixedButton">
                    <input type="submit" value="Logout"/>
                    </div>
                </form>
                <form id="newPfpForm" action="newPfp" method="post" style={{display: "none"}} enctype="multipart/form-data">
                <input id="myFile" type="file" name="pfp"/>
                </form>
            </div>
        )
    }
}

const mapStateToProps = (state) => {
    return {
        projects: state.project.projects
    }
}

export default connect(mapStateToProps)(Profile);