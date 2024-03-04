import React from 'react'
import "./profile.css"
import Topbar from '../../components/topbar/Topbar'
import Sidebar from'../../components/sidebar/Sidebar'
import Feed from '../../components/feed/Feed'
import Rightbar from '../../components/rightbar/Rightbar'

export default function Profile() {
  return (
    <>
    <Topbar />
    <div className="profile">
      <Sidebar />
      <div className="profileRight">
        <div className="profileRightTop">
          <div className="profileCover">
            <img src='assets/post/3.jpeg' className='profileCoverImg' />
            <img src='assets/person/3.jpeg' className='profileUserImg' />
          </div>
          <div className="profileInfo">
            <h4 className="profileInfoName">Name</h4>
            <span className="profileInfoDesc">Desc</span>
          </div>
        </div>
        <div className="profileRightBottom">
          <Feed />
          <Rightbar profile/>
        </div>
      </div>
      
    </div> 
  </>
  )
}
