import React from "react";
import { getAllStudents } from '../lib/api'
import './CSS/StudentListItem.module.css'
import StudentListItem from './StudentListItem'
  


export default class AllStudents extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            students_json: {}
        };
      }
componentDidMount(){
    this.stud()
}

async stud(){
    let res = await getAllStudents()
    this.setState({students_json: await res.data})
    console.log(res.data)
}

render(){
    let json = this.state.students_json
    let arr = [];
    Object.keys(json).forEach(function(key) {
      arr.push(json[key]);
    });
    return(
        <div>
            {this.state.students_json && console.log(json[1])}

                 {this.state.students_json && arr.map((item) => 
        <StudentListItem key={item._id['$oid']} 
            first_name={item.first_name} 
            last_name={item.last_name} 
            desired_magic_skills={item.desired_magic_skills} 
            existing_magic_skills={item.existing_magic_skills} 
            interested_in_course={item.interested_in_course}
            student_id = {item._id['$oid']}
            className={`${"userName-align-left"}`}/>) }
        </div>

    )
}
}

