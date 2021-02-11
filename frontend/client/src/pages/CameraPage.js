import React, {useContext} from 'react'
import '../public/stylesheets/camera-page.css'
import {WebCamera} from "../components/WebCamera";
import {ImageInput} from "../components/ImageInput";
export const CameraPage = () => {

    return (
        <>
            <h2>Image from camera</h2>
            <WebCamera/>
            <h2>Image from file system</h2>
            <ImageInput/>
        </>
    );

}
