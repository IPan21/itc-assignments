import React from "react";
import Paper from "@material-ui/core/Paper";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
// import './CSS/StudentListItem.module.css'
import { Link } from 'react-router-dom';




const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      overflow: "hidden",
      padding: theme.spacing(0, 3),
    },
    paper: {
      minWidth: '50vw',
      maxWidth: 400,
      margin: `${theme.spacing(5)}px auto`,
      background: "#343A40",
      border: 0,
      borderRadius: 3,
      color: "white",
      padding: "30px",
    },
  }));

  
  export default function StudentListItem(props) {
    const { first_name, last_name, existing_magic_skills, desired_magic_skills, interested_in_course, student_id } = props;
    const classes = useStyles();
    const linkpath = '/profile/' + student_id
  
    return (
      <>
        <Paper className={classes.paper}>
          <Grid container wrap="wrap" spacing={2}  justify='flex-start'>

            <Grid item xs={12}>
    <Typography align="center">{first_name + ' ' + last_name}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="username-link">
              <Typography align="right" className="date-align-right">Existing magic skills:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography  component={'span'} align="left">{existing_magic_skills.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="date-align-right">
              <Typography align="right">Desired magic skills:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography  component={'span'} align="left">{desired_magic_skills.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="nowrap" spacing={2}>
            <Grid item xs={6}>
                 <div className="date-align-right">
              <Typography align="right">Interested in course:</Typography>
               </div>
            </Grid>
            <Grid item xs={6}>
                <Typography  component={'span'} align="left">{interested_in_course.map((item, index) => <div key={index}>{item}</div>)}</Typography>
            </Grid>
          </Grid>

          <Grid container wrap="wrap" spacing={2}  justify='flex-start'>

<Grid item xs={12}>
<Typography align="left"><Link to={linkpath} className="username-link">Go to profile</Link></Typography>
</Grid>
</Grid>



        </Paper>
      </>
    );
  }

