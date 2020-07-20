import React from 'react';
import logo from './logo.svg';
import './App.css';
import { GoogleLogin, GoogleLogout } from 'react-google-login';

const CLIENT_ID = process.env.REACT_APP_GOOGLE_CLIENT_ID || "";

function App() {
    console.log(CLIENT_ID);
  return (
    <div className="App">
      <GoogleLogin
          clientId={CLIENT_ID}
          buttonText='Login'
          onSuccess={ (response)=>{console.log(response);} }
          onFailure={ (response)=>{console.log(response);} }
          cookiePolicy={ 'single_host_origin' }
          responseType='code,token'
        />
    </div>
  );
}

export default App;
