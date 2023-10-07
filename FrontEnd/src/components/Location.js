import React, { useEffect, useState} from "react";
import api from "../api";

function Location(props){ 

// Update the data after the reservation is changed
const [locations, setLocations] = useState([])

const fetchLocations = async () =>{
  const response = await api.get('/locations/');
  setLocations(response.data)
};

useEffect(() => {
  fetchLocations();
}, []);

const [buttonText, setButtonText] = useState('Reserve Location');
const setButtonTexts = () => {
  if(props.availability){
    setButtonText("Unreserve")
  }else{
    setButtonText("Reserve Location")
  }
}

useEffect(() => {
  setButtonTexts();
}, []);

// Update the reservation and send the data to the backend
const [locationData, setLocationData] = useState({
  address: props.address,
  availability: props.availability,
  price: props.price
})

 const handleButtonPress = async (event) => {
  event.preventDefault();
  if(locationData.availability == true){
    setButtonText("Reserve Location")
    const db_loc = '/locations/' + String(props.id)
    await api.patch(db_loc, {address: props.address, 
                             availability: false,
                             price: props.price});
    fetchLocations();
    setLocationData({
      address: props.address,
      availability: false,
      price: props.price
 })
  }else{
    setButtonText("Unreserve")
    const db_loc = '/locations/' + String(props.id);
    await api.patch(db_loc, {address: props.address, 
                             availability: true,
                             price: props.price});
    fetchLocations();
    setLocationData({
      address: props.address,
      availability: true,
      price: props.price
   })  
  }
 }
 
const buttonStyle = {
  color: '#FFF2D8',
  backgroundColor: '#113946',
  fontSize: 16,
  borderRadius: 2,
  margin: 10
}
    return(
    <div className='col-4'>
      <h3>{props.address}</h3>
      <p>${props.price}</p>
      <button onClick={handleButtonPress} style={buttonStyle}>{buttonText}</button>
  </div>
  );
}

export default Location