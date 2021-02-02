import React from 'react'
import Webcam from "react-webcam";
import '../public/stylesheets/camera-page.css'

<<<<<<< HEAD

export const CameraPage = () => {
    const webcamRef = React.useRef(null);
    const [imgScreenshotSrc, setImgSrc] = React.useState(null);
    const [imgInputSrc, setImgInputSrc] = React.useState(null);
    //const inputFile = React.createRef();


    const capture = React.useCallback(() => {
        //скрин с камеры (его можно скачать)
        const tempImgSrc = webcamRef.current.getScreenshot();
        setImgSrc(tempImgSrc);
    }, [webcamRef, setImgSrc]);

    const handleDownload = React.useCallback(() => {
        if (imgScreenshotSrc) {
            const link = document.createElement("a");
            document.body.appendChild(link);
            link.href = imgScreenshotSrc;
=======
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
>>>>>>> liubov-frontend
            let data = new Date();
            const imageName = `${data.getDate()}${data.getMonth()}${data.getFullYear()}_${data.getHours()}${data.getMinutes()}${data.getSeconds()}_${data.getMilliseconds()}`
            link.download = `${imageName}.jpeg`;
            link.click();
<<<<<<< HEAD
            window.URL.revokeObjectURL(imgScreenshotSrc);

        }
    }, [imgScreenshotSrc]);


    const handleSend = React.useCallback(() => {

    }, []);

    const handleClear = React.useCallback(() => {
        setImgInputSrc("")

    }, [setImgInputSrc]);

    const handleDisplay = e => {
        //изображение из файловой системы

        // let file = inputFile.current.files[0];
        let file = e.target.files[0];
        let reader = new FileReader();
        reader.onloadend = () => {
            setImgInputSrc(reader.result)
        }
        if (file) {
            reader.readAsDataURL(file);
        } else {
            setImgInputSrc("");
        }


    }

    return (
        <>
            <h2>Image from camera</h2>
            <div className="Webcam">
                <div className="camera">
                    <Webcam
                        audio={false}
                        ref={webcamRef}
                        screenshotFormat="image/jpeg"
                    />
                    <button className="ScreenshotButton" onClick={capture}>Screenshot</button>
                </div>
                <div className="screenshotImage">
                    {
                        imgScreenshotSrc
                        && (<img src={imgScreenshotSrc}/>)
                    }
                    {
                        imgScreenshotSrc
                        && (<button className="DownloadButton" onClick={handleDownload}>Download</button>)
                    }

                </div>
            </div>
            <h2>Image from file system</h2>
            <div className="FileInput">
                <input
                    className="fileInput"
                    id="fileInput"
                    type="file"
                    onChange={handleDisplay}
                />
                <label className="ImageInputButton" htmlFor="fileInput">Image input</label>
                <img className="inputImage" src={imgInputSrc} height="500" alt=""/>
                {
                    imgInputSrc && (<button className="ClearButton" onClick={handleClear}>Clear</button>)
                }
            </div>
            <h2>Send image on server</h2>
            <div className="ServerSender">
                <button onClick={handleSend}>Send</button>
            </div>

        </>
    );

=======
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
>>>>>>> liubov-frontend
}
