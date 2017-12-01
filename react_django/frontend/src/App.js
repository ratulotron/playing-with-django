import React, { Component } from 'react';
import { login, loggedIn } from './util/Auth';
import store from './store';
import logo from './logo.svg';
import './App.css';
import createFragment from 'react-addons-create-fragment'; // ES6



class App extends Component {
    render() {
        login("admin", "nothing1234");
        var status = loggedIn();
        return (<div className="App" >
            <div className="App-header" >
                <img src={logo}
                    className="App-logo"
                    alt="logo" />
                <h2> Welcome to React </h2> 
            </div> 
            <p className="App-intro" > {
                            // To get started, edit <code>src/App.js</code> and save to reload.
                        } 
                <p> Logged in ? {status} </p>

            </p> 
            </div>
        );
    }
}

export default App;