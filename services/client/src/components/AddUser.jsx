import React from 'react'

const AddUser = (props) => {
  return (
    <form onSubmit={(event) => props.addUser(event)}>
      <div className="field">
        <input
          type="text"
          className="input is-large"
          name="username"
          placeholder="Enter an username"
          required
          value={props.username}
          onChange={props.handleChange}
        />
        <input
          type="text"
          className="input is-large"
          name="email"
          placeholder="Enter an email address"
          required
          value={props.email}
          onChange={props.handleChange}
        />
        <input
          type="submit"
          className="button is-primary is-large is-fullwidth"
          value="Submit"
        />
      </div>
    </form>
  )
}

export default AddUser