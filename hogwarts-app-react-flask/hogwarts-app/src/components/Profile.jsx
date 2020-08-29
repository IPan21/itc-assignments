import React, { useState, useEffect } from "react";
import { BrowserRouter as Router, Route,
  Switch,
  useParams } from 'react-router-dom'
import Paper from "@material-ui/core/Paper";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import './CSS/StudentListItem.module.css'
import { getStudentById } from '../lib/api'
import EditProfile from './EditProfile'
import EditButton from './ProfileEditButton'



const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      overflow: "hidden",
      padding: theme.spacing(0, 3),
    },
    paper: {
      maxWidth: 800,
      margin: `${theme.spacing(5)}px auto`,
      background: "#343A40",
      border: 0,
      borderRadius: 3,
      color: "white",
      padding: "30px",
    },
  }));

  
  export default function StudentListItem() {
    let { _id } = useParams();
    const [student, setStudent] = useState()
    const [clicked, setClicked] = useState(false)
    const classes = useStyles();
    const fetchData = async () => {
        let res = await getStudentById(_id);
      setStudent(res.data.result);
      console.log(res.data.result)
    };

    useEffect(() => {
        fetchData();
    }, []);



    const handleEditButton = () => {
        if (clicked) {
            fetchData()
        }

        setClicked(!clicked)
    }
  
    return (
      <div className="App">{student && <>
        {!clicked &&
        <Paper className={classes.paper}>
          <Grid container wrap="wrap" spacing={2} justify='flex-start'>

            <Grid item xs={12} >
    <Typography align="center">{student.first_name + ' ' + student.last_name}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="date-align-right">
              <Typography align="right">Existing magic skills:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography component={'span'} align="left">{student.existing_magic_skills.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="date-align-right">
              <Typography align="right">Desired magic skills:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography component={'span'} align="left">{student.desired_magic_skills.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="date-align-right">
              <Typography align="right">Interested in course:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography component={'span'} align="left">{student.interested_in_course.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>
        </Paper>}
        
        
       
        
        
        
        
        {clicked &&
        <Paper className={classes.paper}>
            <div style={{ paddingTop: '30px', paddingBottom: '30px'}}>
            <EditProfile student={student} />
            </div>
        </Paper>}
        
        <EditButton self={this} handleEditButton={handleEditButton}/>
        
        
        
        
        
        
        </>}
      </div>
    );
  }