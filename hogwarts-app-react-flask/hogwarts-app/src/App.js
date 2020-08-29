import React from 'react';
import './App.css';
import AddStudent from './components/AddStudent'
// import Profile from './components/Profile';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Navbar from "./components/Navbar"
// import AppContext from './AppContext';
// import Login from "./components/Login";
// import SignUp from "./components/SignUp";
// import SearchBar from "./components/Search";
// import { AuthProvider } from './Auth'
// import PrivateRoute from "./PrivateRoute";
// import LogOut from './components/LogOut'
// import MultipleSelect from './components/task'
import AllStudents from './components/StudentsList';
import Profile from './components/Profile';
import Dashboard from './components/Dashboard';
import Register from './components/Register'
import Login from './components/Login'
import UserProfile from './components/UserProfile';



function App() {
  return (

    <Router>
      
      <div className="App">
      <Navbar />
    <header className="App-header">

      <Switch>
        <Route exact path="/" component={Dashboard} />
        <Route path="/students" component={AllStudents} />
        <Route path="/add-student" component={AddStudent} />
        <Route path="/profile/:_id" component={Profile} />
        <Route exact path="/profile" component={UserProfile} />
   
        <Route path="/login" component={Login} />
      <Route path="/signup" component={Register} />
      {/* <Route path="/" component={Main} /> */}
      </Switch>
      </header>
  </div>

    </Router>

  );
}


export default App;
