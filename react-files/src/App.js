import React, { Component } from 'react';
import Command from './components/Command.js';
import Header from './components/Header.js';
import Content from './components/Content.js';

class App extends Component {
  constructor(props){
    super(props);
  }

  render() {
    return(
      <div>
        <Header title="Application" />
        <Content />
        <Command />
      </div>
    )
  }
}

export default App;
