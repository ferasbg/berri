import React from 'react';

import styles from "./style.module.css"

export default class Login extends React.Component {

    render () {
        return (
            <div>
                <div class="section">
                    <div class="box-1">
                        <div id="searchMenu">
                            <input type="text" name="search" placeholder="Search you chats..." autocomplete="off"/>
                        </div>
                        <div class="head"> 
                            <h2>YOUR TUTORS</h2>
                        </div>
                        <div id="yourTutors"></div>
                        <div class="head"> 
                            <h2>YOUR STUDENTS</h2>
                        </div>
                        <div id="yourStudents"></div>
                    </div>
                    <div class="box-2">
                        <div class="chat-header">
                            <img class="circleCrop" id="imgHeading" alt="Profile Pic"/>
                            <h5 id="chatHeading"></h5>
                            <div id="callButtons">
                                <button id="startButton">Start</button>
                                <button id="callButton">Call</button>
                                <button id="hangupButton">Hang Up</button>
                            </div>
                        </div>
                        <div class="chatMessages"></div>
                        <div class="chat-form-container">
                        <form id="chat-form">
                            <input id="textmsg" type="text" name="chat" placeholder="Aa" autocomplete="off"/>
                            <input id="send" type="submit" value="↑"/>
                        </form>
                        </div>
                    </div>
                    </div>
                    <form id="signupformA" action="/" method="get">
                    <div class="button in-line" id="fixedButton">
                        <input type="submit" value="Return Home"/>
                    </div>
                    </form>
                    <div id="videos">
                    <video id="localVideo" autoplay playsinline></video>
                    <video id="remoteVideo" autoplay playsinline></video>
                    </div>
                    <p class="hidden" id="userData"></p>
                    <p class="hidden" id="tutorChatData"></p>
                    <p class="hidden" id="studentChatData"></p>
            </div>
        )
    }
}