import React from 'react'
import {NavLink, useHistory} from "react-router-dom";
import {useContext} from "react";
import {AuthContext} from "../context/AuthContext";



export const Navbar = () => {
    const history= useHistory()
    const auth = useContext(AuthContext)

    const logoutHandler = event => {
        event.preventDefault()
        auth.logout()
        history.push("/")
    }

return(
    <nav>
        <div className="nav-wrapper  blue-grey darken-1"
        style={{padding: "0 2rem"}}>
            <span href="/" className="brand-logo">ER</span>
            <ul id="nav-mobile" className="right hide-on-med-and-down">
                <li><NavLink to="/create">Create</NavLink></li>
                <li><NavLink to="/camera">Camera</NavLink></li>
                <li><a href="/" onClick={logoutHandler}>Logout</a></li>
            </ul>
        </div>
    </nav>

)
}
