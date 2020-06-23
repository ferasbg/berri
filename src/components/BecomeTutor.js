
import React from 'react';
import "./style.module.css"

export default class BecomeTutor extends React.Component {

    render () {
        return (
            <div>
                <div class="titleHead">
                <h1>Become a tutor</h1>
                <p>Become a tutor for students</p>
                </div>
                <div class="app topSpace">
                <div class="container__signup">
                    <form id="signupformA" action="saveNewTutor" method="post">
                    <div class="form-group">
                        <label for="age">Age</label><br/>
                        <input class="form-control" id="age" type="text" name="age" placeholder="Age" required="" />
                    </div>
                    <div class="form-group">
                        <label for="subjects">Subjects you can teach</label><br/>
                        <div id="output"></div>
                        <select class="chosen-select" data-placeholder="Choose subjects ..." name="subjects" multiple=""></select>
                    </div>
                    <div class="form-group">
                        <label for="email">City</label><br/>
                        <input class="form-control" id="city" type="text" name="city" placeholder="City" required="" />
                    </div>
                    <div class="button">
                        <input type="submit" value="Submit" />
                    </div>
                    <p>Want to find a tutor instead? <a href="/findTutor">Find a tutor</a></p>
                    </form>
                </div>
                </div>  
            </div>
        )
    }
}

