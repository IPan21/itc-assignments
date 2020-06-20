
import React from "react";
import Button from '@material-ui/core/Button';
import { updateStudent } from '../lib/api'
import { Formik } from "formik";
import * as Yup from "yup";
import { withStyles } from '@material-ui/core/styles';
import MultipleSelect from './AddStudentsSelect'
import Typography from '@material-ui/core/Typography';
import Error from "./Error";
import CSSTextField from './AddStudentInput'

const ValidationSchema = Yup.object().shape({
    first_name: Yup.string()
    .min(1, "Too Short!")
    .max(50, "Too Long!"),


    last_name: Yup.string()
    .min(1, "Too Short!")
    .max(50, "Too Long!")

    // existing_magic_skills: Yup.array()
    // .required("Required"),

    // desired_magic_skills: Yup.array()
    // .required("Required"),

    // courses: Yup.array()
    // .required("Required"),
  });
  

const styles = theme => ({
  root: {
    "& .MuiTextField-root": {
      margin: theme.spacing(1),
      width: "26ch",
      color: "#000000"
    }
}
})


class EditProfile extends React.Component {
    state = {
            name: []
          };
    constructor(props) {
        super(props);
        this.state = {
          loading: true,
          text: '',
          date: '',
          buttoncolor: 'primary',
          errorMessage: false,
        };
      }

    getCurrentDate() {    
        const tempDate = new Date();
        const currDate = tempDate.toISOString();
        return currDate;       
      }

    // handleOnSubmit(values) {
    //     addStudent(values)
    // }

      handleSelectChange = event => {
    this.setState({ name: event.target.value });
  };

    render() {
        const { student } = this.props

        return (
            <>
            <Formik
              initialValues={{ first_name: "", last_name: "", existing_magic_skills: [], desired_magic_skills: [], interested_in_course: [],}}
                validationSchema={ValidationSchema}
              validate={values => {
                let errors = {};
                 if (values.first_name.length >= 50) {
                    errors.first_name = `Max 50 characters`;
                  } else if (values.last_name.length >= 50) {
                        errors.last_name = `Max 50 characters`;
                  }
                return errors;
              }}
             onSubmit={async (values, { setSubmitting, resetForm }) => {
                this.setState({buttoncolor: 'inherit'})
                this.setState({errorMessage : false})
                setSubmitting(false);
                console.log(values)
                
                
                // const datetime = this.getCurrentDate()
                resetForm();
                updateStudent(student._id, values)
                let a = values.toString()
                console.log(a)
                setSubmitting(true);
                this.setState({buttoncolor: 'primary'})
                }}
              >
            
                {({
                values,
                errors,
                touched,
                handleChange,
                handleBlur,
                handleSubmit,
                isSubmitting,
              }) => (
            <form className={`${styles.root}`} autoComplete="off" onSubmit={handleSubmit}>





                <CSSTextField
                    name="first_name"
                    id="first_name"
                    onChange={handleChange}
                    onBlur={handleBlur}
                    value={values.first_name}
                    color={this.state.buttoncolor}
                    placeholder={student.first_name}
                  >
                    ), }} ><label htmlFor="contained-button-file"></label>
                  </CSSTextField>
                <Error touched={touched.first_name} message={errors.first_name} />

                <CSSTextField
                    name="last_name"
                    id="last_name"
                    onChange={handleChange}
                    onBlur={handleBlur}
                    value={values.last_name}
                    color={this.state.buttoncolor}
                    placeholder={student.last_name}
                  >
                    ), }} ><label htmlFor="contained-button-file"></label>
                  </CSSTextField>
                <Error touched={touched.last_name} message={errors.last_name} />

                    <MultipleSelect 
                            onChange={handleChange}
                            id="existing_magic_skills"
                            name='existing_magic_skills'
                            value={values.existing_magic_skills}
                            placeholder="Existing magic skills"
                    />
                <Error touched={touched.existing_magic_skills} message={errors.existing_magic_skills} />

              
                    <MultipleSelect 
                            onChange={handleChange}
                            id="desired_magic_skills"
                            name='desired_magic_skills'
                            value={values.desired_magic_skills}
                            placeholder="Desired magic skills"
                    />

                <Error touched={touched.desired_magic_skills} message={errors.desired_magic_skills} />


                <MultipleSelect 
                            onChange={handleChange}
                            id="interested_in_course"
                            name='interested_in_course'
                            value={values.interested_in_course}
                            placeholder="Interested in course"
                    />

                <Error touched={touched.interested_in_course} message={errors.interested_in_course} />


                <Button type="submit" variant="contained" color={this.state.buttoncolor} position="end" disabled={isSubmitting}>
                            Send
                        </Button>
            </form>
                  )}
                    
                  </Formik>
                  {this.state.errorMessage && <Typography>Message was't sent. Try again.</Typography>}
            </>      
          );
    }

  
}

export default withStyles(styles)(EditProfile)

