import React from 'react'
import "./online.css"

export default function Online({user}) {
  return (
    <li className="rightbarFreind">
        <div className="rightbarProfileImgContainer">
        <img className='rightbarProfileImg' src={user.profilePicture} />
        <span className="rightbarOnline"></span>
        </div>
        <span className="rightbarUsername">{user.username}</span>
    </li>    
  )
}
