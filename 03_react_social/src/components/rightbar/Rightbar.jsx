import React from 'react'
import "./rightbar.css"
import { Users } from '../../dummyData'
import Online from '../online/Online'

export default function Rightbar({profile}) {
  const HomeRightbar = () =>{
        return(
          <>
          <div className="birthdayContainer">
              <img src='/assets/gift.png' className='birthdayImg'/>
              <span className="birthdayText">
                <b>Pola Fosetr</b> and <b>3 other freinds </b> have a birthday today </span>
            </div>
            <img className='rightbarAd' src="/assets/add.png" alt="" />
            <h4 className="rightbarTitle">Online Freinds</h4>
            <ul className="rightFreindlist">
                {Users.map( u => (
                  <Online  key={u.id} user={u}/>
                ))}
            </ul>
          </>
        )
      }

  const ProfileRightBar = () =>{
    return (
      <>
        <h4 className='rightbarTitle'>
          User Information
        </h4>
        <div className="rightbarInfo">
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">City</span>
            <span className="rightbarInfoValue">New York</span>
          </div>
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">From</span>
            <span className="rightbarInfoValue">Madrid</span>
          </div>
          <div className="rightbarInfoItem">
            <span className="rightbarInfoKey">Relationship</span>
            <span className="rightbarInfoValue">Single</span>
          </div>
        </div>
        <h4 className='rightbarTitle'>
          User Freinds
        </h4>
        <div className="rightbarFollowings">
          <div className="rightbarFollowing">
            <img src="/assets/person/1.jpeg" alt="" className="rightbarFollowingImg" />
            <span className="rightbarFollowingName">John Doe</span>
          </div>
        </div>
      </>
    )
  }
  return (
    <div className='rightbar'>
      <div className="rightbarWrapper">
          {profile ? <ProfileRightBar /> : <HomeRightbar />}
      </div>
    </div>
  )
}
