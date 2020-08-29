import React from 'react';
import Paper from '@material-ui/core/Paper';
import { makeStyles } from '@material-ui/core/styles';
import { withRouter } from 'react-router-dom';
import { NavLink } from 'react-router-dom';
import Logout from './Logout'
import './CSS/Navbar.css'



const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    overflow: 'hidden',
  },
  paper: {
    padding: theme.spacing(2),
    background: '#343A40',
    border: 0,
    height: '20px',
    alignContent: 'bottom',
    borderRadius: 3,
    color: 'white',
    // width: "100vw",
  },
}));

function Navbar() {
    const classes = useStyles();

      return (
        <div className="App">
          <Paper className={classes.paper}>
          <div className="navbar-link-font link-font">
            {localStorage.usertoken && 
            <>
            <NavLink exact to='/' className="link-font" activeClassName="navbar-link-font-active">Dashboard</NavLink>
            <NavLink exact to='/students' className="link-font" activeClassName="navbar-link-font-active">Students</NavLink>
            <NavLink exact to='/add-student' className="link-font" activeClassName="navbar-link-font-active">Add Student</NavLink>
            <NavLink exact to='/profile' className="link-font" activeClassName="navbar-link-font-active">Profile</NavLink>
            <Logout />
            </>
              }

              {!localStorage.usertoken && <>
                          <NavLink exact to='/signup' className="link-font" activeClassName="navbar-link-font-active">Sign Up</NavLink>
                          <NavLink exact to='/login' className="link-font" activeClassName="navbar-link-font-active">Log In</NavLink></>
                          }

            
            
          </div>
         </Paper>
        </div>
  
        
      );
    }
    
    export default withRouter(Navbar);

