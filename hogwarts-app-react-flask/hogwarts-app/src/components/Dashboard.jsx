
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import PieChart from "./PieChart"
import React from "react";
import StudentDashItem from './StudentDashItem'
import DatePicker from './DatePicker'
// import { BrowserRouter as Router, Route, Switch, useParams } from 'react-router-dom'


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
      marginTop: "20px",
    padding: theme.spacing(2),
    textAlign: "center",
    // color: theme.palette.text.secondary,
    background: '#343A40',
    border: 0,
    borderRadius: 3,
    color: 'white',
  },

  root1: {
    display: "flex",
    "& > *": {
      margin: theme.spacing(1),
      width: theme.spacing(16),
      height: theme.spacing(16),
    },
  },
}));

export default function Dashboard() {

    const classes = useStyles();


  return (
    <div className={classes.root}>
      <Grid container spacing={0} justify="center">
        <Grid container spacing={0} justify="center">
          <Grid item xs={11} sm={12} md={7} lg={7}>

            <Grid container spacing={0} justify="center">
              <Grid item xs={11}>
                <Paper className={classes.paper} variant="outlined">

                <StudentDashItem/>
                </Paper>
              </Grid>
            </Grid>
          </Grid>

          <Grid item xs={12} sm={12} md={5} lg={4}>
            <Grid container spacing={1}>
              <Grid item xs={12} sm={12}>
                <Paper className={classes.paper} variant="outlined">
                  <DatePicker />
                </Paper>
              </Grid>
              <Grid item xs={12} sm={12}>
                <Paper className={classes.paper} variant="outlined">
                  <PieChart skill_type='existing' chart_header='Student has skill'/>
                  <div style={{height: '20px'}} />
                  <PieChart skill_type='desired' chart_header='Student want skill'/>
                  <div style={{height: '20px'}} />
                  <PieChart skill_type='course' chart_header='Most Desired Course'/>
                </Paper>
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>

    </div>
  );
}

