import React from 'react';
import { withStyles,makeStyles,} from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';


const CssTextField = withStyles({
  root: {
    '& label.Mui-focused': {
      color: 'grey',
    },
    '& .MuiInput-underline:after': {
      borderBottomColor: 'grey',
    },
    '& .MuiOutlinedInput-root': {
      '& fieldset': {
        borderColor: 'white',
      },
      '&:hover fieldset': {
        borderColor: 'white',
        borderWidth: '2px'
      },
      '&.Mui-focused fieldset': {
        borderColor: 'grey',
        borderWidth: '2px'
      },
    },
  },
})(TextField);


const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  margin: {
    margin: theme.spacing(1),
  },
}));



export default function CSSTextField(props) {
  const classes = useStyles();
  const {onBlur, value, onChange, name, classname, placeholder} = props

  return (
      <>
            <CssTextField
        type="text"
        name={name}
        id={name}
        onBlur={onBlur}
        onChange={onChange}
        value={value}
        placeholder={placeholder}
        className={`${classes.margin}, ${classname}`}
        variant="outlined"
        inputProps={{
            maxLength: 20,
            style: { fontFamily: "Arial", color: "white", margin: "0 0 0 0", flex: 2,},
          }}style={{ flex: 2, margin: "0 0 0 0", width: "100%", }}>
        <label htmlFor="contained-button-file"></label>
    </CssTextField>


                    </>
  );
}
