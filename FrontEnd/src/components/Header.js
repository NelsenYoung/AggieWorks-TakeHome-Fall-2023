import React from "react";

const Header = () => {
    const myStyle = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Sans-Serif"
    };
    return (
    <nav className='navbar'>
        <div className='nav-container'>
          <a className='navbar-title' href='#' style={{myStyle}}>
            Couch Surf
          </a>
        </div>
    </nav>
    )
}

export default Header