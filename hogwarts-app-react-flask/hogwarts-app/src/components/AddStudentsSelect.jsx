import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Input from "@material-ui/core/Input";
import InputLabel from "@material-ui/core/InputLabel";
import MenuItem from "@material-ui/core/MenuItem";
import FormControl from "@material-ui/core/FormControl";
import Select from "@material-ui/core/Select";
import Chip from "@material-ui/core/Chip";
import { createMuiTheme, ThemeProvider } from '@material-ui/core/styles';




const useStyles = makeStyles(theme => ({
    select: {
        '&:before': {
            borderColor: 'white',
        },
        '&:focused': {
            borderColor: 'white',
        },
        '&:after': {
            borderColor: 'white',
        }
    },
    icon: {
        fill: '#ffffff',
    },
  formControl: {
    margin: theme.spacing(1),
    minWidth: 300,
    maxWidth: 300
  },
  chips: {
    width: 300,
    display: "flex",
    flexWrap: "wrap"
  },
  chip: {
    margin: 2
  },
  noLabel: {
    marginTop: theme.spacing(3)
  }
}));

const ITEM_HEIGHT = 48;
const ITEM_PADDING_TOP = 8;
const MenuProps = {
  PaperProps: {
    style: {
      maxHeight: ITEM_HEIGHT * 4.5 + ITEM_PADDING_TOP,
      width: 250
    }
  }
};

const courses = [
    'Muggle Studies',
    'Divination',
    'Ancient Runes',
    'Care of Magical Creatures',
    'Arithmancy',
    'Flying',
    'Defense Against the Dark Arts',
    'Herbology',
    'Astronomy',
    'History of Magic',
    'Potions',
    'Transfiguration',
    'Charms'
];

const names = [
    'Lycanthropy',
    'Veela Charm',
    'Magical Resistance',
    'Parseltongue',
    'Legilimency And Occlumency',
    'Seeing',
    'Wandless Magic',
    'Apparition',
    'Animagus',
    'Metamorphmagi'
];

function getStyles(name, personName, theme) {
  return {
    fontWeight:
      personName.indexOf(name) === -1
        ? theme.typography.fontWeightRegular
        : theme.typography.fontWeightMedium
  };
}

export default function MultipleSelect(props) {
    const theme = createMuiTheme({
        palette: {
          type: 'dark',
        },
      });
  const classes = useStyles();
//   const theme = useTheme();
//   const [personName, setPersonName] = React.useState([]);
const { value, onChange, id, name, placeholder } = props
//   const handleChange = event => {
//     setPersonName(event.target.value);
//     console.log(personName)
//   };

  return (
    <div>
      <FormControl className={classes.formControl}>
      <ThemeProvider theme = {theme}>
  <InputLabel id="demo-mutiple-chip-label">{placeholder}</InputLabel>
        
        <Select
          labelId={(id + 'label')}
          id={id}
          name={name}
          className={classes.select}
          multiple
          value={value}
          onChange={onChange}
          input={<Input id="select-multiple-chip" />}
          renderValue={selected => (
            <div className={classes.chips}>
              {selected.map(value => (
                <Chip key={value} label={value} className={classes.chip} />
              ))}
            </div>
          )}
          MenuProps={MenuProps}
        >
            {id !== 'interested_in_course' &&
          names.map(name => (
            <MenuItem key={name} value={name} style={getStyles(name, value, theme)} >
              {name}
            </MenuItem>
          ))}

            {id === 'interested_in_course' &&
          courses.map(name => (
            <MenuItem key={name} value={name} style={getStyles(name, value, theme)} >
              {name}
            </MenuItem>
          ))}
        </Select>
        </ThemeProvider>
      </FormControl>
    </div>
  );
}
