import React from 'react';


export default class TutorProfile extends React.Component {

    render () {
        return (
            <div>
                
                <div class="flexContainer">
                    <div class="box-1">
                        <form id="retryForm" method="GET" action="retryTutor">
                        <input name="email" style={{display: "none"}} /><a class="button" id="noBtn" href="javascript:{}" onclick="document.getElementById('retryForm').submit();">↻</a>
                        </form>
                    </div>
                    <div class="box-2">
                        <div class="section"><img class="prof" src="https://images.unsplash.com/photo-1511367461989-f85a21fda167?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80" alt="Profile Pic" />
                        <h1>Romir Singla</h1>
                        <h4>18 years old</h4>
                        <h4>Buffalo Grove</h4>
                        <h2>I can help you with...</h2>
                        <div class="center"></div>
                        </div>
                    </div>
                    <div class="box-3">
                        <form id="submitForm" method="post" action="messageBoard">
                        <input name="newTutor" value="true" style={{display: "none"}} /><a class="button" id="yesBtn" href="javascript:{}" onclick="document.getElementById('submitForm').submit();">✔</a>
                        </form>
                    </div>
                </div>
                <form id="signupformA" action="/" method="get">
                <div class="button in-line" id="fixedButton">
                    <input type="submit" value="Return Home"/>
                </div>
                </form>
                
            </div>
        )
    }
}