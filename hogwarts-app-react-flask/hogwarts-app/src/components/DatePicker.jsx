import 'date-fns';
import React, { useState, useEffect } from "react";
import Grid from '@material-ui/core/Grid';
import DateFnsUtils from '@date-io/date-fns';
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { MuiPickersUtilsProvider, KeyboardDatePicker } from '@material-ui/pickers';
import { getStudentsByDate } from '../lib/api'
import { getStudentsByMonth } from '../lib/api'

export default function DatePicker() {
    const theme = createMuiTheme({
        palette: {
          type: 'dark',
        },
      });
  const date = new Date();
  const [selectedDate, setSelectedDate] = React.useState(new Date(date.toISOString()));
  const [countStudents, setCountStudents] = useState('0')
  const [countStudentsByMonth, setCountStudentsByMonth] = useState('0')
  const [day, setDay] = useState()
  const [monthNum, setMonthNum] = useState()
  const months = [ "January", "February", "March", "April", "May", "June", 
           "July", "August", "September", "October", "November", "December" ];




  const fetchData = async (date) => {
     let shirtDate = date.toISOString().slice(0,10)
     shirtDate = shirtDate.split('-')
     let year = parseInt(shirtDate[0])
     let month = parseInt(shirtDate[1])
     setDay(parseInt(shirtDate[2]))
     setMonthNum(month)
     let num_of_students = await getStudentsByDate(date.toISOString().slice(0,10))
     console.log(num_of_students.data.total)
     let num_of_students_by_month = await getStudentsByMonth(month, year)
     setCountStudents(num_of_students.data.total)
     setCountStudentsByMonth(num_of_students_by_month.data.total)
};

const handleDateChange = (date) => {

    fetchData(date);
    setSelectedDate(date);
    
  };

useEffect(() => {
    fetchData(selectedDate);
}, []);

  return (
      <>
       {!countStudents ? 
       <div className='date-picker-text'>No students added on {day} of {months[monthNum - 1]} {selectedDate.toISOString().slice(0,4) && selectedDate.toISOString().slice(0,4)}</div> 
       : 
       <div className='date-picker-text'>{countStudents.toString()} students added on {day} of {months[monthNum - 1]} {selectedDate.toISOString().slice(0,4) && selectedDate.toISOString().slice(0,4)}</div>} 

              {!countStudentsByMonth ? 
       <div className='date-picker-text'>No students added on {months[monthNum - 1]}</div> 
       : 
       <div className='date-picker-text'>{countStudentsByMonth.toString()} students added in {months[monthNum - 1]}</div>} 

    <ThemeProvider  theme = {theme}>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Grid container justify="space-around">
        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          format="MM/dd/yyyy"
          margin="normal"
          id="date-picker-inline"
          label="Pick the date"
          value={selectedDate}
          onChange={handleDateChange}
          // KeyboardButtonProps={{
          //   'aria-label': 'change date',
          // }}
        />
      </Grid>
    </MuiPickersUtilsProvider>
    </ThemeProvider>
    </>
  );
}
