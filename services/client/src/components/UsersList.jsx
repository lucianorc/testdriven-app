import React from 'react'

const UsersList = (props) => {
  return (
    <div>
      {
        props.users.map((user) => {
          return (
            <h4
              className="box title is-4"
              key={user.id}
            >
              {user.username}
            </h4>
          )
        })
      }
    </div>
  )
}

export default UsersList