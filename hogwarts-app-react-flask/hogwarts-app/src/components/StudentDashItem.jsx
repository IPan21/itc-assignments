import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActions from '@material-ui/core/CardActions';
import CardContent from '@material-ui/core/CardContent';
import Button from '@material-ui/core/Button';
import Typography from '@material-ui/core/Typography';
import { getAllStudents } from '../lib/api'
import { removeStudentById } from '../lib/api'
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';
import { withRouter } from 'react-router-dom';


const useStyles = makeStyles({
  root: {
    // minWidth: 260,
    // maxWidth: 300,
    width: 250,
    margin: '10px',
    background: '#343A40',
  },
  bullet: {
    display: 'inline-block',
    margin: '0 2px',
    transform: 'scale(0.8)',
  },
  title: {
    fontSize: 14,
  },
  pos: {
    marginBottom: 12,
  },
});

function OutlinedCard(props) {
    const handleClick = (func, self, student_id) => {
        func(self, student_id);
      }
    const theme = createMuiTheme({
        palette: {
          type: 'dark',
        },
      });
  const classes = useStyles();
  const { first_name, last_name, existing_magic_skills, handleRemoveButtonClick, self, student_id } = props;

  

  return (
      <ThemeProvider  theme = {theme}>
    <Card className={classes.root} variant="outlined">
      <CardContent>
        <Typography className={classes.title} color="textSecondary" gutterBottom>
          Student
        </Typography>
        <Typography variant="h5" component="h2">
        {first_name} {last_name}
        </Typography>
        <Typography className={classes.pos} color="textSecondary">
          Magic Skills
        </Typography>
        <Typography variant="body2" component="p">
        {existing_magic_skills}
          <br />
          {'"a benevolent smile"'}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size="small" onClick={() => handleClick(handleRemoveButtonClick, self, student_id)}>Remove student</Button>
      </CardActions>
    </Card>
    </ThemeProvider>
  );
}


class StudentsDashItem extends React.Component {
    constructor() {
        super();
        this.state = {
            students_json: {},
            student_count: 0,
            search: null,
            inputVal: '',
        };
      }
componentDidMount(){
    this.getStudents()
    this.setState({student_count: this.state.students_json.length})
    let query = this.props.location.search
    if (query.length > 0) {
      query = query.split('=')[1]
      this.setState({search:query})
      this.setState({inputVal:query})
    }
}

async getStudents(){
    let res = await getAllStudents()
    this.setState({students_json: {}})
    this.setState({student_count: res.data.length})
    this.setState({students_json: res.data})
    return res.data
}

addToQuery(input) {
  if (input.length === 0) {
    this.props.history.push('/')
  } else {
    this.props.history.push('?query=' + input)
  }
}

searchSpace=(event)=>{
  console.log(this.state.inputVal)
  let keyword = event.target.value;
  this.setState({search:keyword})
  this.setState({inputVal:keyword})
  this.addToQuery(keyword)
}


async handleRemoveButtonClick(self, student_id) {
    let res = await removeStudentById(student_id)
    console.log(await res)
    res = await self.getStudents()
    console.log(await res)
    console.log(self.state.student_count)
}

render() {
    let json = this.state.students_json
    let arr = [];
    Object.keys(json).forEach(function(key) {
      arr.push(json[key]);
    });
    const { inputVal } = this.state
    let listToRender = arr.sort(function(a, b){
      if(a.first_name < b.first_name) { return -1; }
      if(a.first_name > b.first_name) { return 1; }
      return 0;
  }).filter((data)=>{
      if(this.state.search == null)
          return data
      else if(data.last_name.toLowerCase().includes(this.state.search.toLowerCase()) 
                    // || data.description.toLowerCase().includes(this.state.search.toLowerCase())
                    ){
          return data
      }
    }).map(item => <OutlinedCard key={item._id['$oid']} 
    first_name={item.first_name} 
    last_name={item.last_name} 
    desired_magic_skills={item.desired_magic_skills} 
    existing_magic_skills={item.existing_magic_skills} 
    interested_in_course={item.interested_in_course}
    student_id = {item._id['$oid']}
    self = {this}
    handleRemoveButtonClick = {this.handleRemoveButtonClick}
    className={`${"userName-align-left"}`}/>)
    return(
        <>
                    <div>
      <input type="text" value={inputVal} placeholder="Search by last name" className='search-input' onChange={(e)=>this.searchSpace(e)} />
      <div className="student-dash-wrapper">{listToRender}</div>
      </div>

      Students total: {this.state.student_count}
        <div className="student-dash-wrapper">
                </div>
                </>

    )
}

}

export default withRouter(StudentsDashItem)