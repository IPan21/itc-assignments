import React, { Component } from 'react'
import jwt_decode from 'jwt-decode'
import './CSS/StudentListItem.module.css'



class UserProfile extends Component {
    constructor() {
        super()
        this.state = {
            first_name: '',
            last_name: '',
            email: ''
        }
    }

    componentDidMount () {
        if (localStorage.usertoken){
            const token = localStorage.usertoken
            const decoded = jwt_decode(token)
             this.setState({
                first_name: decoded.identity.first_name,
                last_name: decoded.identity.last_name,
                email: decoded.identity.email
        }) 
        } else {
            this.props.history.push(`/login`)
        }

    }

    render () {

        return (
        
  <div className="user-profile-wrapper">
                        <div className="font-profile"> User Profile</div>
                    <div className="date-align-right font-profile-grey">First Name:</div>
                  <div className="font-profile">{this.state.first_name}</div>

                  <div className="date-align-right font-profile-grey">Last Name:</div>
                  <div className="font-profile">{this.state.last_name}</div>

                  <div className="date-align-right font-profile-grey">Email:</div>
                  <div className="font-profile">{this.state.email}</div>

            </div>

        )
    }
}


export default UserProfile;