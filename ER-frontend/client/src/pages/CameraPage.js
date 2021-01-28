import React from 'react'
import Webcam from "react-webcam";
import '../public/stylesheets/camera-page.css'

export const CameraPage = () => {
    const webcamRef = React.useRef(null);
    const [imgSrc, setImgSrc] = React.useState(null);

    const capture = React.useCallback(() => {
        const imageSrc = webcamRef.current.getScreenshot();
        setImgSrc(imageSrc);
    }, [webcamRef, setImgSrc]);

    const handleDownload = React.useCallback(() => {
        if (imgSrc) {
            const link = document.createElement("a");
            document.body.appendChild(link);
            //link.style = "display: none";
            link.href = imgSrc;
            let data = new Date();
            const imageName = `${data.getDate()}${data.getMonth()}${data.getFullYear()}_${data.getHours()}${data.getMinutes()}${data.getSeconds()}_${data.getMilliseconds()}`
            link.download = `${imageName}.jpeg`;
            link.click();
            window.URL.revokeObjectURL(imgSrc);
            setImgSrc(imgSrc);
        }
    }, [imgSrc]);

    const handleSend = React.useCallback(() => {


    },[]);


    return (
        <>
            <div id ='buttons'>
                <button onClick={capture}>Screenshot</button>
                <button onClick={handleDownload}>Download</button>
                <button onClick={handleSend}>Send</button>
            </div>
            <div id='camera'>
                <Webcam
                    audio={false}
                    ref={webcamRef}
                    screenshotFormat="image/jpeg"
                />

                {imgSrc && (
                    <img
                        src={imgSrc}
                    />

                )}
            </div>



        </>
    );
}
