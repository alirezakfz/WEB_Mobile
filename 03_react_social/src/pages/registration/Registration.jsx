import React from 'react'
import './registration.css'

export default function registration() {
  return (
    <div className="registration">
        <div className="registrationWrapper">
            <div className="registrationLeft">
                <h3 className="registrationLogo">Lamasocial</h3>
                <span className="registrationDescription">
                    Connect with freinds and the world around you on Lamasocial.
                </span>
            </div>
            <div className="registrationRight">
                <div className="registrationBox">
                    <input type="text" placeholder='Username' className="registrationInput" />
                    <input type="email" placeholder='Email' className="registrationInput" />
                    <input type="password" placeholder='Password' className="registrationInput" />
                    <input type="password" placeholder='Retype Password' className="registrationInput" />
                    <button className="registrationButton">Sign Up</button>
                    <button className="registrationRegisterButton">Log inot Account</button>
                </div>
            </div>

        </div>
    </div>
  )
}
