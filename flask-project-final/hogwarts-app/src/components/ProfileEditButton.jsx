import React from "react";
import "./CSS/ProfileEditButton.css";


export default class EditButton extends React.Component {
  constructor() {
    super();
    this.state = {
      clicked: true,
    };
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick(func) {
    this.setState({
      clicked: !this.state.clicked,
    });
    func();
  }

  render() {
    const { handleEditButton } = this.props
    const label = this.state.clicked
      ? "Edit"
      : "Back to profile";
    return (

          <div className="filter-button-wrapper">
            <button
              className={`box ${this.state.clicked ? "" : "active"}`}
              onClick={() =>
                this.handleClick(handleEditButton)
              }
            >
              {label}
            </button>
          </div>

    );
  }
}
