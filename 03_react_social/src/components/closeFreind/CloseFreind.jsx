import React from 'react'
import "./closeFreind.css"

export default function CloseFreind({user}) {
  return (
    <li className="sidebarFriend">
        <img className='sidebarFreindImg' src={user.profilePicture} alt='' />
        <span className="sidebarFreindName">{user.username}</span>
    </li>
  )
}
