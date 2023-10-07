import './App.css';
import React, {useState, useEffect} from 'react';
import api from './api';
import Location from './components/Location';

const App = () => {
  const [locations, setLocations] = useState([])

  const fetchLocations = async () =>{
    const response = await api.get('/locations/');
    setLocations(response.data)
  };

  useEffect(() => {
    fetchLocations();
  }, []);

  const headStyle = {
    color: 'white',
    backgroundColor: '#113946',
    padding: "10px",
    fontFamily: "Sans-Serif"
};

const titleStyle = {
  color: '#113946',
  fontSize: 48 
}

  return(
    <div className="App">
      <h1 align="left" style={headStyle}>Couch Surf</h1>
        <div className='container'>
          <h1 className='title' style={titleStyle}>Current Locations</h1>
          <div className='row'>
                {locations.map((location) =>
                 <Location id={location.id} address={location.address} price={location.price} availability={location.availability}/>
                )}
          </div>
        </div>
    </div>
  )
}

export default App;

